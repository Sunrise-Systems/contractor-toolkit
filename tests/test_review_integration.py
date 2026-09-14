"""Regression checks for independently reviewed integration boundaries."""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'scripts'))


class ReviewIntegrationTests(unittest.TestCase):
    def test_ci_actions_use_immutable_release_pins(self):
        workflow = (REPO / '.github/workflows/validate.yml').read_text()
        for action in ('checkout', 'setup-python'):
            self.assertRegex(workflow, rf'actions/{action}@[0-9a-f]{{40}}\s+# v\d+\.\d+\.\d+')

    def test_packaged_guard_imports_without_repository(self):
        from package_layout import package_inputs
        policy = json.loads((REPO / 'scripts/toolkit-policy.json').read_text())
        inputs = package_inputs(REPO, 'plugins/contractor-initialize/skills/update-brand', policy)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, source in inputs.items():
                dest = root / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(source.read_bytes())
            result = subprocess.run([sys.executable, str(root / 'scripts/toolkit_guard.py'), '--help'],
                                    cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_workflow_source_symlink_swap_after_path_validation_rejected(self):
        import workflow_checks
        from test_workflow_checks import WorkflowTests
        fixture = WorkflowTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        state, evidence = fixture.fixture()
        original = workflow_checks.inside
        def swapped(root, relative):
            path = original(root, relative)
            private = fixture.base / 'private.txt'
            private.write_bytes(path.read_bytes())
            path.unlink()
            path.symlink_to(private)
            return path
        with patch.object(workflow_checks, 'inside', side_effect=swapped):
            with self.assertRaises((ValueError, OSError)):
                workflow_checks.check_workflow(state, evidence)

    def test_artifact_identical_inode_replacement_during_parse_rejected(self):
        import artifact_checks
        fields = {'project_id': 'P', 'company': 'Synthetic', 'revision': 'R1'}
        expected = dict(schema_version=1, approved_fields=fields, required_text=[], print_css='@media print {}')
        raw = '<html><head><style>@media print {}</style></head><body>' + ''.join(
            f'<p data-field="{k}">{v}</p>' for k, v in fields.items()) + '</body></html>'
        with tempfile.TemporaryDirectory() as directory:
            artifact = Path(directory) / 'draft.html'
            artifact.write_text(raw)
            original = artifact_checks._html
            def swapped(*args):
                replacement = artifact.with_name('replacement.html')
                replacement.write_text(raw)
                replacement.replace(artifact)
                return original(*args)
            with patch.object(artifact_checks, '_html', side_effect=swapped):
                with self.assertRaisesRegex(ValueError, 'identity|changed'):
                    artifact_checks.verify_artifact(artifact, expected)
