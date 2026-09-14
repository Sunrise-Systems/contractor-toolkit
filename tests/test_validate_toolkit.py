import json
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]

class SourceTests(unittest.TestCase):
    def fixture(self):
        import tempfile, shutil
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        tree = Path(temp.name) / "source"
        shutil.copytree(ROOT, tree, ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))
        return tree

    def test_asset_logo_must_be_bundled_image_and_dependency_closure_is_source_gate(self):
        from source_resources import resource_checks
        from toolkit_validation import load_json, validate
        tree = self.fixture()
        policy = load_json(tree / 'scripts/toolkit-policy.json')
        policy['copies']['plugins/contractor-estimating/skills/estimating-workflow'].pop('references/brand-system.md')
        (tree / 'scripts/toolkit-policy.json').write_text(json.dumps(policy))
        with self.assertRaisesRegex(ValueError, 'resource'):
            validate(tree)

    def test_explanatory_token_literals_have_exact_context_exemptions(self):
        registry = json.loads((ROOT / 'scripts/template-tokens.json').read_text())
        rows = registry['plugins/contractor-docs/skills/document-generator/SKILL.md']
        row = next(r for r in rows if r['line'].startswith('This skill is **token-driven**.'))
        self.assertEqual(row['kind'], 'explanation')
        tree = self.fixture()
        p = tree / 'plugins/contractor-docs/skills/document-generator/SKILL.md'
        p.write_text(p.read_text() + '\n' + row['line'] + '\n')
        from toolkit_validation import validate
        with self.assertRaisesRegex(ValueError, 'unregistered token'):
            validate(tree)

    def test_markdown_links_and_malformed_tokens_are_not_exempt(self):
        from toolkit_validation import validate
        for addition in ('Required: [rules](references/missing-rules.md).',
                         'Read `references/nested/missing.md`.', '{{COMPANY_NAME}',
                         "Required: [rules](references/nested/missing.md 'Rules').",
                         '[rules][r]\n\n[r]: references/nested/missing.md "Rules"'):
            tree = self.fixture()
            p = tree / 'plugins/contractor-estimating/skills/estimate/SKILL.md'
            p.write_text(p.read_text() + '\n' + addition + '\n')
            with self.subTest(addition=addition), self.assertRaises(ValueError):
                validate(tree)

    def test_private_runtime_files_and_unknown_frontmatter_block(self):
        from toolkit_validation import validate, frontmatter
        for relative in ('.env', 'references/workflow-state.json', 'assets/checkpoints/before.json'):
            tree = self.fixture()
            p = tree / 'plugins/contractor-brand/skills/brand' / relative
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text('synthetic private runtime content')
            with self.subTest(relative=relative), self.assertRaisesRegex(ValueError, 'private|unsupported'):
                validate(tree)
        with self.assertRaises(ValueError):
            frontmatter('---\nname: x\ndescription: y\nunknown: true\n---\n')

    def test_new_reference_and_logo_policy(self):
        from toolkit_validation import validate
        tree = self.fixture()
        skill = tree / "plugins/contractor-brand/skills/brand/SKILL.md"
        skill.write_text(skill.read_text() + "\nRead `references/not-present.md`.\n")
        with self.assertRaisesRegex(ValueError, "resource"):
            validate(tree)
        tree = self.fixture()
        # Configure only required lines; explanatory occurrences remain exact.
        registry = json.loads((tree / "scripts/template-tokens.json").read_text())
        import re
        for name, rows in registry.items():
            p = tree / name
            text = p.read_text()
            for row in rows:
                if row["kind"] == "required":
                    text = text.replace(row["line"], re.sub(r"\{\{[^{}]+\}\}", "Synthetic", row["line"]))
            p.write_text(text)
        with self.assertRaisesRegex(ValueError, "logo"):
            validate(tree, "release")
        p = tree / "scripts/toolkit-policy.json"
        policy = json.loads(p.read_text())
        policy["logo"] = {"mode": "no-logo", "files": [], "approval": {"reviewer": "Synthetic reviewer", "reason": "Text-only design", "digest": "0" * 64}}
        p.write_text(json.dumps(policy))
        with self.assertRaisesRegex(ValueError, "logo.*digest"):
            validate(tree, "release")
        import hashlib
        brand = tree / "plugins/contractor-brand/skills/brand"
        approval_digest = hashlib.sha256(json.dumps({f.relative_to(brand).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest()
            for f in brand.rglob("*") if f.is_file()}, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        policy["logo"]["approval"]["digest"] = approval_digest
        p.write_text(json.dumps(policy))
        self.assertEqual(len(validate(tree, "release")["packages"]), 38)

    def test_resources_paths_tokens_fail_closed(self):
        from toolkit_validation import validate
        for mutation in ("missing", "symlink", "traversal", "token", "duplicate-token"):
            with self.subTest(mutation=mutation):
                tree = self.fixture()
                resource = tree / "plugins/contractor-brand/skills/brand/references/voice-guide.md"
                if mutation == "missing":
                    resource.unlink()
                elif mutation == "symlink":
                    resource.unlink()
                    resource.symlink_to("/etc/passwd")
                elif mutation == "traversal":
                    resource.write_text(resource.read_text() + "\nRead `references/../../../../outside.md`\n")
                elif mutation == "token":
                    resource.write_text(resource.read_text() + "\n{{UNREGISTERED_TOKEN}}\n")
                else:
                    resource.write_text(resource.read_text() + "\n" + next(l for l in resource.read_text().splitlines() if "{{" in l))
                with self.assertRaises(ValueError):
                    validate(tree)
        with self.assertRaisesRegex(ValueError, "unresolved required"):
            validate(ROOT, "release")

    def test_manifest_consistency_and_names(self):
        from toolkit_validation import validate, package_names
        a, b = "plugins/a/skills/same", "plugins/b/skills/same"
        self.assertEqual(package_names([b, a]), {a: "a-same", b: "b-same"})
        for mutation in ("author", "version", "source", "duplicate", "inventory"):
            with self.subTest(mutation=mutation):
                tree = self.fixture()
                p = tree / "plugins/contractor-brand/.claude-plugin/plugin.json"
                data = json.loads(p.read_text())
                if mutation == "author":
                    del data["author"]
                elif mutation == "version":
                    data["version"] = "9.9.9"
                elif mutation == "inventory":
                    (tree / "plugins/contractor-brand/skills/undeclared").mkdir()
                else:
                    p = tree / ".claude-plugin/marketplace.json"
                    data = json.loads(p.read_text())
                    if mutation == "source":
                        data["plugins"][0]["source"] = "../outside"
                    else:
                        data["plugins"].append(data["plugins"][0])
                p.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    validate(tree)

    def test_all_inventory_and_strict_frontmatter(self):
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        import importlib.util
        self.assertIsNotNone(importlib.util.find_spec("toolkit_validation"), "source validator missing")
        from toolkit_validation import validate, frontmatter
        self.assertEqual(len(validate(ROOT)["packages"]), 38)
        for bad in ("---\nname: x\nname: y\ndescription: z\n---\n", "---\n- x\n---\n", "---\nname: x\ndescription: a: b\n---\n", "---\nname: 2\ndescription: x\n---\n", "---\nname: x\ndescription: x\nallowed-tools: 3\n---\n"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                frontmatter(bad)
        self.assertEqual(frontmatter('---\nname: x\ndescription: y\nargument-hint: [a, b]\n---\n')["argument-hint"], ["a", "b"])

class DeliveryTests(unittest.TestCase):
    def test_validation_cli_and_ci_documented(self):
        import subprocess, sys
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate-toolkit.py"), "--mode", "source"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["skills"], 38)
        ci = ROOT / ".github/workflows/validate.yml"
        self.assertTrue(ci.is_file(), "CI gate missing")
        for command in ('validate-toolkit.py --mode source', 'unittest discover -s tests -v', 'bash -n scripts/build-dist.sh'):
            self.assertIn(command, ci.read_text())
        self.assertIn('template-preview', (ROOT / 'README.md').read_text())
        self.assertIn('not_issued', (ROOT / 'dist/README.md').read_text())

class MetadataTests(unittest.TestCase):
    def test_brand_entry_point_is_compact(self):
        p = ROOT / "plugins/contractor-brand/skills/brand/SKILL.md"
        self.assertLessEqual(len(p.read_text().splitlines()), 300)
        self.assertTrue((p.parent / "references/voice-and-audience.md").is_file())
        self.assertTrue((p.parent / "references/content-enforcement.md").is_file())

    def test_brand_metadata_is_valid(self):
        p = ROOT / "plugins/contractor-brand"
        try:
            data = yaml.safe_load((p / "skills/brand/SKILL.md").read_text().split("---")[1])
        except yaml.YAMLError as exc:
            self.fail(f"Brand YAML must parse: {exc}")
        self.assertIsInstance(data["description"], str)
        self.assertEqual(json.loads((p / ".claude-plugin/plugin.json").read_text())["author"]["name"], "Formwork")
