"""Exact staged images, explicit contexts, no target mutation."""
from guard_common import approval, digest, exact, inside, safe_path, text, version
import json
import os
import shutil
from secure_io import read_bytes, write_bytes, mkdir, stable_io, read_optional, parent_fd
from guard_common import load_json, validate_schema


def _checkpoint(plan, directory):
    path = safe_path(directory)
    root = safe_path(plan['root'])
    if path == root or root in path.parents or path in root.parents:
        raise ValueError('checkpoint must be outside target root')
    return path


@stable_io
def snapshot(plan, directory):
    checked = check_change(plan)
    dest = _checkpoint(plan, directory)
    if not dest.parent.is_dir():
        raise ValueError('checkpoint parent must exist')
    with parent_fd(dest):
        pass  # bind checkpoint ancestors before capacity check and creation
    needed = sum(len((t['before'] or '').encode()) for t in plan['targets'])
    if shutil.disk_usage(dest.parent).free < needed + 65536:
        raise ValueError('insufficient backup capacity')
    mkdir(dest, mode=0o700)  # exclusive: existing/partial checkpoints never overwritten
    records = []
    for index, target in enumerate(plan['targets']):
        before = target['before']
        name = None if before is None else f'{index}.before'
        if name is not None:
            file = dest / name
            write_bytes(file, before.encode(), mode=0o400)
            if digest(read_bytes(file)) != target['before_sha256']:
                raise ValueError('backup verification failed')
        records.append({'path': target['path'], 'backup': name, 'sha256': target['before_sha256']})
    check_change(plan)  # concurrent edits invalidate even an otherwise complete backup
    write_bytes(dest / 'manifest.json', json.dumps(
        {'plan_digest': checked['plan_digest'], 'records': records}).encode(), mode=0o400)
    return checked | {'checkpoint': str(dest)}


def verify_change(plan, directory):
    checked = check_change(plan, read_before=False)
    dest = _checkpoint(plan, directory)
    manifest = load_json(inside(dest, 'manifest.json'))
    exact(manifest, 'plan_digest records')
    if manifest['plan_digest'] != checked['plan_digest'] or len(manifest['records']) != len(plan['targets']):
        raise ValueError('checkpoint plan mismatch')
    states, file_hashes = {}, {}
    for index, (target, record) in enumerate(zip(plan['targets'], manifest['records'])):
        expected = {'path': target['path'], 'backup': None if target['before'] is None else f'{index}.before', 'sha256': target['before_sha256']}
        if record != expected:
            raise ValueError('checkpoint record mismatch')
        if record['backup'] is not None and digest(read_bytes(inside(dest, record['backup']))) != record['sha256']:
            raise ValueError('backup corrupt')
        path = inside(plan['root'], target['path'])
        content = read_optional(path)
        actual = digest(content) if content is not None else None
        file_hashes[target['path']] = actual
        states[target['path']] = ('approved-after' if actual == target['after_sha256'] else
                                  'before' if actual == target['before_sha256'] else 'conflict')
    return {'status': 'verified' if all(v == 'approved-after' for v in states.values()) else 'needs_human',
            'targets': states, 'file_hashes': file_hashes, 'plan_digest': checked['plan_digest'], 'issuance': 'not_issued', 'next_safe_action': 'human review; never automatic retry or rollback'}


def _parsed(raw, kind):
    if kind == 'text':
        return {'__body__': raw}
    if kind == 'markdown':
        import re
        match = re.fullmatch(r'---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)', raw, re.S)
        if not match:
            raise ValueError('Markdown requires YAML frontmatter')
        fields = _parsed(match[1], 'yaml')
        if '__body__' in fields:
            raise ValueError('reserved Markdown body field')
        return dict(fields, __body__=match[2])
    if kind == 'json':
        from guard_common import load_json
        def pairs(items):
            result = {}
            for k, v in items:
                if k in result:
                    raise ValueError('duplicate JSON key')
                result[k] = v
            return result
        value = json.loads(raw, object_pairs_hook=pairs)
    elif kind == 'yaml':
        import yaml
        class Unique(yaml.SafeLoader):
            pass
        def mapping(loader, node):
            result = {}
            for k, v in node.value:
                key = loader.construct_object(k)
                if key in result:
                    raise ValueError('duplicate YAML key')
                result[key] = loader.construct_object(v, deep=True)
            return result
        Unique.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
        value = yaml.load(raw, Loader=Unique)
    else:
        raise ValueError('only whole JSON/YAML mapping images supported')
    if not isinstance(value, dict):
        raise ValueError('mapping image required')
    digest(value)  # reject nonfinite values and non-JSON YAML custom scalar types
    return value


