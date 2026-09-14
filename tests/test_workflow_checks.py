"""Durable synthetic project fixtures, never client inputs."""
import json
from test_toolkit_guard import GuardFixture, digest
import unittest


class WorkflowTests(GuardFixture, unittest.TestCase):
    def scope_approval_digest(self, state):
        return digest({k: state[k] for k in ('project_id', 'revision', 'scope_digest', 'sources')})

    def test_reindexed_source_still_invalidates_old_approval(self):
        state, evidence = self.fixture()
        (self.root / 'drawing.txt').write_text('changed')
        state['sources'][0]['sha256'] = digest(b'changed')
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('approval', result.stderr)

    def fixture(self):
        (self.root / 'drawing.txt').write_text('synthetic drawing')
        source = dict(id='drawing', project_id='P', path='drawing.txt', sha256=digest(b'synthetic drawing'),
                      revision='1', date=None, locator='sheet 1', missing_reason='date unavailable')
        evidence = dict(schema_version=1, kind='pricing_evidence', project_id='P', revision='1',
                        quantity_evidence=[dict(id='Q', source_id='drawing', unit='ea', rating='B')],
                        price_evidence=[dict(id='R', source_id='drawing', unit='ea', currency='USD',
                        source_type='quote', market='synthetic', base_rate='0.10', locality='1', escalation='1',
                        adjustment_basis='none', confidence='reviewed', override=None, override_reason=None,
                        disposition='reviewed', reviewer='Estimator')],
                        lines=[dict(id='L', division='01', quantity='3', unit='ea', rate='0.10', amount='0.30',
                        currency='USD', quantity_ref='Q', price_ref='R', derivation='quantity * rate', allowance=False)],
                        division_totals={'01':'0.30'}, subtotal='0.30', markup_rate='0.10', markup_basis='subtotal',
                        fee='0.03', total='0.33', currency='USD', rounding='ROUND_HALF_UP', quantum='0.01')
        state = dict(schema_version=1, kind='workflow_state', root=str(self.root), workflow_id='W',
                     project_id='P', project_name='Synthetic', revision='1', stage='ROM', status='draft',
                     domain='estimate', issuance='not_issued', sources=[source], scope={'description':'synthetic'},
                     scope_digest=digest({'description':'synthetic'}), pricing_digest=digest(evidence),
                     phases={p: {'status': 'complete' if p in ('scope','takeoff') else 'pending', 'reason':None}
                             for p in ('scope','takeoff','pricing','artifact')}, approvals=[], artifacts=[],
                     exceptions=[], next_safe_action='pricing')
        state['approvals'] = [dict(reviewer='Estimator', purpose='scope', digest=self.scope_approval_digest(state))]
        return state, evidence

    def approve_pricing_and_final(self, state):
        state['phases']['pricing']['status'] = 'complete'
        state['next_safe_action'] = 'artifact'
        bound = {k: state[k] for k in ('project_id', 'revision', 'scope_digest', 'sources', 'pricing_digest')}
        state['approvals'].append(dict(reviewer='Estimator', purpose='pricing', digest=digest(bound)))
        state['approvals'].append(dict(reviewer='Estimator', purpose='estimate_final',
                                      digest=digest({k: v for k, v in state.items()
                                                     if k not in ('approvals', 'status')})))

    def test_wrong_project_evidence_rejected_even_with_fresh_digest(self):
        state, evidence = self.fixture()
        evidence['project_id'] = 'OTHER'
        state['pricing_digest'] = digest(evidence)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('wrong project/revision evidence', result.stderr)

    def test_wrong_project_source_rejected_even_with_fresh_approval(self):
        state, evidence = self.fixture()
        state['sources'][0]['project_id'] = 'OTHER'
        state['approvals'][0]['digest'] = self.scope_approval_digest(state)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('wrong-project source', result.stderr)

    def test_changed_approved_amount_invalidates_old_pricing_approval(self):
        state, evidence = self.fixture()
        state['status'] = 'approved_for_final'
        self.approve_pricing_and_final(state)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertEqual(result.returncode, 0, result.stderr)
        # Internally consistent new pricing, not an arithmetic-error rejection.
        evidence['lines'][0].update(quantity='4', amount='0.40')
        evidence.update(division_totals={'01': '0.40'}, subtotal='0.40', fee='0.04', total='0.44')
        state['pricing_digest'] = digest(evidence)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('approval', result.stderr)
        self.assertNotIn('total mismatch', result.stderr)
        # Reapproval, rather than reverting the amount, restores estimate eligibility.
        state['approvals'] = state['approvals'][:1]
        self.approve_pricing_and_final(state)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_nonestimate_cannot_reuse_complete_estimator_approvals(self):
        for domain in ('contract', 'incident-report', 'sub-pay-app'):
            for status in ('approved_for_final', 'final_verified'):
                with self.subTest(domain=domain, status=status):
                    state, evidence = self.fixture()
                    state.update(domain=domain, status=status)
                    self.approve_pricing_and_final(state)
                    result = self.cli('check-workflow', state=state, evidence=evidence)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('adapter unavailable', result.stderr)
                    self.assertEqual(json.loads(result.stderr)['issuance'], 'not_issued')

    def assert_pay_app_closed(self, field=None, value=None):
        # Synthetic artifact, NOT a supported pay-app evidence schema or receipt.
        payload = dict(project_id='P', revision='1', prior_certified='200.00',
                       prior_period='200.00', earned_to_date='500.00', retainage_rate='0.10',
                       retainage='50.00', sov_lines=['600.00', '400.00'], sov='1000.00',
                       contract_sum='1000.00', totals='250.00')
        if field:
            self.assertNotEqual(payload[field], value)
            payload[field] = value
        for status in ('approved_for_final', 'final_verified'):
            with self.subTest(check=field or 'consistent_control', status=status):
                state, evidence = self.fixture()
                state.update(domain='sub-pay-app', status=status)
                artifact = self.root / 'pay-app.json'
                artifact.write_text(json.dumps(payload))
                # Even current hashes and all estimator approvals cannot attest billing.
                state['artifacts'] = [dict(path=artifact.name, sha256=digest(artifact.read_bytes()),
                                           semantic_sha256=digest(payload))]
                self.approve_pricing_and_final(state)
                result = self.cli('check-workflow', state=state, evidence=evidence)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('adapter unavailable', result.stderr)
                self.assertIn(field or 'totals', result.stderr)
                self.assertIn('semantic_sha256', result.stderr)
                self.assertEqual(json.loads(result.stderr)['status'], 'needs_human')

    def test_pay_app_domain_change_invalidates_estimate_final_approval(self):
        state, evidence = self.fixture()
        state['status'] = 'approved_for_final'
        self.approve_pricing_and_final(state)
        self.assertEqual(self.cli('check-workflow', state=state, evidence=evidence).returncode, 0)
        state['domain'] = 'sub-pay-app'
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('approval digest/purpose stale', result.stderr)
        self.assertEqual(json.loads(result.stderr)['issuance'], 'not_issued')

    def test_pay_app_wrong_project_evidence_with_current_digest_blocks(self):
        state, evidence = self.fixture()
        state.update(domain='sub-pay-app', status='approved_for_final')
        evidence['project_id'] = 'OTHER'
        state['pricing_digest'] = digest(evidence)
        self.approve_pricing_and_final(state)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('wrong project/revision evidence', result.stderr)
        self.assertEqual(json.loads(result.stderr)['issuance'], 'not_issued')

    def test_pay_app_changed_amount_invalidates_pricing_approval(self):
        state, evidence = self.fixture()
        state.update(domain='sub-pay-app', status='approved_for_final')
        self.approve_pricing_and_final(state)
        evidence['lines'][0].update(quantity='4', amount='0.40')
        evidence.update(division_totals={'01': '0.40'}, subtotal='0.40', fee='0.04', total='0.44')
        state['pricing_digest'] = digest(evidence)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('approval digest/purpose stale', result.stderr)
        self.assertEqual(json.loads(result.stderr)['issuance'], 'not_issued')

    def test_pay_app_without_approvals_cannot_promote(self):
        for status in ('approved_for_final', 'final_verified'):
            with self.subTest(status=status):
                state, evidence = self.fixture()
                state.update(domain='sub-pay-app', status=status, approvals=[])
                result = self.cli('check-workflow', state=state, evidence=evidence)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('completed scope needs scope approval', result.stderr)
                self.assertEqual(json.loads(result.stderr)['issuance'], 'not_issued')

    def test_pay_app_prior_period_mismatch_cannot_finalize(self):
        self.assert_pay_app_closed('prior_period', '201.00')

    def test_pay_app_retainage_mismatch_cannot_finalize(self):
        self.assert_pay_app_closed('retainage', '49.00')

    def test_pay_app_sov_mismatch_cannot_finalize(self):
        self.assert_pay_app_closed('sov', '999.00')

    def test_pay_app_totals_mismatch_cannot_finalize(self):
        self.assert_pay_app_closed('totals', '251.00')

    def test_pay_app_consistent_control_still_requires_unavailable_adapter(self):
        self.assert_pay_app_closed()

    def test_decimal_and_separate_provenance_fail_closed(self):
        import copy
        state, evidence = self.fixture()
        cases = [('total', lambda e: e.update(total='0.34')),
                 ('quantity reference', lambda e: e['lines'][0].update(quantity_ref='R')),
                 ('price reference', lambda e: e['lines'][0].update(price_ref='Q')),
                 ('duplicate', lambda e: e['lines'].append(copy.deepcopy(e['lines'][0]))),
                 ('unit', lambda e: e['lines'][0].update(unit='sf')),
                 ('currency', lambda e: e['lines'][0].update(currency='EUR')),
                 ('nonfinite', lambda e: e['lines'][0].update(quantity='NaN')),
                 ('unknown field', lambda e: e['lines'][0].update(secret=True)),
                 ('version', lambda e: e.update(schema_version=True))]
        for name, mutate in cases:
            with self.subTest(name=name):
                changed = copy.deepcopy(evidence)
                mutate(changed)
                state['pricing_digest'] = digest(changed)
                result = self.cli('check-workflow', state=state, evidence=changed)
                self.assertNotEqual(result.returncode, 0, name)

    def test_unknown_nested_scope_and_missing_scope_approval_block(self):
        state, evidence = self.fixture()
        state['scope']['unknown'] = 'not supported'
        state['scope_digest'] = digest(state['scope'])
        state['approvals'][0]['digest'] = state['scope_digest']
        self.assertNotEqual(self.cli('check-workflow', state=state, evidence=evidence).returncode, 0)
        state, evidence = self.fixture()
        state['approvals'] = []
        self.assertNotEqual(self.cli('check-workflow', state=state, evidence=evidence).returncode, 0)

    def test_formal_allowance_approval_bound_to_exact_content(self):
        state, evidence = self.fixture()
        evidence['price_evidence'][0].update(source_type='assumption', source_id=None)
        evidence['lines'][0]['allowance'] = True
        state.update(stage='formal', status='approved_for_final', next_safe_action='artifact',
                     pricing_digest=digest(evidence))
        state['phases']['pricing']['status'] = 'complete'
        bound = {k:state[k] for k in ('project_id','revision','scope_digest','sources','pricing_digest')}
        state['approvals'].append(dict(reviewer='Estimator', purpose='pricing', digest=digest(bound)))
        state['approvals'].append(dict(reviewer='Estimator', purpose='estimate_final',
                                      digest=digest({k:v for k,v in state.items() if k not in ('approvals','status')})))
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertEqual(result.returncode, 0, result.stderr)
        state['project_name'] = 'different displayed project'
        self.assertNotEqual(self.cli('check-workflow', state=state, evidence=evidence).returncode, 0)

    def test_pay_app_finalization_names_unavailable_checks(self):
        state, evidence = self.fixture()
        state.update(domain='sub-pay-app', status='final_verified')
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        for check in ('prior_period', 'retainage', 'sov', 'totals', 'semantic_sha256'):
            self.assertIn(check, result.stderr)
        self.assertIn('unavailable', result.stderr)

    def test_consequential_status_cannot_bypass_review(self):
        for domain in ('estimate', 'contract', 'incident-report', 'sub-pay-app'):
            with self.subTest(domain=domain):
                state, evidence = self.fixture()
                state.update(status='final_verified', domain=domain)
                result = self.cli('check-workflow', state=state, evidence=evidence)
                self.assertNotEqual(result.returncode, 0)
        state, evidence = self.fixture()
        state['stage'] = 'formal'
        evidence['price_evidence'][0].update(source_type='assumption', source_id=None,
                                           disposition='pending', reviewer=None)
        state['pricing_digest'] = digest(evidence)
        self.assertNotEqual(self.cli('check-workflow', state=state, evidence=evidence).returncode, 0)

    def test_resume_before_pricing_requires_no_invented_rates(self):
        state, evidence = self.fixture()
        evidence.update(price_evidence=[], lines=[], division_totals={}, subtotal='0.00', fee='0.00', total='0.00')
        state['pricing_digest'] = digest(evidence)
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['next_safe_action'], 'pricing')
        state['phases']['pricing']['status'] = 'complete'
        state['next_safe_action'] = 'artifact'
        self.assertNotEqual(self.cli('check-workflow', state=state, evidence=evidence).returncode, 0)

    def test_resume_after_takeoff_preserves_scope_approval(self):
        state, evidence = self.fixture()
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = json.loads(result.stdout)
        self.assertEqual(result['next_safe_action'], 'pricing')
        self.assertEqual(result['valid_approvals'], ['scope'])
        (self.root / 'drawing.txt').write_text('revised drawing')
        result = self.cli('check-workflow', state=state, evidence=evidence)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('source', result.stderr)
