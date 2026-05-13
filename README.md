# Contractor Toolkit

A Claude Code plugin marketplace for general contractors and construction companies. Templated skills for brand identity, branded document generation, preconstruction estimating, proposals, project timelines, change orders, RFIs, submittals, and daily logs.

**Status:** Template repository. Fork this, run `/initialize`, and Claude walks you through configuring every skill for your company.

---

## What's Inside

| Plugin | Purpose | Key Skills |
|--------|---------|------------|
| `contractor-initialize` | One-time setup wizard for your company | `/initialize`, `/update-brand`, `/update-estimating` |
| `contractor-brand` | Brand identity reference — colors, type, voice, logos | `brand` (auto-loads on any branded output) |
| `contractor-docs` | Branded document generator — HTML + DOCX | `document-generator` |
| `contractor-estimating` | Preconstruction estimating pipeline (ROM → Conceptual Budget → Formal Bid) | `/estimate`, `/rom`, `/conceptual-budget`, `/formal-bid`, `/scope-check`, `/sub-bid-package`, `/exclusions-excel`, `/contract` |
| `contractor-extras` | Common contractor deliverables | `/proposal`, `/project-timeline`, `/change-order`, `/rfi`, `/submittal`, `/daily-log`, `/internal-doc` |

---

## Quick Start

### 1. Fork & clone

```bash
gh repo fork <your-org>/contractor-toolkit --clone
cd contractor-toolkit
```

### 2. Install as a Claude Code plugin marketplace

In Claude Code:

```
/plugin marketplace add /absolute/path/to/contractor-toolkit
/plugin install contractor-initialize@contractor-toolkit
```

Then install the rest:

```
/plugin install contractor-brand@contractor-toolkit
/plugin install contractor-docs@contractor-toolkit
/plugin install contractor-estimating@contractor-toolkit
/plugin install contractor-extras@contractor-toolkit
```

### 3. Run `/initialize`

```
/initialize
```

This walks you through:

1. **Company basics** — Name, legal name, tagline, founding year, services
2. **Brand colors** — Primary, accent, neutrals (hex values)
3. **Typography** — Primary font, fallbacks
4. **Logos** — Upload paths for your logo files (orange/black/white/wordmark variants)
5. **Voice & tone** — Personality, banned words, signature phrases
6. **Contact** — Registered + operating addresses, phone, email, domain
7. **ICP** — Target client profile (revenue range, project types, regions)
8. **Estimating defaults** — Default PM, division, city, hourly rates
9. **Sub-brands** (optional) — If you operate multiple divisions

Answers are saved to `.claude/contractor.local.md` and the skill files are updated with your values. You can re-run any sub-step (`/initialize brand`, `/initialize estimating`, etc.) to update individual sections.

### 4. (Optional) Push to your own org

```bash
gh repo create my-construction-skills --private --source=. --remote=origin --push
```

Each teammate clones your fork, installs the marketplace, and gets your company's branded skills — no re-configuration.

---

## File Layout

```
contractor-toolkit/
├── .claude-plugin/
│   └── marketplace.json                    # Marketplace manifest
├── plugins/
│   ├── contractor-initialize/              # /initialize wizard
│   ├── contractor-brand/                   # Brand reference skill
│   ├── contractor-docs/                    # Branded doc generator
│   ├── contractor-estimating/              # 8-phase preconstruction pipeline
│   └── contractor-extras/                  # Proposals, timelines, RFIs, etc.
└── README.md
```

After `/initialize`, additional files appear:

```
.claude/contractor.local.md                 # Your company config (gitignored by default)
.claude/contractor-brand.local.md           # Brand-specific overrides
.claude/contractor-estimating.local.md      # Estimating defaults
```

---

## Customizing Further

Each skill is a plain Markdown file under `plugins/<plugin>/skills/<skill>/SKILL.md`. Edit them directly to:

- Add custom CSI divisions or scope categories
- Adjust voice / tone rules for your market
- Swap in your own exclusion lists, fee tables, or unit-cost references
- Add new document archetypes

If you want to share your customizations back, open a PR against this template repo — generic, broadly-useful improvements are welcome.

---

## Credits

Derived from the Delta Family Companies plugin suite and the Formwork brand identity skill, both built by Sunrise Systems. Genericized for general contractor use under a permissive license.

## License

MIT — see `LICENSE`.
