"""Project-bound resume gates. Local approval records are not authentication."""
from guard_common import approval, digest, exact, inside, safe_path, text, version, validate_schema

from decimal import Decimal, ROUND_HALF_UP
from secure_io import read_bytes, stable_io


def number(value):
    if not isinstance(value, str):
        raise ValueError('Decimal strings required')
    result = Decimal(value)
    if not result.is_finite() or result < 0:
        raise ValueError('nonfinite or negative amount')
    return result


def check_evidence(evidence, source_ids):
    exact(evidence, 'schema_version kind project_id revision quantity_evidence price_evidence lines division_totals subtotal markup_rate markup_basis fee total currency rounding quantum')
    version(evidence, 'pricing_evidence')
    if evidence['rounding'] != 'ROUND_HALF_UP' or evidence['quantum'] != '0.01' or evidence['markup_basis'] != 'subtotal':
        raise ValueError('unsupported rounding/markup; manual reconciliation required')
    def rounded(value):
        return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    quantities, prices = {}, {}
    for q in evidence['quantity_evidence']:
        exact(q, 'id source_id unit rating')
        if q['id'] in quantities or q['source_id'] not in source_ids or q['rating'] not in ('A','B','C','D'):
            raise ValueError('invalid quantity provenance')
        quantities[q['id']] = q
    for p in evidence['price_evidence']:
        exact(p, 'id source_id unit currency source_type market base_rate locality escalation adjustment_basis confidence override override_reason disposition reviewer')
        if p['id'] in prices or p['source_type'] not in ('quote','historical','published','assumption'):
            raise ValueError('invalid price provenance')
        if p['source_id'] not in source_ids and not (p['source_type'] == 'assumption' and p['source_id'] is None):
            raise ValueError('orphan price source')
        for field in ('market', 'adjustment_basis', 'confidence'):
            text(p[field])
        if p['override'] is not None:
            number(p['override'])
            text(p['override_reason'])
        prices[p['id']] = p
    seen, divisions = set(), {}
    for line in evidence['lines']:
        exact(line, 'id division quantity unit rate amount currency quantity_ref price_ref derivation allowance')
        text(line['id'])
        text(line['division'])
        if line['id'] in seen:
            raise ValueError('duplicate line')
        seen.add(line['id'])
        if line['quantity_ref'] not in quantities or line['price_ref'] not in prices:
            raise ValueError('orphan quantity/price evidence reference')
        q, p = quantities[line['quantity_ref']], prices[line['price_ref']]
        if line['unit'] != q['unit'] or line['unit'] != p['unit']:
            raise ValueError('unit conversion unsupported')
        if line['currency'] != p['currency'] or line['currency'] != evidence['currency']:
            raise ValueError('currency conversion unsupported')
        if line['derivation'] != 'quantity * rate' or type(line['allowance']) is not bool:
            raise ValueError('unsupported derivation/allowance')
        rate = number(p['base_rate']) * number(p['locality']) * number(p['escalation'])
        rate = number(p['override']) if p['override'] is not None else rounded(rate)
        if number(line['rate']) != rate:
            raise ValueError('adjusted rate mismatch')
        amount = rounded(number(line['quantity']) * rate)
        if amount != number(line['amount']):
            raise ValueError('extension mismatch')
        divisions[line['division']] = divisions.get(line['division'], Decimal(0)) + amount
    if {k: number(v) for k, v in evidence['division_totals'].items()} != divisions:
        raise ValueError('division total mismatch')
    subtotal = sum(divisions.values(), Decimal(0))
    fee = rounded(subtotal * number(evidence['markup_rate']))
    if (number(evidence['subtotal']), number(evidence['fee']), number(evidence['total'])) != (subtotal, fee, subtotal + fee):
        raise ValueError('recomputed total mismatch')


PHASES = ('scope', 'takeoff', 'pricing', 'artifact')
STATE_KEYS = ('schema_version kind root workflow_id project_id project_name revision stage status domain '
              'issuance sources scope scope_digest pricing_digest phases approvals artifacts exceptions next_safe_action')


