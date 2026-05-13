# dist/ — Standalone Skill Packages

This directory is **generated**. Run `./scripts/build-dist.sh` from the repo root to populate it.

## What's in here

After running the build script:

```
dist/
├── skills/                   # Flat skill directories — one per skill
│   ├── initialize/
│   │   ├── SKILL.md
│   │   └── references/        (if present)
│   ├── brand/
│   ├── document-generator/
│   ├── estimating-workflow/
│   ├── proposal/
│   └── …
└── zips/                     # Same skills, zipped for upload
    ├── initialize.zip
    ├── brand.zip
    └── …
```

Each skill is a self-contained package: `SKILL.md` at the root plus its `references/` and `assets/` folders. No `plugin.json` wrapper, no nesting.

## Where each format installs

| Target | Format | How to install |
|---|---|---|
| **Claude Code** (CLI / desktop / IDE extension) | Plugin marketplace | From the repo root: `/plugin marketplace add /path/to/contractor-toolkit` then `/plugin install <plugin>@contractor-toolkit`. Use the top-level `plugins/` directory — ignore `dist/`. |
| **Claude.ai** (web) — personal or org-level | Standalone skill zip | Go to **Settings → Skills → New skill**, drag-and-drop a `.zip` from `dist/zips/`. Repeat per skill you want available. |
| **Cowork** (Anthropic's web workspace) | Standalone skill zip | When creating or editing a skill, upload a `.zip` from `dist/zips/`. |
| **Anthropic API** (custom Skills via SDK) | Standalone skill folder | Point your SDK config at a folder under `dist/skills/<name>/`. |

## Why two formats

- The **plugin marketplace format** (`plugins/*/.claude-plugin/plugin.json` + `plugins/*/skills/<name>/SKILL.md`) is Claude Code-specific. It lets a single marketplace install multiple skills + commands + hooks together.
- The **standalone skill format** (`<name>/SKILL.md` at root, zippable) is what Claude.ai and Cowork accept for org-level skills. They expect one skill per upload.

The build script flattens the former into the latter so you don't have to maintain two copies.

## Regenerating after edits

After editing any `plugins/**/SKILL.md` or its references:

```bash
./scripts/build-dist.sh
```

This wipes `dist/skills/` and `dist/zips/` and regenerates from `plugins/`. This README is preserved. Always edit source under `plugins/` — manual edits to files inside `dist/skills/` are lost on the next build.

## What's NOT included

- `plugin.json` files (Claude Code-only)
- Subagents under `plugins/contractor-estimating/agents/` — Claude Code only; not part of standalone skills
- The top-level `marketplace.json`

If a user installs the standalone skills, they get the SKILL.md content + references. They lose the agent subroutines from `contractor-estimating`, so for the full preconstruction pipeline experience, Claude Code installation is recommended.