def check_change(plan, root=None, read_before=True):
    validate_schema(plan, 'change_plan')
    exact(plan, 'schema_version kind operation_id root selected_sections targets approval')
    version(plan, 'change_plan')
    text(plan['operation_id'])
    root = safe_path(plan['root']) if root is None else safe_path(root)
    if str(root) != plan['root'] or not root.is_dir():
        raise ValueError('root mismatch or missing')
    if not isinstance(plan['selected_sections'], list) or not plan['selected_sections']:
        raise ValueError('selected sections required')
    for section in plan['selected_sections']:
        text(section)
    if not isinstance(plan['targets'], list) or not plan['targets']:
        raise ValueError('targets required')
    paths = set()
    for target in plan['targets']:
        exact(target, 'path format before after before_sha256 after_sha256 selected_fields contexts'
              + (' section' if plan['schema_version'] == 2 else ''))
        path = inside(root, target['path'])
        if path in paths:
            raise ValueError('duplicate target')
        paths.add(path)
        before, after = target['before'], target['after']
        text(after)
        import re
        from collections import Counter
        pattern = r'\{\{[^{}\n]+\}\}'
        if Counter(re.findall(pattern, after)) - Counter(re.findall(pattern, before or '')):
            raise ValueError('new unresolved tokens')
        remainder = re.sub(pattern, '', after)
        if '{{' in remainder or '}}' in remainder:
            raise ValueError('malformed unresolved tokens')
        if target['before_sha256'] != (None if before is None else digest(before.encode())) or target['after_sha256'] != digest(after.encode()):
            raise ValueError('image digest mismatch')
        old, new = ({} if before is None else _parsed(before, target['format'])), _parsed(after, target['format'])
        fields = target['selected_fields']
        if not isinstance(fields, list) or not fields or len(set(fields)) != len(fields):
            raise ValueError('unique selected fields required')
        if plan['schema_version'] == 2:
            text(target['section'])
            if target['section'] not in plan['selected_sections']:
                raise ValueError('unselected section')
        elif not set(fields) <= set(plan['selected_sections']):
            raise ValueError('unselected section')
        if digest({k: v for k, v in old.items() if k not in fields}) != digest({k: v for k, v in new.items() if k not in fields}):
            raise ValueError('unrequested fields changed')
        staged = before or ''
        if not isinstance(target['contexts'], list) or not target['contexts']:
            raise ValueError('explicit contexts required')
        for context in target['contexts']:
            exact(context, 'before after count')
            if type(context['count']) is not int or context['count'] != 1:
                raise ValueError('one unique context required')
            if before is None and context['before'] == '' and staged == '':
                staged = context['after']
            else:
                text(context['before'])
                if staged.count(context['before']) != 1:
                    raise ValueError('ambiguous context')
                staged = staged.replace(context['before'], context['after'], 1)
        if staged != after:
            raise ValueError('contexts do not produce exact after image')
        if read_before:
            writable = path if path.exists() else path.parent
            if not writable.exists() or not writable.stat().st_mode & 0o222 or not os.access(writable, os.W_OK):
                raise ValueError('target or parent is read-only')
            actual = read_optional(path)
            if actual != (None if before is None else before.encode()):
                raise ValueError('stale before image; approval invalidated')
    plan_digest = digest({k: v for k, v in plan.items() if k != 'approval'})
    approval(plan['approval'], plan_digest, 'local_update')
    return {'status': 'validated', 'plan_digest': plan_digest, 'issuance': 'not_issued'}
