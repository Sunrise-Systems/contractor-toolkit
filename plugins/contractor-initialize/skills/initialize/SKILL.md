---
name: initialize
description: One-time setup wizard for contractor-toolkit. Configures company brand, voice, logos, ICP, and estimating defaults. Triggers on /initialize.
argument-hint: "[section name to re-run just one section: brand, voice, logos, contact, icp, estimating]"
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
  - Glob
  - Bash
---

# /initialize — Contractor Toolkit Setup Wizard

This is the **first thing** a new user runs. It's a conversational interview that configures every other plugin in the toolkit. After this finishes, `/estimate`, `/proposal`, `/branded-doc`, etc. will all be pre-filled with the company's brand, voice, and defaults.

## How to run this

If an argument was passed (`brand`, `voice`, `logos`, `contact`, `icp`, `estimating`), **jump straight to that section** and skip the others. Otherwise, walk all 9 sections in order.

Before starting, check whether `.claude/contractor.local.md` already exists.
- If it exists and no argument was passed: tell the user "Looks like you've already run /initialize. Want to start fresh, or re-run a specific section? (`brand`, `voice`, `logos`, `contact`, `icp`, `estimating`)" — let them choose.
- Otherwise: proceed.

## Tone

Conversational. Friendly. Not bureaucratic. One section at a time — never dump 30 questions at once. Always offer a sensible default the user can accept by saying "default" or "skip". Show progress like `Section 3 of 9 — Brand Colors`.

Use `AskUserQuestion` for genuinely multi-choice selections (service lines, voice archetype). Use plain conversational prose for everything else.

---

## Section 1 of 9 — Company Basics

> "Let's start with the basics. What's your company called?"

Ask, in a natural flow:
- **Display name** — what shows on documents (e.g., "Apex Construction")
- **Legal name with entity type** — for contracts (e.g., "Apex Construction Group, LLC")
- **Founded year** — for credibility blurbs
- **Tagline** — optional, one line (e.g., "Built right. On time.")
- **One-sentence description** — what the company does, plain English

Write to `.claude/contractor.local.md` (create if missing) under a `# Company` section.

---

## Section 2 of 9 — Services & Sub-brands

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

Then ask: **"Do you operate these as separate sub-brands (different names, logos, colors per service line), or as one unified brand?"** Most contractors are unified — that's the default.

Save to `contractor.local.md` and `.claude/contractor-brand.local.md`.

---

## Section 3 of 9 — Brand Colors

> "Let's talk colors. Got a primary brand color? Drop a hex code or describe it."

- **Primary color** — hex (e.g., `#1A1A1A`). If unsure, recommend a clean black + white + grays system: `#0A0A0A` primary, white background, gray scale neutrals. Explain this reads as premium / architectural / serious.
- **Accent color** — optional. One accent works best. Default: none.
- **Neutrals** — confirm a grayscale palette (light gray, mid gray, charcoal).

Save to `.claude/contractor-brand.local.md`.

---

## Section 4 of 9 — Typography

> "Pick a typeface. If you don't have a preference, I'll suggest something clean."

Suggestions:
- **Helvetica Neue** (fallback Arial) — safe, neutral, premium
- **Inter** — modern, web-friendly, free
- **Monument Grotesk** — architectural, distinctive
- **"I don't know — pick something clean"** → default to Helvetica Neue / Arial

Save primary font + fallback stack to `contractor-brand.local.md`.

---

## Section 5 of 9 — Logos

> "Drop your logo files into `plugins/contractor-brand/skills/brand/assets/logos/`. I'll look for these four variants:"

Checklist:
- `wordmark-primary.svg` (or .png) — main horizontal logo
- `mark-only.svg` — icon / monogram alone
- `wordmark-white.svg` — for dark backgrounds
- `wordmark-black.svg` — for light backgrounds

Glob the directory and report what's present vs. missing. If files are missing, save the checklist to `contractor-brand.local.md` and tell the user: "No worries — drop them in later and re-run `/initialize logos`."

---

## Section 6 of 9 — Voice & Tone

> "How does your company sound when it talks?"

Use `AskUserQuestion` for the archetype:
- **Approachable Expert** — warm, plain-spoken, confident
- **No-Nonsense Builder** — direct, blue-collar, no fluff
- **Visionary Advisor** — strategic, big-picture, design-forward
- **Premium Craftsman** — restrained, precise, quality-obsessed
- **Other** — let user describe

Then ask conversationally:
- **3–5 signature phrases** — taglines or sayings the company actually uses
- **Banned words** — words/phrases never to use (e.g., "synergy", "world-class", "cheap")

Save to `.claude/contractor-brand.local.md` under `# Voice`.

---

## Section 7 of 9 — Contact Info

> "Now the boring-but-important stuff."

- **Registered legal address** — for contracts (street, city, state, ZIP)
- **Operating address** — for proposals/marketing (may be same)
- **Main phone**
- **Main email**
- **Website domain** (e.g., `apexbuilds.com`)

