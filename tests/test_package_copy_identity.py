"""Package copy identity across inventory and materialization."""
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


class PackageCopyIdentityTests(unittest.TestCase):
    def test_generate_rejects_same_content_replacement_after_inventory(self):
        import build_dist
        from package_layout import package_inputs
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'synthetic/asset.bin'
            source.parent.mkdir()
            source.write_bytes(b'synthetic public resource')
            checked = {'packages': {'synthetic': 'sample'}, 'policy': {
                'copies': {}, 'covered_skills': [],
                'companions': {'synthetic': []}, 'logo': {}}}
            def swapped(*args):
                result = package_inputs(*args)
                replacement = root / 'replacement'
                replacement.write_bytes(source.read_bytes())
                replacement.replace(source)
                return result
            with patch('build_dist.package_inputs', side_effect=swapped):
                with self.assertRaisesRegex(ValueError, 'identity/content changed'):
                    build_dist.generate(root, root / 'output', 'template-preview', checked)
            self.assertFalse((root / 'output/skills/sample/asset.bin').exists())