@stable_io
def check_workflow(state, evidence):
    validate_schema(state, 'workflow_state')
    validate_schema(evidence, 'pricing_evidence')
    exact(state, STATE_KEYS)
    version(state, 'workflow_state')
    version(evidence, 'pricing_evidence')
    root = safe_path(state['root'])
    if not root.is_dir():
        raise ValueError('missing project root')
    for field in ('workflow_id', 'project_id', 'project_name', 'revision'):
        text(state[field])
    if state['project_id'] != evidence['project_id'] or state['revision'] != evidence['revision']:
        raise ValueError('wrong project/revision evidence')
    if state['issuance'] != 'not_issued':
        raise ValueError('issuance forbidden')
    if state['scope_digest'] != digest(state['scope']) or state['pricing_digest'] != digest(evidence):
        raise ValueError('scope/pricing digest changed; approvals invalidated')
    ids = set()
    for source in state['sources']:
        exact(source, 'id project_id path sha256 revision date locator missing_reason')
        text(source['id'])
        if source['id'] in ids or source['project_id'] != state['project_id']:
            raise ValueError('duplicate or wrong-project source')
        ids.add(source['id'])
        if digest(read_bytes(inside(root, source['path']))) != source['sha256']:
            raise ValueError('source changed; quantities, prices and approvals invalidated')
        for field in ('revision', 'date', 'locator'):
            if source[field] is None:
                text(source['missing_reason'])
            else:
                text(source[field])
    if not evidence['lines'] and (state['phases']['pricing']['status'] != 'pending' or evidence['price_evidence']):
        raise ValueError('priced lines required after pricing or when price evidence exists')
    check_evidence(evidence, ids)
    exact(state['phases'], ' '.join(PHASES))
    next_action = 'human_review'
    pending = False
    for phase in PHASES:
        record = state['phases'][phase]
        exact(record, 'status reason')
        if record['status'] not in ('complete', 'pending', 'not_applicable'):
            raise ValueError('unknown phase status')
        if record['status'] == 'not_applicable':
            text(record['reason'])
            if state['stage'] != 'ROM':
                raise ValueError('only ROM permits phase skips')
        if record['status'] == 'pending' and not pending:
            next_action, pending = phase, True
        elif pending and record['status'] == 'complete':
            raise ValueError('out-of-order completed phase')
    if state['next_safe_action'] != next_action:
        raise ValueError('unsafe next action; expected ' + next_action)
    valid = []
    for record in state['approvals']:
        purpose = record.get('purpose')
        if purpose not in ('scope', 'pricing', 'estimate_final'):
            raise ValueError('unsupported approval purpose')
        bound = {k: state[k] for k in ('project_id', 'revision', 'scope_digest', 'sources')}
        if purpose == 'pricing':
            bound['pricing_digest'] = state['pricing_digest']
        if purpose == 'estimate_final':
            bound = {k: v for k, v in state.items() if k not in ('approvals', 'status')}
        approval(record, digest(bound), purpose)
        if purpose in valid:
            raise ValueError('duplicate approval')
        valid.append(purpose)
    if state['phases']['scope']['status'] == 'complete' and 'scope' not in valid:
        raise ValueError('completed scope needs scope approval')
    if state['phases']['pricing']['status'] == 'complete' and 'pricing' not in valid:
        raise ValueError('completed pricing needs pricing approval')
    if state['stage'] not in ('ROM', 'conceptual', 'formal') or state['status'] not in ('draft', 'needs_review', 'needs_human', 'approved_for_final', 'final_verified'):
        raise ValueError('unsupported stage/status')
    if state['domain'] not in ('estimate', 'contract', 'incident-report', 'sub-pay-app'):
        raise ValueError('unsupported consequential domain')
    for exception in state['exceptions']:
        exact(exception, 'id owner reason next_action')
        for value in exception.values():
            text(value)
    for artifact in state['artifacts']:
        exact(artifact, 'path sha256 semantic_sha256')
        if digest(read_bytes(inside(root, artifact['path']))) != artifact['sha256']:
            raise ValueError('artifact changed; approval invalidated')
    if state['stage'] == 'formal':
        for price in evidence['price_evidence']:
            if price['disposition'] != 'reviewed':
                raise ValueError('formal price/assumption requires estimator disposition')
            text(price['reviewer'])
            if price['source_type'] == 'assumption' and any(
                    not line['allowance'] for line in evidence['lines'] if line['price_ref'] == price['id']):
                raise ValueError('formal assumptions must remain visible allowances')
    if state['status'] in ('approved_for_final', 'final_verified'):
        if state['domain'] == 'sub-pay-app':
            raise ValueError('billing review adapter unavailable; needs_human: independently recomputed '
                             'prior_period, retainage, sov, totals checks bound to project/revision and '
                             'artifact semantic_sha256 required; supplied hashes/approvals cannot certify them')
        if state['domain'] != 'estimate':
            raise ValueError('domain-specific legal/safety/billing review adapter unavailable; needs_human')
        if state['exceptions'] or set(valid) != {'scope', 'pricing', 'estimate_final'}:
            raise ValueError('scope/pricing approvals and resolved exceptions required')
        if any(state['phases'][p]['status'] != 'complete' for p in PHASES[:3]):
            raise ValueError('incomplete financial phases')
        if state['status'] == 'final_verified':
            raise ValueError('visual/domain verification adapter unavailable; cannot certify final_verified')
    return {'status': 'validated', 'next_safe_action': next_action, 'valid_approvals': valid,
            'issuance': 'not_issued', 'limitations': ['not authentication', 'not market accuracy']}
