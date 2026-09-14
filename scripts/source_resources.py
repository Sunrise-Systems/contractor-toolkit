"""Explicit resources and exact-context token policy (no wildcard exemptions)."""
from collections import Counter
from pathlib import Path, PurePosixPath
import re
import hashlib
import json
from io import BytesIO
from secure_io import read_bytes, read_text
from functools import lru_cache

TOKEN = re.compile(r"\{\{[^{}\n]+\}\}")


@lru_cache(maxsize=256)
def resource_links(text):
    """CommonMark dependency links and inline-code paths, not regex link guessing."""
    from urllib.parse import unquote
    from markdown_it import MarkdownIt
    refs = set()
    for block in MarkdownIt('commonmark').parse(text):
        for token in block.children or []:
            value = token.attrGet('href') if token.type == 'link_open' else token.content if token.type == 'code_inline' else None
            if isinstance(value, str) and value.startswith(('references/', 'scripts/')) and not any(c.isspace() for c in value):
                refs.add(unquote(value.split('#', 1)[0]))
    return refs

def check_resource_closure(files):
    for relative, source in files.items():
        if not relative.endswith('.md'):
            continue
        for ref in resource_links(read_text(source)):
            safe_path(Path('/'), ref)
            if ref not in files and not (ref.endswith("/") and any(p.startswith(ref) for p in files)):
                raise ValueError(f"missing packaged resource: {relative}: {ref}")


def safe_path(root, relative):
    path = PurePosixPath(relative)
    if path.is_absolute() or not path.parts or ".." in path.parts or "\\" in relative:
        raise ValueError(f"unsafe path: {relative}")
    target = Path(root)
    for part in path.parts:
        target = target / part
        if target.is_symlink():
            raise ValueError(f"symlink forbidden: {target}")
    if not target.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError(f"path escape: {relative}")
    return target


def resource_checks(root, policy, mode, load_json):
    if mode not in {"source", "release", "template-preview"}:
        raise ValueError("unsupported mode")
    if policy.get("schema_version") != 1:
        raise ValueError("unsupported policy version")
    for base in ("plugins", "references", "scripts", ".claude-plugin"):
        safe_path(root, base)
        for path in (root / base).rglob("*"):
            safe_path(root, path.relative_to(root).as_posix())
            if not (path.is_file() or path.is_dir()):
                raise ValueError(f"unsupported filesystem entry: {path}")
    for ref in policy["required_resources"] + policy["shared_files"]:
        if not safe_path(root, ref).is_file():
            raise ValueError(f"missing required resource: {ref}")
    for skill, copies in policy["copies"].items():
        for dest, source in copies.items():
            safe_path(root / skill, dest)
            if not safe_path(root, source).is_file():
                raise ValueError(f"missing copied resource: {source}")
    for skill_path in root.glob("plugins/*/skills/*/SKILL.md"):
        skill = skill_path.parent.relative_to(root).as_posix()
        for child in skill_path.parent.iterdir():
            if child.name not in {"SKILL.md", "references", "assets", "scripts"}:
                raise ValueError(f"unsupported package input: {child}")
        for child in skill_path.parent.rglob("*"):
            if (child.name.startswith(".env") or child.name.endswith((".local.md", ".pem", ".key", ".bak"))
                    or child.name in {"checkpoints", "snapshots", "workflow-state.json", "pricing-evidence.json", "receipt.json"}):
                raise ValueError(f"private runtime input: {child}")
        for doc in skill_path.parent.rglob("*.md"):
            for ref in resource_links(read_text(doc)):
                local = safe_path(skill_path.parent, ref)
                shared = skill in policy["covered_skills"] and ref in policy["shared_files"]
                copied = ref in policy["copies"].get(skill, {})
                if not (local.is_file() or ref.endswith("/") and local.is_dir() or shared or copied):
                    raise ValueError(f"unresolved required resource: {doc}: {ref}")
    registry = load_json(safe_path(root, policy["tokens_file"]))
    for path in (root / "plugins").rglob("*"):
        if not path.is_file():
            continue
        try:
            text = read_text(path)
        except UnicodeError:
            continue
        remainder = TOKEN.sub('', text)
        if '{{' in remainder or '}}' in remainder:
            raise ValueError(f"malformed token delimiters: {path}")
        # Reject traversal even in new undeclared relative reference strings.
        for ref in re.findall(r"`((?:references|assets|scripts)/[^`]+)`", text):
            safe_path(root, ref)
        allowed = {row["line"]: row for row in registry.get(path.relative_to(root).as_posix(), [])}
        for line, count in Counter(l for l in text.splitlines() if TOKEN.search(l)).items():
            row = allowed.get(line)
            if row is None or count > row["count"] or row["kind"] not in {"required", "explanation"}:
                raise ValueError(f"unregistered token context: {path}: {line}")
            if mode == "release" and row["kind"] == "required":
                raise ValueError(f"unresolved required token: {path}: {line}")
    if mode == "release":
        logo = policy["logo"]
        if logo["mode"] == "assets":
            from PIL import Image
            brand = root / "plugins/contractor-brand/skills/brand"
            if not logo["files"]:
                raise ValueError("logo files required")
            for relative in logo["files"]:
                file = safe_path(root, relative)
                if not file.is_relative_to(brand / 'assets/logos') or file.suffix.lower() not in {'.png', '.jpg', '.jpeg'}:
                    raise ValueError('logo must be a bundled PNG/JPEG under brand assets/logos')
                if file.name not in read_text(brand / 'SKILL.md'):
                    raise ValueError('logo not referenced by configured brand')
                try:
                    with Image.open(BytesIO(read_bytes(file))) as image:
                        if image.format not in {'PNG', 'JPEG'}:
                            raise ValueError('unsupported logo format')
                        image.verify()
                except Exception as exc:
                    raise ValueError('invalid logo image') from exc
        elif logo["mode"] == "no-logo":
            approval = logo.get("approval") or {}
            if not (approval.get("reviewer") and approval.get("reason") and
                    re.fullmatch(r"[0-9a-f]{64}", approval.get("digest", ""))):
                raise ValueError("no-logo design approval required")
            brand = root / "plugins/contractor-brand/skills/brand"
            content = {p.relative_to(brand).as_posix(): hashlib.sha256(read_bytes(p)).hexdigest()
                       for p in brand.rglob("*") if p.is_file()}
            bound = hashlib.sha256(json.dumps(content, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            if approval["digest"] != bound:
                raise ValueError("no-logo design digest stale")
        else:
            raise ValueError("logo design unconfigured")
