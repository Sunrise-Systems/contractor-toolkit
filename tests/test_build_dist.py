import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.tree = self.base / "source"
        shutil.copytree(ROOT, self.tree, ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))
        (self.tree / "dist").mkdir()
        (self.tree / "dist/README.md").write_text("Tracked documentation")
        self.out = self.base / "preview"

    def build(self, mode="template-preview", out=None):
        import os
        env = dict(os.environ, PYTHON=sys.executable)
        return subprocess.run(["bash", str(self.tree / "scripts/build-dist.sh"),
            "--mode", mode, "--output-dir", str(out or self.out)], env=env,
            capture_output=True, text=True)

    def test_same_content_source_swap_after_validation_is_rejected(self):
        import build_dist
        from unittest.mock import patch
        original = build_dist.generate
        source = self.tree / 'plugins/contractor-brand/skills/brand/SKILL.md'
        def swap(*args):
            replacement = self.base / 'replacement'
            replacement.write_bytes(source.read_bytes())
            replacement.replace(source)
            return original(*args)
        with patch('build_dist.generate', side_effect=swap):
            with self.assertRaisesRegex(ValueError, 'changed'):
                build_dist.build(self.tree, self.out, 'template-preview')
        self.assertFalse(self.out.exists())

    def test_source_hardlinks_are_rejected_before_packaging(self):
        import os
        source = self.tree / 'plugins/contractor-brand/skills/brand/SKILL.md'
        os.link(source, self.base / 'external-alias')
        result = self.build()
        self.assertNotEqual(result.returncode, 0, 'hardlinked source accepted')
        self.assertFalse(self.out.exists())

    def configure(self):
        registry = json.loads((self.tree / "scripts/template-tokens.json").read_text())
        for name, rows in registry.items():
            p = self.tree / name
            text = p.read_text()
            for row in rows:
                if row["kind"] == "required":
                    text = text.replace(row["line"], re.sub(r"\{\{[^{}]+\}\}", "Synthetic", row["line"]))
            p.write_text(text)
        p = self.tree / "scripts/toolkit-policy.json"
        data = json.loads(p.read_text())
        data["logo"] = {"mode": "no-logo", "files": [], "approval": {
            "reviewer": "Synthetic", "reason": "Text-only design", "digest": "0" * 64}}
        import hashlib
        brand = self.tree / "plugins/contractor-brand/skills/brand"
        data["logo"]["approval"]["digest"] = hashlib.sha256(json.dumps({f.relative_to(brand).as_posix():
            hashlib.sha256(f.read_bytes()).hexdigest() for f in brand.rglob("*") if f.is_file()},
            sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        p.write_text(json.dumps(data))

    def test_staging_preserves_previous_and_rejects_unsafe_destinations(self):
        import build_dist
        self.assertTrue(hasattr(build_dist, "verify_packages"), "package verifier missing")
        from build_dist import build
        from unittest.mock import patch
        self.configure()
        self.assertEqual(self.build("release").returncode, 0)
        before = {p.relative_to(self.out): p.read_bytes() for p in self.out.rglob("*") if p.is_file()}
        # Fail after generation, before promotion; prior output must remain identical.
        with patch("build_dist.verify_packages", side_effect=ValueError("injected parity failure")):
            with self.assertRaisesRegex(ValueError, "injected"):
                build(self.tree, self.out, "release")
        self.assertEqual(before, {p.relative_to(self.out): p.read_bytes() for p in self.out.rglob("*") if p.is_file()})
        for path in (self.tree, self.tree / "plugins/build", Path.home(), self.tree / "scripts"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                build(self.tree, path, "release")
        alias = self.base / "alias"
        alias.symlink_to(self.out, target_is_directory=True)
        with self.assertRaises(ValueError):
            build(self.tree, alias, "release")
        self.assertEqual(self.build("release", self.tree / "dist").returncode, 0)
        self.assertEqual((self.tree / "dist/README.md").read_text(), "Tracked documentation")

    def test_interrupted_promotion_restores_prior_release(self):
        from build_dist import promote
        from unittest.mock import patch
        stage = self.base / "stage"
        stage.mkdir()
        (stage / "build-report.json").write_text("new")
        self.out.mkdir()
        (self.out / "build-report.json").write_text("old")
        original = Path.rename
        def interrupted(path, destination):
            if path == stage:
                raise KeyboardInterrupt("simulated interruption")
            return original(path, destination)
        with patch.object(Path, "rename", interrupted), self.assertRaises(KeyboardInterrupt):
            promote(stage, self.out)
        self.assertEqual((self.out / "build-report.json").read_text(), "old")
        self.assertTrue(stage.exists())

    def test_release_logo_assets_cannot_be_arbitrary_repository_files(self):
        from toolkit_validation import validate
        self.configure()
        p = self.tree / 'scripts/toolkit-policy.json'
        policy = json.loads(p.read_text())
        policy['logo'] = {'mode':'assets', 'files':['README.md'], 'approval':None}
        p.write_text(json.dumps(policy))
        with self.assertRaisesRegex(ValueError, 'logo'):
            validate(self.tree, 'release')
        # Synthetic supported image fixture, not a company/client asset.
        from PIL import Image
        logo = self.tree / 'plugins/contractor-brand/skills/brand/assets/logos/primary.png'
        Image.new('RGB', (1, 1), 'white').save(logo)
        skill = self.tree / 'plugins/contractor-brand/skills/brand/SKILL.md'
        skill.write_text(skill.read_text() + '\nConfigured logo: `primary.png`\n')
        policy['logo']['files'] = [logo.relative_to(self.tree).as_posix()]
        p.write_text(json.dumps(policy))
        self.assertEqual(len(validate(self.tree, 'release')['packages']), 38)
        logo.write_text('not an image')
        with self.assertRaises(ValueError):
            validate(self.tree, 'release')

    def test_packaged_dependency_closure(self):
        self.configure()
        result = self.build('release')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.out / 'skills/estimating-workflow/references/brand-system.md').is_file(),
                        'copied templates require local brand-system.md')
        from toolkit_validation import validate
        from build_dist import verify_packages
        target = self.out / 'skills/estimating-workflow/references/brand-system.md'
        target.unlink()
        with self.assertRaises(ValueError):
            verify_packages(self.tree, self.out, validate(self.tree, 'release'), 'release')

    def test_archive_tampering_is_rejected(self):
        import zipfile
        import build_dist
        self.assertTrue(hasattr(build_dist, "verify_packages"), "package verifier missing")
        from build_dist import verify_packages
        from toolkit_validation import validate
        self.configure()
        self.assertEqual(self.build("release").returncode, 0)
        archive = next((self.out / "zips").glob("*.zip"))
        with zipfile.ZipFile(archive, "a") as z:
            z.writestr("../escape", "bad")
        with self.assertRaises(ValueError):
            verify_packages(self.tree, self.out, validate(self.tree, "release"), "release")

    def test_release_archives_match_sources_and_generated_helpers(self):
        import zipfile, hashlib
        self.configure()
        result = self.build("release")
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((self.out / 'skills/brand/package-manifest.json').read_text())
        self.assertIn('logo_policy', manifest, 'approved logo disposition missing from package')
        self.assertEqual(manifest['logo_policy']['mode'], 'no-logo')
        archives = sorted((self.out / "zips").glob("*.zip"))
        self.assertEqual(len(archives), 38)
        for archive in archives:
            with zipfile.ZipFile(archive) as z:
                self.assertIsNone(z.testzip())
                self.assertEqual(z.namelist().count("SKILL.md"), 1)
                folder = self.out / "skills" / archive.stem
                self.assertEqual({n: z.read(n) for n in z.namelist()},
                    {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob("*") if p.is_file()})
        from build_dist import package_inputs
        from toolkit_validation import validate
        data = validate(self.tree, "release")
        for identity, name in data["packages"].items():
            for relative, source in package_inputs(self.tree, identity, data["policy"]).items():
                self.assertEqual((self.out / "skills" / name / relative).read_bytes(), source.read_bytes())
        second = self.base / "second"
        self.assertEqual(self.build("release", second).returncode, 0)
        self.assertEqual(json.loads((self.out / "build-report.json").read_text())["packages"],
                         json.loads((second / "build-report.json").read_text())["packages"])

    def test_preview_is_unpacked_and_release_rejects_tokens(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.out / "build-report.json").is_file(), "explicit preview destination/report missing")
        self.assertEqual(len(list((self.out / "skills").iterdir())), 38)
        self.assertFalse(list(self.out.rglob("*.zip")))
        report = json.loads((self.out / "build-report.json").read_text())
        self.assertFalse(report["release"])
        result = self.build("release", self.base / "release")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unresolved required", result.stderr)
        self.assertFalse((self.base / "release").exists())
