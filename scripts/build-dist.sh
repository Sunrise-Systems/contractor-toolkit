#!/usr/bin/env bash
# Build standalone skill packages for upload to claude.ai (Skills) and Cowork.
#
# Reads every skill under plugins/<plugin>/skills/<skill>/ and emits:
#   dist/skills/<skill>/             — flat directory ready to upload as a skill
#   dist/zips/<skill>.zip            — same, zipped for the Skills UI upload flow
#
# The Claude Code plugin marketplace (.claude-plugin/marketplace.json + plugins/)
# is untouched — both install paths coexist.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"

# Wipe only the generated subdirs — preserve dist/README.md and any other tracked files
rm -rf "$DIST/skills" "$DIST/zips"
mkdir -p "$DIST" "$DIST/skills" "$DIST/zips"

echo "Building dist/ from plugins/…"
echo ""

skills_count=0
for skill_dir in "$ROOT"/plugins/*/skills/*/; do
  [ -d "$skill_dir" ] || continue
  [ -f "$skill_dir/SKILL.md" ] || continue

  skill_name="$(basename "$skill_dir")"
  plugin_dir="$(dirname "$(dirname "$skill_dir")")"
  plugin_name="$(basename "$plugin_dir")"

  # Default: use the skill folder name. On collision (rare), prefix with
  # the plugin's namespace (stripped of the "contractor-" prefix).
  dist_name="$skill_name"
  if [ -d "$DIST/skills/$dist_name" ]; then
    dist_name="${plugin_name#contractor-}-${skill_name}"
  fi

  target="$DIST/skills/$dist_name"
  mkdir -p "$target"
  cp "$skill_dir/SKILL.md" "$target/"
  [ -d "$skill_dir/references" ] && cp -R "$skill_dir/references" "$target/"
  [ -d "$skill_dir/assets" ] && cp -R "$skill_dir/assets" "$target/"
  [ -d "$skill_dir/scripts" ] && cp -R "$skill_dir/scripts" "$target/"

  echo "  ✓ $dist_name  (from $plugin_name)"
  skills_count=$((skills_count + 1))
done

echo ""
echo "Checking for unresolved template tokens…"
unresolved="$(grep -rEl '\{\{[A-Z_0-9]+\}\}' "$DIST/skills" 2>/dev/null \
  | xargs -I{} grep -hEo '\{\{[A-Z_0-9]+\}\}' {} 2>/dev/null \
  | grep -v -e 'TOKEN' -e 'PLACEHOLDER' | sort -u || true)"
if [ -n "$unresolved" ]; then
  echo ""
  echo "  ⚠ WARNING: these template tokens are still unresolved in dist/skills/:"
  echo "$unresolved" | sed 's/^/      /'
  echo ""
  echo "    These zips will produce documents with raw {{TOKENS}} in them."
  echo "    Run /initialize in Claude Code FIRST, then re-run this script."
  echo "    ({{LOGO_*}} tokens are expected if logo files haven't been provided yet.)"
  echo ""
fi

echo "Zipping packages…"
(
  cd "$DIST/skills"
  for d in */; do
    name="${d%/}"
    zip -qr "$DIST/zips/${name}.zip" "$name"
    echo "  ✓ $name.zip"
  done
)

cat <<EOF

Done.
  $skills_count skills packaged
  Folders: dist/skills/
  Zips:    dist/zips/

Next steps:
  • Claude.ai (web)  → Settings → Skills → "New skill" → upload a zip from dist/zips/
  • Cowork           → attach a zip from dist/zips/ when creating a skill
  • Claude Code      → already installable via the plugin marketplace; no extra step
EOF
