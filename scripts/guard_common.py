"""Bounded local validation primitives; not an authentication boundary."""
import hashlib
import json
from pathlib import Path
from secure_io import read_text


def digest(value):
    raw = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(read_text(path), object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def exact(obj, keys):
    if not isinstance(obj, dict) or set(obj) != set(keys.split()):
        raise ValueError('missing or unknown fields; expected: ' + keys)


def text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('nonempty string required')


def safe_path(path):
    p = Path(path)
    if not p.is_absolute() or '..' in p.parts:
        raise ValueError('absolute non-traversing path required')
    if any(q.is_symlink() for q in [p, *p.parents]):
        raise ValueError('symlinks forbidden')
    return p


def inside(root, relative):
    text(relative)
    p = Path(relative)
    if p.is_absolute() or '..' in p.parts or str(p) == '.':
        raise ValueError('unsafe relative path')
    return safe_path(safe_path(root) / p)


def version(obj, kind):
    supported = (1, 2) if kind == 'change_plan' else (1,)
    if type(obj.get('schema_version')) is not int or obj['schema_version'] not in supported or obj.get('kind') != kind:
        raise ValueError('unsupported schema version/kind')


def validate_schema(value, kind):
    from jsonschema import Draft202012Validator
    schema = load_json(Path(__file__).resolve().parents[1] / 'references/workflow-contract.schema.json')
    Draft202012Validator({'$ref': '#/$defs/' + kind, '$defs': schema['$defs']}).validate(value)


def approval(record, expected, purpose):
    exact(record, 'reviewer purpose digest')
    text(record['reviewer'])
    if record['purpose'] != purpose or record['digest'] != expected:
        raise ValueError('approval digest/purpose stale or absent')