Save to `contractor.local.md` under `# Contact`.

---

## Section 8 of 9 — ICP / Target Client

> "Who are you trying to win work from?"

- **Project type focus** — multi-select via `AskUserQuestion`: Residential, Commercial Tenant Improvement, Ground-Up Commercial, Healthcare, K-12, Higher Ed, Hospitality, Multi-Family, Industrial, Mixed-Use, Government, Other
- **Typical project size** — revenue range ($X–$Y) or sqft range
- **Typical client annual revenue** — rough band
- **Geographic regions** — cities, counties, or states served

Save to `.claude/contractor.local.md` under `# ICP`.

---

## Section 9 of 9 — Estimating Defaults

> "Last section. These pre-fill `/estimate` so you don't retype them every time."

- **Default PM name**
- **Default PM title** (e.g., "Senior Project Manager")
- **Default PM email**
- **Default PM phone**
- **Default service line for estimates** — pick one from Section 2
- **Default city/market**
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
company_legal_name: Apex Construction Group, LLC
tagline: Built right. On time.
founded_year: 2014
primary_color: "#0A0A0A"
accent_color: ""
typography_primary: "Helvetica Neue, Arial, sans-serif"
registered_address: "123 Main St, Phoenix, AZ 85001"
operating_address: "123 Main St, Phoenix, AZ 85001"
phone: "(602) 555-0100"
email: "hello@apexbuilds.com"
domain: "apexbuilds.com"
voice_archetype: "Approachable Expert"
target_revenue_range: "$2M–$25M projects"
project_types: ["Commercial TI", "Ground-Up Commercial", "Multi-Family"]
service_lines: ["General Contracting", "Design-Build"]
pm_name: "Jordan Reyes"
pm_title: "Senior Project Manager"
pm_email: "jordan@apexbuilds.com"
pm_phone: "(602) 555-0142"
default_division: "General Contracting"
default_city: "Phoenix"
ohp_percent: 15
contingency_percent: 10
---

# Apex Construction — Master Config

Last updated: 2026-05-13
```

Also write per-plugin files:
- `.claude/contractor-brand.local.md` — colors, typography, logos, voice
- `.claude/contractor-estimating.local.md` — PM, defaults, markups
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
```

For each file, do exact string substitution of these tokens:

| Placeholder | Source field |
|---|---|
| `{{COMPANY_NAME}}` | company_name |
| `{{COMPANY_LEGAL_NAME}}` | company_legal_name |
| `{{TAGLINE}}` | tagline |
| `{{FOUNDED_YEAR}}` | founded_year |
| `{{PRIMARY_COLOR}}` | primary_color |
| `{{ACCENT_COLOR}}` | accent_color |
| `{{TYPOGRAPHY_PRIMARY}}` | typography_primary |
| `{{REGISTERED_ADDRESS}}` | registered_address |
| `{{OPERATING_ADDRESS}}` | operating_address |
| `{{PHONE}}` | phone |
| `{{EMAIL}}` | email |
| `{{DOMAIN}}` | domain |
| `{{VOICE_ARCHETYPE}}` | voice_archetype |
| `{{TARGET_REVENUE_RANGE}}` | target_revenue_range |
| `{{PROJECT_TYPES}}` | project_types (comma-joined) |
| `{{SERVICE_LINES}}` | service_lines (comma-joined) |
| `{{PM_NAME}}` | pm_name |
| `{{PM_TITLE}}` | pm_title |
| `{{PM_EMAIL}}` | pm_email |
| `{{PM_PHONE}}` | pm_phone |
| `{{DEFAULT_DIVISION}}` | default_division |
| `{{DEFAULT_CITY}}` | default_city |
| `{{OHP_PERCENT}}` | ohp_percent |
| `{{CONTINGENCY_PERCENT}}` | contingency_percent |

Use `Edit` with `replace_all: true` for each token in each file. Skip files that contain no placeholders.

---

## Final confirmation

Print a summary like:

```
✓ Company configured: Apex Construction
✓ Brand: #0A0A0A primary, Helvetica Neue, 4/4 logo variants present
✓ Voice: Approachable Expert
✓ Estimating defaults: Jordan Reyes, General Contracting, Phoenix
✓ Updated 4 plugins, 12 skills

You're ready to use /estimate, /proposal, /branded-doc, and the rest of the toolkit.
Run /show-config any time to review.
```

## Section-only re-runs

If the user passed an argument:
- `brand` → Sections 3 + 4 only, then re-substitute brand tokens
- `voice` → Section 6, re-substitute voice tokens
- `logos` → Section 5, no substitution needed
- `contact` → Section 7, re-substitute contact tokens
- `icp` → Section 8, re-substitute ICP tokens
- `estimating` → Section 9, re-substitute estimating tokens

Don't touch sections that weren't requested. Keep existing values.
