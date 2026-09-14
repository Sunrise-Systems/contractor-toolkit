#!/usr/bin/env bash
# Validation and staging use the selected isolated Python environment.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec "${PYTHON:-python3}" "$ROOT/scripts/build_dist.py" "$@"
