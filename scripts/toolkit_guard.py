#!/usr/bin/env python3
"""Supervised local checks. Never edits targets, approves, or issues outputs."""
import argparse
import json
import sys
from guard_common import load_json, safe_path
from secure_io import write_bytes, stable_io, parent_fd
from change_checks import check_change, snapshot, verify_change


@stable_io
def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    change = commands.add_parser('check-change')
    change.add_argument('--plan', required=True)
    change.add_argument('--root', required=True)
    for name in ('snapshot', 'verify-change'):
        sub = commands.add_parser(name)
        sub.add_argument('--plan', required=True)
        sub.add_argument('--checkpoint-dir', required=True)
    sub = commands.add_parser('check-workflow')
    sub.add_argument('--state', required=True)
    sub.add_argument('--evidence', required=True)
    sub = commands.add_parser('verify-artifact')
    for field in ('artifact', 'expectations', 'receipt'):
        sub.add_argument('--' + field, required=True)
    args = parser.parse_args(argv)
    try:
        plan = load_json(args.plan) if hasattr(args, 'plan') else None
        if args.command == 'verify-artifact':
            from artifact_checks import verify_artifact
            dest = safe_path(args.receipt)
            if dest.exists() or not dest.parent.is_dir():
                raise ValueError('receipt requires new destination in existing safe directory')
            with parent_fd(dest):
                pass  # bind receipt ancestors before artifact verification
            receipt = verify_artifact(safe_path(args.artifact), load_json(args.expectations))
            write_bytes(dest, json.dumps(receipt, sort_keys=True).encode())
            if load_json(dest) != receipt:
                raise ValueError('receipt readback mismatch')
            result = {'status': 'verified', 'receipt': str(dest), 'issuance': 'not_issued'}
        elif args.command == 'check-workflow':
            from workflow_checks import check_workflow
            result = check_workflow(load_json(args.state), load_json(args.evidence))
        elif args.command == 'check-change':
            result = check_change(plan, args.root)
        elif args.command == 'snapshot':
            result = snapshot(plan, args.checkpoint_dir)
        else:
            result = verify_change(plan, args.checkpoint_dir)
        print(json.dumps(result, sort_keys=True))
        return 1 if result['status'] == 'needs_human' else 0
    except Exception as exc:
        print(json.dumps({'status': 'needs_human', 'error': str(exc), 'issuance': 'not_issued'}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
