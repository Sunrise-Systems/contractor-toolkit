#!/usr/bin/env python3
"""Validate repository inputs or read back a previously generated package tree."""
import argparse
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=['source', 'release', 'template-preview'], default='source')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--package-dir', type=Path)
    args = parser.parse_args()
    try:
        from toolkit_validation import validate
        result = validate(args.root, args.mode)
        if args.package_dir:
            if args.mode == 'source':
                raise ValueError('package verification requires release or template-preview mode')
            from build_dist import verify_packages
            verify_packages(args.root.resolve(), args.package_dir.resolve(), result, args.mode)
        print(json.dumps({'status': 'validated', 'mode': args.mode,
                          'plugins': len(result['policy']['plugins']), 'skills': len(result['packages'])}))
    except Exception as exc:
        print(json.dumps({'status': 'needs_human', 'error': str(exc)}), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
