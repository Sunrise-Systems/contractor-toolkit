---
name: initialize
description: One-time setup wizard for contractor-toolkit. Configures company brand, voice, logos, ICP, capabilities, and estimating defaults. Triggers on /initialize.
argument-hint: "[section name to re-run just one section: company, services, brand, typography, logos, voice, contact, icp, capabilities, estimating]"
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
  - Glob
  - Grep
  - Bash
---

# /initialize — Contractor Toolkit Setup Wizard

This is the **first thing** a new user runs. It's a conversational interview that configures every other plugin in the toolkit. After this finishes, `/estimate`, `/proposal`, `/branded-doc`, etc. will all be pre-filled with the company's brand, voice, and defaults.

## How to run this

If an argument was passed (`company`, `services`, `brand`, `typography`, `logos`, `voice`, `contact`, `icp`, `capabilities`, `estimating`), **jump straight to that section** and skip the others. Otherwise, walk all 10 sections in order.

Before starting, check whether `.claude/contractor.local.md` already exists.
- If it exists and no argument was passed: tell the user "Looks like you've already run /initialize. Want to start fresh, or re-run a specific section? (`company`, `services`, `brand`, `typography`, `logos`, `voice`, `contact`, `icp`, `capabilities`, `estimating`)" — let them choose.
- Otherwise: proceed.

## Tone

Conversational. Friendly. Not bureaucratic. One section at a time — never dump 30 questions at once. Always offer a sensible default the user can accept by saying "default" or "skip". Show progress like `Section 3 of 10 — Brand Colors`.

Use `AskUserQuestion` for genuinely multi-choice selections (service lines, voice archetype). Use plain conversational prose for everything else.

---

## Section 1 of 10 — Company Basics

> "Let's start with the basics. What's your company called?"

Ask, in a natural flow:
- **Display name** — what shows on documents (e.g., "Apex Construction")
- **Short name** — the casual one-word version used in running text (e.g., "Apex"). Default: first word of display name.
- **Legal name with entity type** — for contracts (e.g., "Apex Construction Group, LLC")
- **Founded year** — for credibility blurbs. Derive `years_experience` from it (current year − founded year, phrased like "25+ years").
- **Ownership type** — family-owned, employee-owned, privately held, partnership, etc. Default: "privately held".
- **Company type** — what they'd call themselves in one phrase: "general contractor", "design-build firm", "GC with in-house A&E", etc.
- **Tagline** — optional, one line (e.g., "Built right. On time.")
- **One-sentence description** — what the company does, plain English

Write to `.claude/contractor.local.md` (create if missing) under a `# Company` section.

---

## Section 2 of 10 — Services & Sub-brands

> "What service lines do you offer? Pick all that apply."

Use `AskUserQuestion` with a multi-select:
- General Contracting
- Design-Build
- Architecture & Engineering
- Electrical
- Plumbing
- Mechanical / HVAC
- Civil
- Concrete
- Drywall
- Framing
- Roofing
- Painting
- Specialty Trade — Other (ask for description)

Then ask: **"Do you operate these as separate sub-brands (different names, logos, colors per service line), or as one unified brand?"** Most contractors are unified — that's the default. If sub-brands: collect each sub-brand's name (these populate `{{SUBBRAND_N_NAME}}` tokens).

Then ask: **"What work do you self-perform vs. subcontract?"** Offer the common GC default (self-perform: supervision, general labor, rough carpentry, drywall, painting, light demo; sub out: MEP, roofing, concrete, steel, specialty trades) and let them adjust. This feeds Phase 3 of the estimating pipeline.

Save to `contractor.local.md` and `.claude/contractor-brand.local.md`.

---

## Section 3 of 10 — Brand Colors

> "Let's talk colors. Got a primary brand color? Drop a hex code or describe it."

- **Primary color** — hex (e.g., `#1A1A1A`). If unsure, recommend a clean black + white + grays system: `#0A0A0A` primary, white background, gray scale neutrals. Explain this reads as premium / architectural / serious.
- **Accent color** — optional. One accent works best. Default: none.
- **Tonal scale** — the document system uses a 7-step neutral scale. Offer the standard defaults and only ask for overrides if the user has a brand guide that specifies them:

