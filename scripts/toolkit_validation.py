"""Fail-closed repository checks. No writes and no template expansion."""
from collections import Counter
import json
from pathlib import Path
import re
import yaml
from secure_io import read_text


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def mapping(loader, node):
    return unique_pairs((loader.construct_object(k), loader.construct_object(v, deep=True))
                        for k, v in node.value)


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def load_json(path):
    return json.loads(read_text(path), object_pairs_hook=unique_pairs)


def frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    try:
        data = yaml.load(match[1], Loader=UniqueLoader)
    except (yaml.YAMLError, TypeError) as exc:
        raise ValueError(f"invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be mapping")
    supported = {"name", "description", "argument-hint", "allowed-tools", "user-invocable", "disable-model-invocation"}
    if set(data) - supported:
        raise ValueError("unsupported frontmatter field")
    for field in ("name", "description"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f"nonempty string required: {field}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", data["name"]):
        raise ValueError("unsafe skill name")
    for field in ("argument-hint", "allowed-tools"):
        if field in data and not (isinstance(data[field], str) or
                isinstance(data[field], list) and all(isinstance(x, str) for x in data[field])):
            raise ValueError(f"invalid {field}")
    for field in ("user-invocable", "disable-model-invocation"):
        if field in data and type(data[field]) is not bool:
            raise ValueError(f"invalid {field}")
    return data


def package_names(identities):
    counts = Counter(Path(p).name for p in identities)
    names = {p: (Path(p).name if counts[Path(p).name] == 1 else
                 Path(p).parts[1] + "-" + Path(p).name) for p in sorted(identities)}
    if len(set(names.values())) != len(names):
        raise ValueError("package name collision")
    return names


def validate(root, mode="source"):
    root = Path(root).absolute()
    policy = load_json(root / "scripts/toolkit-policy.json")
    from source_resources import resource_checks
    resource_checks(root, policy, mode, load_json)
    actual = {p.name: sorted(s.name for s in (p / "skills").iterdir() if s.is_dir())
              for p in (root / "plugins").iterdir() if p.is_dir()}
    if actual != policy["plugins"]:
        raise ValueError("inventory mismatch")
    market = load_json(root / ".claude-plugin/marketplace.json")
    if (market.get("name") != "contractor-toolkit" or
            market.get("owner", {}).get("name") != "Formwork"):
        raise ValueError("marketplace metadata")
    entries = market["plugins"]
    if Counter(e["name"] for e in entries) != Counter(actual.keys()):
        raise ValueError("marketplace inventory")
    for entry in entries:
        name = entry["name"]
        if entry["source"] != f"./plugins/{name}":
            raise ValueError("marketplace source")
        manifest = load_json(root / "plugins" / name / ".claude-plugin/plugin.json")
        if (manifest.get("name") != name or manifest.get("version") != market.get("version")
                or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", manifest.get("version", ""))
                or manifest.get("author", {}).get("name") != "Formwork"
                or manifest.get("license") != "MIT"
                or not isinstance(manifest.get("description"), str) or not manifest["description"]):
            raise ValueError(f"plugin metadata: {name}")
        if "version" in entry and entry["version"] != manifest["version"]:
            raise ValueError("entry version mismatch")
    identities = []
    for plugin, skills in actual.items():
        for skill in skills:
            identity = f"plugins/{plugin}/skills/{skill}"
            data = frontmatter(read_text(root / identity / "SKILL.md"))
            if data["name"] != skill:
                raise ValueError("skill name/folder mismatch")
            identities.append(identity)
    from package_layout import package_inputs
    for identity in identities:
        package_inputs(root, identity, policy)
    return {"packages": package_names(identities), "policy": policy}
