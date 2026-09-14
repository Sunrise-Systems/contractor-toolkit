"""Versioned section labels: new behavior and explicit legacy regressions."""
import sys
from pathlib import Path

import pytest
from jsonschema import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from change_checks import check_change
from guard_common import digest, version


def approve(plan):
    plan['approval'] = {'reviewer': 'Human fixture', 'purpose': 'local_update',
                        'digest': digest({k: v for k, v in plan.items() if k != 'approval'})}
    return plan


def plan_for(tmp_path):
    before = '{"company_name": "Old", "license": "Keep"}'
    after = before.replace('Old', 'New')
    (tmp_path / 'company.json').write_text(before)
    return approve({'schema_version': 2, 'kind': 'change_plan', 'operation_id': 'sections',
                    'root': str(tmp_path), 'selected_sections': ['Company identity'],
                    'targets': [{'path': 'company.json', 'format': 'json',
                                 'section': 'Company identity', 'before': before, 'after': after,
                                 'before_sha256': digest(before.encode()),
                                 'after_sha256': digest(after.encode()),
                                 'selected_fields': ['company_name'],
                                 'contexts': [{'before': 'Old', 'after': 'New', 'count': 1}]}],
                    'approval': None})


@pytest.mark.parametrize('section', ['Licensing', ' Company identity', '   '])
def test_v2_unselected_section_rejected(tmp_path, section):
    plan = plan_for(tmp_path)
    plan['targets'][0]['section'] = section
    with pytest.raises(ValueError, match='unselected section|nonempty string'):
        check_change(approve(plan))


def test_v2_human_label_differs_from_field_key(tmp_path):
    plan = plan_for(tmp_path)
    assert check_change(plan)['status'] == 'validated'
    assert (tmp_path / 'company.json').read_text() == plan['targets'][0]['before']


# Regression/contract coverage below: existing checks, not claimed RED cycles.
def test_v2_missing_section_rejected_by_schema(tmp_path):
    plan = plan_for(tmp_path)
    del plan['targets'][0]['section']
    with pytest.raises(ValidationError):
        check_change(approve(plan))


@pytest.mark.parametrize('fields', [['license'], ['Company identity'], ['company_name.child']])
def test_v2_field_selection_is_exact_not_a_label_or_nested_selector(tmp_path, fields):
    plan = plan_for(tmp_path)
    plan['targets'][0]['selected_fields'] = fields
    with pytest.raises(ValueError, match='unrequested fields changed'):
        check_change(approve(plan))


def test_v2_unselected_field_change_rejected(tmp_path):
    plan = plan_for(tmp_path)
    target = plan['targets'][0]
    target['after'] = target['after'].replace('Keep', 'Changed')
    target['after_sha256'] = digest(target['after'].encode())
    target['contexts'].append({'before': 'Keep', 'after': 'Changed', 'count': 1})
    with pytest.raises(ValueError, match='unrequested fields changed'):
        check_change(approve(plan))


@pytest.mark.parametrize('mutation', ['section', 'selected_sections', 'selected_fields', 'version'])
def test_stale_approval_binds_section_fields_and_version(tmp_path, mutation):
    plan = plan_for(tmp_path)
    plan['selected_sections'].append('Legal identity')
    approve(plan)
    if mutation == 'section':
        plan['targets'][0]['section'] = 'Legal identity'
    elif mutation == 'selected_sections':
        plan['selected_sections'].append('Licensing')
    elif mutation == 'selected_fields':
        plan['targets'][0]['selected_fields'].append('license')
    else:
        plan['schema_version'] = 1
        plan['selected_sections'] = ['company_name']
        del plan['targets'][0]['section']
    with pytest.raises(ValueError, match='approval digest/purpose stale'):
        check_change(plan)


def test_stale_before_image_still_rejected(tmp_path):
    plan = plan_for(tmp_path)
    (tmp_path / 'company.json').write_text('{}')
    with pytest.raises(ValueError, match='stale before image'):
        check_change(plan)


def test_legacy_v1_field_key_allowlist_unchanged(tmp_path):
    plan = plan_for(tmp_path)
    plan['schema_version'] = 1
    del plan['targets'][0]['section']
    plan['selected_sections'] = ['company_name']
    assert check_change(approve(plan))['status'] == 'validated'
    plan['selected_sections'] = ['Company identity']
    with pytest.raises(ValueError, match='unselected section'):
        check_change(approve(plan))


def test_v1_cannot_accept_v2_binding(tmp_path):
    plan = plan_for(tmp_path)
    plan['schema_version'] = 1
    plan['selected_sections'] = ['company_name']
    with pytest.raises(ValidationError):
        check_change(approve(plan))


@pytest.mark.parametrize('kind', ['workflow_state', 'pricing_evidence', 'receipt'])
def test_other_contract_kinds_remain_v1(kind):
    with pytest.raises(ValueError, match='unsupported schema version'):
        version({'kind': kind, 'schema_version': 2}, kind)
    from guard_common import load_json
    schema = load_json(Path(__file__).resolve().parents[1] / 'references/workflow-contract.schema.json')
    assert schema['$defs'][kind]['properties']['schema_version'] == {'type': 'integer', 'const': 1}


@pytest.mark.parametrize('bad_version', [True, 2.0, 3])
def test_invalid_change_versions_rejected(tmp_path, bad_version):
    plan = plan_for(tmp_path)
    plan['schema_version'] = bad_version
    with pytest.raises((ValueError, ValidationError)):
        check_change(approve(plan))


@pytest.mark.parametrize('kind,before', [('markdown', '---\nname: Keep\n---\nOld'),
                                        ('text', 'Old'), ('yaml', 'company_name: Old\nlicense: Keep')])
def test_v2_body_and_yaml_fields_keep_exact_selection(tmp_path, kind, before):
    plan = plan_for(tmp_path)
    target = plan['targets'][0]
    target.update(format=kind, before=before, after=before.replace('Old', 'New'),
                  selected_fields=['company_name' if kind == 'yaml' else '__body__'])
    target['before_sha256'] = digest(before.encode())
    target['after_sha256'] = digest(target['after'].encode())
    (tmp_path / 'company.json').write_text(before)
    assert check_change(approve(plan))['status'] == 'validated'
    target['selected_fields'] = ['Company identity']
    with pytest.raises(ValueError, match='unrequested fields changed'):
        check_change(approve(plan))
