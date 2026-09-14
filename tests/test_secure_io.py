"""Real filesystem regressions; syscall patches schedule deterministic races."""
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from guard_common import load_json
from test_toolkit_guard import GuardFixture


class ChangeIOTests(GuardFixture, unittest.TestCase):
    def test_absent_target_swapped_to_dangling_symlink_is_not_absent(self):
        from change_checks import check_change
        self.target.unlink()
        target = self.plan['targets'][0]
        from guard_common import digest
        after = '{"brand":"new"}'
        target.update(before=None, before_sha256=None, after=after, after_sha256=digest(after.encode()),
                      contexts=[{'before': '', 'after': after, 'count': 1}])
        self.approve()
        original = os.access
        def swap(*args, **kwargs):
            self.target.symlink_to(self.base / 'missing')
            return original(*args, **kwargs)
        with patch('os.access', side_effect=swap):
            with self.assertRaises((ValueError, OSError)):
                check_change(self.plan)

    def test_snapshot_rejects_same_bytes_target_replacement(self):
        from change_checks import snapshot
        import shutil
        original = shutil.disk_usage
        def swap(path):
            replacement = self.base / 'replacement'
            replacement.write_bytes(self.target.read_bytes())
            replacement.replace(self.target)
            return original(path)
        with patch('shutil.disk_usage', side_effect=swap):
            with self.assertRaisesRegex(ValueError, 'changed'):
                snapshot(self.plan, self.base / 'checkpoint')

    def test_snapshot_backup_swap_never_chmods_outside(self):
        from change_checks import snapshot
        from contextlib import contextmanager
        checkpoint = self.base / 'checkpoint'
        outside = self.base / 'outside'
        outside.write_text('private')
        outside.chmod(0o600)
        original = Path.open
        @contextmanager
        def swapped(path, *args, **kwargs):
            with original(path, *args, **kwargs) as stream:
                yield stream
            if path.name == '0.before':
                path.unlink()
                path.symlink_to(outside)
        with patch.object(Path, 'open', swapped):
            try:
                snapshot(self.plan, checkpoint)
            except (ValueError, OSError):
                pass
        self.assertEqual(outside.stat().st_mode & 0o777, 0o600)

    def test_snapshot_rejects_regular_parent_swap(self):
        from change_checks import snapshot
        import shutil
        parent = self.base / 'backups'
        parent.mkdir()
        original = shutil.disk_usage
        def swap(path):
            result = original(path)
            parent.rename(self.base / 'moved')
            parent.mkdir()
            return result
        with patch('shutil.disk_usage', side_effect=swap):
            with self.assertRaisesRegex(ValueError, 'changed'):
                snapshot(self.plan, parent / 'checkpoint')
        self.assertEqual(list(parent.iterdir()), [])

    def test_snapshot_parent_swap_cannot_write_outside(self):
        from change_checks import snapshot
        import shutil
        parent = self.base / 'backups'
        outside = self.base / 'outside'
        parent.mkdir()
        outside.mkdir()
        original = shutil.disk_usage
        def swap(path):
            result = original(path)
            parent.rename(self.base / 'moved')
            parent.symlink_to(outside, target_is_directory=True)
            return result
        with patch('shutil.disk_usage', side_effect=swap):
            with self.assertRaises((ValueError, OSError)):
                snapshot(self.plan, parent / 'checkpoint')
        self.assertEqual(list(outside.iterdir()), [])

    def test_change_target_hardlink_rejected(self):
        from change_checks import check_change
        os.link(self.target, self.base / 'alias')
        with self.assertRaisesRegex(ValueError, 'single.link|hardlink'):
            check_change(self.plan)


class SecureIOTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.file = self.root / 'input.json'
        self.file.write_text('{"ok":true}')

    def test_generate_cannot_mkdir_through_symlink(self):
        from build_dist import generate
        output = self.root / 'output'
        (output / 'skills').mkdir(parents=True)
        outside = self.root / 'outside'
        outside.mkdir()
        (output / 'skills/sample').symlink_to(outside, target_is_directory=True)
        checked = {'packages': {'synthetic': 'sample'}, 'policy': {}}
        with patch('build_dist.package_inputs', return_value={'references/new/data': self.file}):
            with self.assertRaises((ValueError, OSError)):
                generate(self.root, output, 'template-preview', checked)
        self.assertEqual(list(outside.iterdir()), [])

    def test_generate_archive_does_not_overwrite_symlink_target(self):
        from build_dist import generate
        output = self.root / 'output'
        (output / 'zips').mkdir(parents=True)
        outside = self.root / 'outside'
        outside.write_bytes(b'private')
        (output / 'zips/sample.zip').symlink_to(outside)
        checked = {'packages': {'synthetic': 'sample'}, 'policy': {
            'companions': {'synthetic': []}, 'covered_skills': [], 'logo': {}}}
        with patch('build_dist.package_inputs', return_value={'asset.bin': self.file}):
            with self.assertRaises((ValueError, OSError)):
                generate(self.root, output, 'release', checked)
        self.assertEqual(outside.read_bytes(), b'private')

    def test_generate_manifest_does_not_overwrite_symlink_target(self):
        from build_dist import generate
        output = self.root / 'output'
        folder = output / 'skills/sample'
        folder.mkdir(parents=True)
        outside = self.root / 'outside'
        outside.write_bytes(b'private')
        (folder / 'package-manifest.json').symlink_to(outside)
        checked = {'packages': {'synthetic': 'sample'}, 'policy': {
            'companions': {'synthetic': []}, 'covered_skills': [], 'logo': {}}}
        with patch('build_dist.package_inputs', return_value={'asset.bin': self.file}):
            with self.assertRaises((ValueError, OSError)):
                generate(self.root, output, 'template-preview', checked)
        self.assertEqual(outside.read_bytes(), b'private')

    def test_package_inventory_rejects_hardlinked_binary(self):
        from package_layout import package_inputs
        folder = self.root / 'synthetic'
        folder.mkdir()
        os.link(self.file, folder / 'asset.bin')
        with self.assertRaisesRegex(ValueError, 'single.link|hardlink'):
            package_inputs(self.root, 'synthetic', {'copies': {}, 'covered_skills': []})

    def test_generate_rejects_hardlinked_binary_input(self):
        from build_dist import generate
        os.link(self.file, self.root / 'alias')
        checked = {'packages': {'synthetic': 'sample'}, 'policy': {
            'companions': {'synthetic': []}, 'covered_skills': [], 'logo': {}}}
        with patch('build_dist.package_inputs', return_value={'asset.bin': self.file}):
            with self.assertRaisesRegex(ValueError, 'single.link|hardlink'):
                generate(self.root, self.root / 'output', 'template-preview', checked)
        self.assertFalse((self.root / 'output/skills/sample/asset.bin').exists())

    def test_receipt_readback_rejects_same_content_new_inode(self):
        import toolkit_guard
        original = toolkit_guard.write_bytes
        dest = self.root / 'receipt.json'
        def swap(path, content):
            original(path, content)
            replacement = self.root / 'replacement'
            replacement.write_bytes(content)
            replacement.replace(path)
        with patch('artifact_checks.verify_artifact', return_value={'status': 'verified'}), \
                patch('toolkit_guard.write_bytes', side_effect=swap):
            result = toolkit_guard.main(['verify-artifact', '--artifact', str(self.file),
                '--expectations', str(self.file), '--receipt', str(dest)])
        self.assertEqual(result, 1, 'receipt readback accepted a different inode')

    def test_receipt_rejects_regular_parent_replacement(self):
        import toolkit_guard
        folder = self.root / 'receipts'
        folder.mkdir()
        def verify(*args):
            folder.rename(self.root / 'moved')
            folder.mkdir()
            return {'status': 'verified'}
        with patch('artifact_checks.verify_artifact', side_effect=verify):
            result = toolkit_guard.main(['verify-artifact', '--artifact', str(self.file),
                '--expectations', str(self.file), '--receipt', str(folder / 'receipt.json')])
        self.assertEqual(result, 1, 'silently used a different directory inode')
        self.assertFalse((folder / 'receipt.json').exists())

    def test_receipt_rejects_parent_swap_after_validation(self):
        import toolkit_guard
        folder, outside = self.root / 'receipts', self.root / 'outside'
        folder.mkdir()
        outside.mkdir()
        def verify(*args):
            folder.rename(self.root / 'moved')
            folder.symlink_to(outside, target_is_directory=True)
            return {'status': 'verified'}
        with patch('artifact_checks.verify_artifact', side_effect=verify):
            result = toolkit_guard.main(['verify-artifact', '--artifact', str(self.file),
                '--expectations', str(self.file), '--receipt', str(folder / 'receipt.json')])
        self.assertEqual(result, 1, 'receipt followed swapped parent')
        self.assertFalse((outside / 'receipt.json').exists())

    def test_json_rejects_ancestor_swap_after_open(self):
        folder = self.root / 'folder'
        folder.mkdir()
        self.file.rename(folder / self.file.name)
        original = os.open
        def swapped(path, flags, *args, **kwargs):
            fd = original(path, flags, *args, **kwargs)
            if Path(path).name == 'folder':
                folder.rename(self.root / 'moved')
                folder.mkdir()
                (folder / self.file.name).write_text('{"ok":true}')
            return fd
        with patch('os.open', side_effect=swapped):
            with self.assertRaisesRegex(ValueError, 'changed'):
                load_json(folder / self.file.name)

    def test_json_rejects_mutation_during_read(self):
        from contextlib import contextmanager
        original = os.fdopen
        @contextmanager
        def changed(*args, **kwargs):
            with original(*args, **kwargs) as stream:
                yield stream
                self.file.write_text('{"ok":false}')
        with patch('os.fdopen', changed):
            with self.assertRaisesRegex(ValueError, 'changed'):
                load_json(self.file)

    def test_json_rejects_same_content_inode_swap_at_open(self):
        replacement = self.root / 'replacement'
        replacement.write_bytes(self.file.read_bytes())
        original = os.open
        def swapped(path, flags, *args, **kwargs):
            if Path(path).name == self.file.name:
                replacement.replace(self.file)
            return original(path, flags, *args, **kwargs)
        with patch('os.open', side_effect=swapped):
            with self.assertRaisesRegex(ValueError, 'changed'):
                load_json(self.file)

    def test_json_rejects_symlink_ancestor(self):
        alias = self.root / 'alias'
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises((ValueError, OSError)):
            load_json(alias / self.file.name)

    def test_json_rejects_hardlink(self):
        os.link(self.file, self.root / 'alias')
        with self.assertRaisesRegex(ValueError, 'hardlink|single.link'):
            load_json(self.file)
