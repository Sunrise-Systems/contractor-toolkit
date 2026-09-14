"""Synthetic temporary-only guard integration tests."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))


def digest(value):
    raw = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


class GuardFixture:
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'project'
        self.root.mkdir()
        self.target = self.root / 'config.json'
        self.target.write_text('{"brand":"old","keep":"old"}')
        before = self.target.read_text()
        after = before.replace('"brand":"old"', '"brand":"new"')
        self.plan = dict(schema_version=1, kind='change_plan', operation_id='test', root=str(self.root),
                         selected_sections=['brand'], targets=[dict(path='config.json', format='json',
                         before=before, after=after, before_sha256=digest(before.encode()),
                         after_sha256=digest(after.encode()), selected_fields=['brand'],
                         contexts=[dict(before='"brand":"old"', after='"brand":"new"', count=1)])],
                         approval=None)
        self.approve()

    def approve(self):
        self.plan['approval'] = dict(reviewer='Test human', purpose='local_update',
                                    digest=digest({k: v for k, v in self.plan.items() if k != 'approval'}))

    def cli(self, command, **args):
        paths = {}
        for key, value in args.items():
            if isinstance(value, dict):
                p = self.base / (key + '.json')
                p.write_text(json.dumps(value))
                paths[key] = str(p)
            else:
                paths[key] = str(value)
        return subprocess.run([sys.executable, str(REPO / 'scripts/toolkit_guard.py'), command,
                               *[x for k, v in paths.items() for x in ('--' + k.replace('_', '-'), v)]],
                              capture_output=True, text=True)


class GuardTests(GuardFixture, unittest.TestCase):
    def test_approved_exact_change_check_is_read_only(self):
        old = self.target.read_bytes()
        result = self.cli('check-change', plan=self.plan, root=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['status'], 'validated')
        self.assertEqual(self.target.read_bytes(), old)

    def test_artifact_cli_exclusive_receipt(self):
        fields = {'project_id':'P', 'company':'Synthetic', 'revision':'1'}
        artifact = self.root / 'draft.html'
        artifact.write_text('<html><head><style>@media print {}</style></head><body>' +
                            ''.join(f'<p data-field="{k}">{v}</p>' for k,v in fields.items()) + '</body></html>')
        expected = dict(schema_version=1, approved_fields=fields, required_text=[], print_css='@media print {}')
        receipt = self.base / 'receipt.json'
        result = self.cli('verify-artifact', artifact=artifact, expectations=expected, receipt=receipt)
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = receipt.read_bytes()
        self.assertEqual(json.loads(saved)['file_sha256'], digest(artifact.read_bytes()))
        self.assertNotEqual(self.cli('verify-artifact', artifact=artifact, expectations=expected, receipt=receipt).returncode, 0)
        self.assertEqual(saved, receipt.read_bytes())
        link = self.base / 'link.json'
        link.symlink_to(receipt)
        self.assertNotEqual(self.cli('verify-artifact', artifact=artifact, expectations=expected, receipt=link).returncode, 0)

    def test_schema_and_adversarial_change_inputs(self):
        import copy
        from jsonschema import Draft202012Validator
        self.assertTrue((REPO / 'references/workflow-contract.schema.json').is_file(), 'versioned schema missing')
        schema = json.loads((REPO / 'references/workflow-contract.schema.json').read_text())
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(self.plan)
        for mutate in (lambda p: p.update(unknown=True), lambda p: p.update(schema_version=True),
                       lambda p: p.update(approval=None),
                       lambda p: p['targets'][0].update(path='../escape'),
                       lambda p: p['targets'][0].update(selected_fields=['keep'])):
            bad = copy.deepcopy(self.plan)
            mutate(bad)
            self.assertNotEqual(self.cli('check-change', plan=bad, root=self.root).returncode, 0)
        self.target.chmod(0o400)
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_unrequested_boolean_to_integer_change_is_not_equal(self):
        target = self.plan['targets'][0]
        before, after = '{"brand":"old","keep":true}', '{"brand":"new","keep":1}'
        self.target.write_text(before)
        target.update(before=before, after=after, before_sha256=digest(before.encode()), after_sha256=digest(after.encode()),
                      contexts=[dict(before=before, after=after, count=1)])
        self.approve()
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_absent_target_checkpoint_never_creates_target(self):
        self.target.unlink()
        target = self.plan['targets'][0]
        after = '{"brand":"new"}'
        target.update(before=None, before_sha256=None, after=after, after_sha256=digest(after.encode()),
                      contexts=[dict(before='', after=after, count=1)])
        self.approve()
        checkpoint = self.base / 'absent-checkpoint'
        self.assertEqual(self.cli('snapshot', plan=self.plan, checkpoint_dir=checkpoint).returncode, 0)
        self.assertFalse(self.target.exists())
        manifest = json.loads((checkpoint / 'manifest.json').read_text())
        self.assertIsNone(manifest['records'][0]['backup'])
        result = self.cli('verify-change', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertEqual(json.loads(result.stdout)['targets']['config.json'], 'before')

    def test_nonfinite_selected_config_value_blocks(self):
        target = self.plan['targets'][0]
        after = '{"brand":NaN,"keep":"old"}'
        target.update(after=after, after_sha256=digest(after.encode()),
                      contexts=[dict(before='"brand":"old"', after='"brand":NaN', count=1)])
        self.approve()
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_stale_digest_and_symlink_boundaries(self):
        self.plan['operation_id'] = 'changed'
        self.assertNotEqual(self.cli('snapshot', plan=self.plan, checkpoint_dir=self.base / 'stale').returncode, 0)
        self.assertFalse((self.base / 'stale').exists())
        self.approve()
        self.target.write_text('changed concurrently')
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)
        self.target.unlink()
        outside = self.base / 'outside.json'
        outside.write_text(self.plan['targets'][0]['before'])
        self.target.symlink_to(outside)
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_markdown_frontmatter_update_preserves_unselected_body(self):
        target = self.plan['targets'][0]
        before = '---\nbrand: old\nkeep: old\n---\n# Notes\nKeep this prose exactly.\n'
        after = before.replace('brand: old', 'brand: new')
        self.target.write_text(before)
        target.update(format='markdown', before=before, after=after,
                      before_sha256=digest(before.encode()), after_sha256=digest(after.encode()),
                      contexts=[dict(before='brand: old', after='brand: new', count=1)])
        self.approve()
        result = self.cli('check-change', plan=self.plan, root=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        target['after'] += 'Unapproved new prose'
        target['after_sha256'] = digest(target['after'].encode())
        target['contexts'] = [dict(before=before, after=target['after'], count=1)]
        self.approve()
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_plain_reference_exact_patch_and_receipt_hashes(self):
        before, after = 'Brand color: old\nUnrelated: old\n', 'Brand color: new\nUnrelated: old\n'
        self.target.write_text(before)
        target = self.plan['targets'][0]
        self.plan['selected_sections'] = ['__body__']
        target.update(format='text', selected_fields=['__body__'], before=before, after=after,
                      before_sha256=digest(before.encode()), after_sha256=digest(after.encode()),
                      contexts=[dict(before='Brand color: old', after='Brand color: new', count=1)])
        self.approve()
        checkpoint = self.base / 'text-checkpoint'
        result = self.cli('snapshot', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.target.read_text(), before)
        self.target.write_text(after)
        result = self.cli('verify-change', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertEqual(result.returncode, 0, result.stderr)
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt['file_hashes']['config.json'], digest(after.encode()))
        self.assertEqual(receipt['plan_digest'], self.plan['approval']['digest'])

    def test_partial_template_update_preserves_but_never_introduces_tokens(self):
        before, after = 'Brand: old\nCompany: {{COMPANY_NAME}}\n', 'Brand: new\nCompany: {{COMPANY_NAME}}\n'
        self.target.write_text(before)
        target = self.plan['targets'][0]
        self.plan['selected_sections'] = ['__body__']
        target.update(format='text', selected_fields=['__body__'], before=before, after=after,
                      before_sha256=digest(before.encode()), after_sha256=digest(after.encode()),
                      contexts=[dict(before='Brand: old', after='Brand: new', count=1)])
        self.approve()
        result = self.cli('check-change', plan=self.plan, root=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        after += '{{NEW_TOKEN}}'
        target.update(after=after, after_sha256=digest(after.encode()), contexts=[dict(before=before, after=after, count=1)])
        self.approve()
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_yaml_exact_images_and_duplicate_keys(self):
        target = self.plan['targets'][0]
        before, after = 'brand: old\nkeep: old\n', 'brand: new\nkeep: old\n'
        self.target.write_text(before)
        target.update(format='yaml', before=before, after=after,
                      before_sha256=digest(before.encode()), after_sha256=digest(after.encode()),
                      contexts=[dict(before='brand: old', after='brand: new', count=1)])
        self.approve()
        result = self.cli('check-change', plan=self.plan, root=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        duplicate = after + 'brand: duplicate\n'
        target.update(after=duplicate, after_sha256=digest(duplicate.encode()),
                      contexts=[dict(before=before, after=duplicate, count=1)])
        self.approve()
        self.assertNotEqual(self.cli('check-change', plan=self.plan, root=self.root).returncode, 0)

    def test_snapshot_and_interrupted_readback(self):
        checkpoint = self.base / 'checkpoint'
        result = self.cli('snapshot', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((checkpoint / '0.before').read_bytes(), self.target.read_bytes())
        self.assertNotEqual(self.cli('snapshot', plan=self.plan, checkpoint_dir=checkpoint).returncode, 0)
        result = self.cli('verify-change', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertEqual(json.loads(result.stdout)['targets']['config.json'], 'before')
        self.target.write_text(self.plan['targets'][0]['after'])
        result = self.cli('verify-change', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertEqual(json.loads(result.stdout)['status'], 'verified')
        self.target.write_text('concurrent edit')
        result = self.cli('verify-change', plan=self.plan, checkpoint_dir=checkpoint)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)['targets']['config.json'], 'conflict')
        (checkpoint / '0.before').unlink()
        self.assertNotEqual(self.cli('verify-change', plan=self.plan, checkpoint_dir=checkpoint).returncode, 0)


if __name__ == '__main__':
    unittest.main()
