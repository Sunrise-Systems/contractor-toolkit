#!/usr/bin/env bash
# PostToolUse guard: block branded deliverables (generated .html files) that
# still contain unresolved {{TEMPLATE_TOKENS}}. Skill/plugin source files are
# exempt — they're SUPPOSED to contain tokens until /initialize runs.

set -euo pipefail

input="$(cat)"

file_path="$(printf '%s' "$input" | python3 -c '
import json, sys
try:
    data = json.load(sys.stdin)
    print(data.get("tool_input", {}).get("file_path", ""))
except Exception:
    print("")
')"

# Only inspect generated HTML deliverables, never plugin source.
case "$file_path" in
  *.html) ;;
  *) exit 0 ;;
esac
case "$file_path" in
  */plugins/*|*/dist/*|*SKILL.md) exit 0 ;;
esac

[ -f "$file_path" ] || exit 0

tokens="$(grep -Eo '\{\{[A-Z_0-9]+\}\}' "$file_path" | sort -u || true)"
if [ -n "$tokens" ]; then
  echo "Generated document contains unresolved template tokens: $(printf '%s' "$tokens" | tr '\n' ' ')" >&2
  echo "Do not deliver this file. Run /initialize (or substitute the missing values), regenerate, and re-check." >&2
  exit 2
fi

exit 0