| Role | Default hex | Stored as |
|---|---|---|
| Ink (titles, totals) | `1A1A1A` | `ink_hex` |
| Body text | `2B2B2B` | `body_hex` |
| Mid (supporting text) | `555555` | `mid_hex` |
| Muted (labels, headers) | `888888` | `muted_hex` |
| Light (tertiary) | `BBBBBB` | `light_hex` |
| Rule (hairlines) | `DDDDDD` | `rule_hex` |
| Soft fill (division bands) | `F7F7F5` | `soft_fill_hex` |

Store each value **without** the leading `#` (the templates add it where needed). Most users should just accept the defaults — say so.

Save to `.claude/contractor-brand.local.md`.

---

## Section 4 of 10 — Typography

> "Pick a typeface. If you don't have a preference, I'll suggest something clean."

Suggestions:
- **Helvetica Neue** (fallback Arial) — safe, neutral, premium
- **Inter** — modern, web-friendly, free
- **Monument Grotesk** — architectural, distinctive
- **"I don't know — pick something clean"** → default to Helvetica Neue / Arial

Store both `typography_primary` (e.g., `Helvetica Neue`) and `typography_fallback` (the CSS fallback stack, e.g., `Helvetica, Arial, sans-serif`).

Save to `contractor-brand.local.md`.

---

## Section 5 of 10 — Logos

> "Drop your logo files into `plugins/contractor-brand/skills/brand/assets/logos/`. I'll look for these variants:"

Checklist:
- `wordmark-primary.svg` (or .png) — main horizontal logo
- `wordmark-stacked.svg` — stacked variant (optional)
- `mark-only.svg` — icon / monogram alone
- `wordmark-white.svg` — for dark backgrounds
- `wordmark-black.svg` — for light backgrounds
- One file per sub-brand, if sub-brands exist

Glob the directory and report what's present vs. missing. Record the actual filenames found — they populate the `{{LOGO_*}}` tokens during substitution. If files are missing, save the checklist to `contractor-brand.local.md` and tell the user: "No worries — drop them in later and re-run `/initialize logos`." Until then, the `{{LOGO_*}}` tokens stay unsubstituted on purpose — the brand skill is instructed to stop and ask rather than improvise a missing logo.

---

## Section 6 of 10 — Voice & Tone

> "How does your company sound when it talks?"

Use `AskUserQuestion` for the archetype:
- **Approachable Expert** — warm, plain-spoken, confident
- **No-Nonsense Builder** — direct, blue-collar, no fluff
- **Visionary Advisor** — strategic, big-picture, design-forward
- **Premium Craftsman** — restrained, precise, quality-obsessed
- **Other** — let user describe

Then ask conversationally:
- **Core belief** — one sentence on why the company exists or what it stands for (e.g., "A building is only as good as the relationships that built it."). This appears in brand-led documents. Offer to draft one from the company description if they're stuck.
- **Brand pillars** — 3–5 short phrases the brand stands on (e.g., "Self-perform depth", "Permits, fast", "One team, design through closeout"). Offer to draft from what's been collected so far; these populate `{{PILLAR_1}}`–`{{PILLAR_5}}`.
- **Tone attributes** — 3–4 adjectives for how copy should read (e.g., "direct, warm, specific"). Derive a default from the archetype.
- **Archetype description** — one sentence expanding the archetype in this company's terms. Draft it for them from the answers above; they approve or tweak.
- **3–5 signature phrases** — taglines or sayings the company actually uses
- **Banned words** — words/phrases never to use (e.g., "synergy", "world-class", "cheap")

Save to `.claude/contractor-brand.local.md` under `# Voice`.

---

## Section 7 of 10 — Contact Info

> "Now the boring-but-important stuff."

- **Registered legal address** — for contracts (street, city, state, ZIP)
- **Operating address** — for proposals/marketing (may be same)
- **Main phone**
- **Main email**
- **Website domain** (e.g., `apexbuilds.com`)

Save to `contractor.local.md` under `# Contact`.

---

## Section 8 of 10 — ICP / Target Client

> "Who are you trying to win work from?"

- **Project type focus** — multi-select via `AskUserQuestion`: Residential, Commercial Tenant Improvement, Ground-Up Commercial, Healthcare, K-12, Higher Ed, Hospitality, Multi-Family, Industrial, Mixed-Use, Government, Other
- **Typical project size** — revenue range ($X–$Y) or sqft range
- **Typical client annual revenue** — rough band
- **Geographic regions** — cities, counties, or states served

Save to `.claude/contractor.local.md` under `# ICP`.

---

## Section 9 of 10 — Capabilities & Differentiators

> "Last questions before estimating. This is the material that wins work — it feeds `/capabilities-statement`, proposals, and the investment deck."

Ask conversationally, allowing "skip" on any:
- **Differentiators** — 3–5 reasons clients pick them over the next GC (in-house A&E, fast permitting, self-perform depth, design-build delivery, owner's-rep experience…)
- **Notable projects** — 3–5 best past projects: name, type, size (SF and/or $), location, one-line outcome
- **Certifications & memberships** — licenses held (with numbers if they want them printed), LEED, DBE/MBE/WBE/SBE, OSHA training levels, AGC/ABC membership
- **Bonding capacity** — single project / aggregate, surety name (optional)
- **Key personnel** — 2–4 leaders: name, title, years in industry, one-line bio
- **Safety record** — EMR if known, OSHA recordable rate (optional)

Save to `.claude/contractor.local.md` under `# Capabilities`. Skills read this section at runtime — it is not token-substituted.

---

## Section 10 of 10 — Estimating Defaults

> "Last section. These pre-fill `/estimate` so you don't retype them every time."

- **Default PM name**
- **Default PM title** (e.g., "Senior Project Manager")
- **Default PM email**
- **Default PM phone**
- **Default service line for estimates** — pick one from Section 2
- **Default city/market** — also stored as `market_city`
- **Market region** — the broader region for cost context (e.g., "Greater Phoenix", "SF Bay Area")
- **Contractor license scheme** — which state's classification system applies (e.g., "CSLB (California)", "ROC (Arizona)", "TDLR (Texas)"). Default reference data ships as California CSLB; flag that `references/sub-trade-mapping.md` should be swapped if they pick another state.
- **Hourly markup %** (default: 1.5x)
- **OH&P %** (default: 15%)
- **Contingency %** (default: 10%)

Save to `.claude/contractor-estimating.local.md`.

---

## After all sections — Write config files

Master file `.claude/contractor.local.md` should have YAML frontmatter with every value, plus a human-readable summary below. Example shape:

```markdown
---
company_name: Apex Construction
company_short: Apex
company_legal_name: Apex Construction Group, LLC
company_type: general contractor
ownership_type: family-owned
tagline: Built right. On time.
founded_year: 2014
years_experience: "12+ years"
core_belief: "A building is only as good as the relationships that built it."
primary_color: "#0A0A0A"
accent_color: ""
ink_hex: "1A1A1A"
body_hex: "2B2B2B"
mid_hex: "555555"
muted_hex: "888888"
light_hex: "BBBBBB"
rule_hex: "DDDDDD"
soft_fill_hex: "F7F7F5"
typography_primary: "Helvetica Neue"
typography_fallback: "Helvetica, Arial, sans-serif"
registered_address: "123 Main St, Phoenix, AZ 85001"
operating_address: "123 Main St, Phoenix, AZ 85001"
phone: "(602) 555-0100"
email: "hello@apexbuilds.com"
domain: "apexbuilds.com"
voice_archetype: "Approachable Expert"
target_revenue_range: "$2M–$25M projects"
project_types: ["Commercial TI", "Ground-Up Commercial", "Multi-Family"]
service_lines: ["General Contracting", "Design-Build"]
self_perform: ["supervision", "rough carpentry", "drywall", "painting"]
pm_name: "Jordan Reyes"
pm_title: "Senior Project Manager"
pm_email: "jordan@apexbuilds.com"
pm_phone: "(602) 555-0142"
default_division: "General Contracting"
default_city: "Phoenix"
market_region: "Greater Phoenix"
license_scheme: "ROC (Arizona)"
ohp_percent: 15
contingency_percent: 10
---

# Apex Construction — Master Config

Last updated: [today's date]

## Capabilities
[differentiators, notable projects, certifications, bonding, key personnel, safety record — prose/list form]
```

Also write per-plugin files:
- `.claude/contractor-brand.local.md` — colors, tonal scale, typography, logos, voice
- `.claude/contractor-estimating.local.md` — PM, defaults, markups, license scheme
- `.claude/contractor-docs.local.md` — company, contact, domain (for document headers/footers)

---

## Template substitution — apply the config across plugins

After config is written, walk every SKILL.md and supporting file in the sibling plugins and replace `{{PLACEHOLDER}}` tokens with the values just collected.

Use `Glob` to find candidates:
```
plugins/contractor-brand/**/*.md
plugins/contractor-docs/**/*.md
plugins/contractor-estimating/**/*.md
plugins/contractor-extras/**/*.md
plugins/contractor-subs/**/*.md
```

For each file, do exact string substitution of these tokens:

### Company & contact

| Placeholder | Source field |
|---|---|
| `{{COMPANY_NAME}}` | company_name |
| `{{COMPANY_SHORT}}` | company_short |
| `{{COMPANY_LEGAL_NAME}}` | company_legal_name |
| `{{COMPANY_TYPE}}` | company_type |
| `{{OWNERSHIP_TYPE}}` | ownership_type |
| `{{TAGLINE}}` | tagline |
| `{{FOUNDED_YEAR}}` | founded_year |
| `{{YEARS_EXPERIENCE}}` | years_experience |
| `{{CORE_BELIEF}}` | core_belief |
| `{{REGISTERED_ADDRESS}}` | registered_address |
| `{{OPERATING_ADDRESS}}` | operating_address |
| `{{PHONE}}` | phone |
| `{{EMAIL}}` | email |
| `{{DOMAIN}}` | domain |

### Brand & typography

| Placeholder | Source field |
|---|---|
| `{{PRIMARY_COLOR}}` | primary_color (with `#`) |
| `{{ACCENT_COLOR}}` | accent_color (with `#`, or empty) |
| `{{INK_HEX}}` | ink_hex (no `#`) |
| `{{BODY_HEX}}` | body_hex (no `#`) |
| `{{MID_HEX}}` | mid_hex (no `#`) |
| `{{MUTED_HEX}}` | muted_hex (no `#`) |
| `{{LIGHT_HEX}}` | light_hex (no `#`) |
| `{{RULE_HEX}}` | rule_hex (no `#`) |
| `{{INK_COLOR}}` | `#` + ink_hex |
| `{{BODY_COLOR}}` | `#` + body_hex |
| `{{MID_COLOR}}` | `#` + mid_hex |
| `{{MUTED_COLOR}}` | `#` + muted_hex |
| `{{LIGHT_COLOR}}` | `#` + light_hex |
| `{{RULE_COLOR}}` | `#` + rule_hex |
| `{{SOFT_FILL_COLOR}}` | `#` + soft_fill_hex |
| `{{NEUTRAL_COLOR}}` | `#FFFFFF` |
| `{{TYPOGRAPHY_PRIMARY}}` | typography_primary |
| `{{TYPOGRAPHY_FALLBACK}}` | typography_fallback |
| `{{VOICE_ARCHETYPE}}` | voice_archetype |
| `{{VOICE_ARCHETYPE_DESCRIPTION}}` | archetype description (Section 6) |
| `{{TONE_ATTRIBUTES}}` | tone attributes, comma-joined |
| `{{PILLAR_1}}`…`{{PILLAR_5}}` | brand pillars in order (if fewer than 5 pillars were given, delete the unused pillar lines from the target file instead of leaving tokens) |

### Logos & sub-brands (only substitute what exists)

| Placeholder | Source |
|---|---|
| `{{LOGO_WORDMARK}}` / `{{LOGO_PRIMARY_HORIZONTAL}}` | filename of the horizontal wordmark found in Section 5 |
| `{{LOGO_PRIMARY_STACKED}}` | filename of the stacked wordmark |
| `{{LOGO_MARK}}` | filename of the mark-only file |
| `{{LOGO_WHITE}}` | filename of the white variant |
| `{{LOGO_BLACK}}` | filename of the black variant |
| `{{SUBBRAND_1_NAME}}`…`{{SUBBRAND_3_NAME}}` | sub-brand names from Section 2 |
| `{{LOGO_SUBBRAND_1}}`…`{{LOGO_SUBBRAND_3}}` | sub-brand logo filenames |
| `{{SUBBRANDS}}` / `{{SUBBRAND_ROSTER}}` | comma-joined sub-brand names |

**The `{{SUBBRAND_N_*}}` template block:** `plugins/contractor-brand/skills/brand/references/sub-brands.md` contains one repeatable block of `{{SUBBRAND_N_*}}` tokens (name, full name, abbreviation, scope, voice nuance, proof points, sample copy, logos). For each sub-brand the user has, duplicate the block and fill it from their answers — collect scope and 2–3 proof points per sub-brand during Section 2 if sub-brands exist.

If the user has **no sub-brands**: delete the sub-brand rows from the logo table in `plugins/contractor-brand/skills/brand/SKILL.md`, replace the body of `references/sub-brands.md` with a one-line "This company operates as a single unified brand." note, and substitute `{{SUBBRANDS}}`/`{{SUBBRAND_ROSTER}}` with the company name. If a logo file is missing, leave its token in place — the brand skill treats an unresolved `{{LOGO_*}}` token as "ask the user before rendering."

### Market & estimating

| Placeholder | Source field |
|---|---|
| `{{TARGET_REVENUE_RANGE}}` | target_revenue_range |
| `{{PROJECT_TYPES}}` | project_types (comma-joined) |
| `{{SERVICE_LINES}}` | service_lines (comma-joined) |
| `{{PM_NAME}}` | pm_name |
| `{{PM_TITLE}}` | pm_title |
| `{{PM_EMAIL}}` | pm_email |
| `{{PM_PHONE}}` | pm_phone |
| `{{DEFAULT_DIVISION}}` | default_division |
| `{{DEFAULT_CITY}}` | default_city |
| `{{MARKET_CITY}}` | default_city |
| `{{MARKET_REGION}}` | market_region |
| `{{LICENSE_SCHEME}}` | license_scheme |
| `{{OHP_PERCENT}}` | ohp_percent |
| `{{CONTINGENCY_PERCENT}}` | contingency_percent |

Use `Edit` with `replace_all: true` for each token in each file. Skip files that contain no placeholders.

**Do NOT substitute** the literal meta-tokens `{{TOKEN}}` and `{{PLACEHOLDER}}` — those are documentation examples in `contractor-docs`, not real placeholders.

---

## Verification — no token left behind

After substitution, run a final sweep:

```bash
grep -rEo '\{\{[A-Z_0-9]+\}\}' plugins --include='*.md' | grep -v 'TOKEN\|PLACEHOLDER' | sort | uniq -c
```

Expected leftovers: `{{LOGO_*}}` tokens for logo files the user hasn't provided yet (intentional), and nothing else. If anything else remains, it means a value was skipped — tell the user exactly which tokens are unresolved and which section to re-run. Do not report success while non-logo tokens remain.

---

## Final confirmation

Print a summary like:

```
✓ Company configured: Apex Construction
✓ Brand: #0A0A0A primary, Helvetica Neue, 4/5 logo variants present
✓ Voice: Approachable Expert
✓ Capabilities: 4 differentiators, 5 notable projects, bonding on file
✓ Estimating defaults: Jordan Reyes, General Contracting, Phoenix, ROC (Arizona)
✓ Updated 5 plugins — 0 unresolved tokens (1 logo pending: wordmark-stacked)

You're ready to use /estimate, /proposal, /branded-doc, and the rest of the toolkit.
Run /show-config any time to review.
If you also want these skills on claude.ai, run ./scripts/build-dist.sh NOW (after
initialization) — zips built before /initialize contain raw template tokens.
```

## Section-only re-runs

If the user passed an argument:
- `company` → Section 1, re-substitute company tokens
- `services` → Section 2, re-substitute service/sub-brand tokens
- `brand` → Sections 3 only, re-substitute color tokens
- `typography` → Section 4, re-substitute typography tokens
- `logos` → Section 5, re-substitute logo tokens
- `voice` → Section 6, re-substitute voice tokens
- `contact` → Section 7, re-substitute contact tokens
- `icp` → Section 8, re-substitute ICP tokens
- `capabilities` → Section 9, no substitution (read at runtime)
- `estimating` → Section 10, re-substitute estimating tokens

Don't touch sections that weren't requested. Keep existing values. Always finish a re-run with the verification sweep.
