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

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** Selected-section answers, all four existing local configs, and exact template occurrence contexts.
- **Output:** Approved exact config/template edits, verified backups, and readback record.
- **AI role:** Stage answers and per-file/context patches; validate and apply only approved edits. Preserve unrequested fields and existing user edits.
- **Human role:** Company administrator reviews the diff, target root, and backup location.
- **Risk:** Reversible local update; no publishing or external writes.
- **Checkpoint:** User-approved local directory outside package inputs; change plan, before-images/absent records, after hashes, and receipt.
- **Approval boundary:** Explicit confirmation bound to the plan digest before any live write. Cancellation changes no targets. Ambiguous legacy replacements stop for per-file/context review.
- **Verifier:** Run `python3 "$GUARD" check-change --plan "$PLAN" --root "$ROOT"`, then `python3 "$GUARD" snapshot --plan "$PLAN" --checkpoint-dir "$CHECKPOINT"`; recheck before hashes immediately before edits. Reopen every changed file and run `python3 "$GUARD" verify-change --plan "$PLAN" --checkpoint-dir "$CHECKPOINT"`.
- **Failure:** Stop as `needs_human`; preserve backups and report conflicts. Resume classifies before/approved-after/conflict; recovery requires preview and approval, never overwrite concurrent edits.



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

Stage for `.claude/contractor.local.md` (record absent state if missing) under a `# Company` section.

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

Stage for `contractor.local.md` and `.claude/contractor-brand.local.md`.

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

Stage for `.claude/contractor-brand.local.md`.

---

## Section 4 of 10 — Typography

> "Pick a typeface. If you don't have a preference, I'll suggest something clean."

Suggestions:
- **Helvetica Neue** (fallback Arial) — safe, neutral, premium
- **Inter** — modern, web-friendly, free
- **Monument Grotesk** — architectural, distinctive
- **"I don't know — pick something clean"** → default to Helvetica Neue / Arial

Store both `typography_primary` (e.g., `Helvetica Neue`) and `typography_fallback` (the CSS fallback stack, e.g., `Helvetica, Arial, sans-serif`).

Stage for `contractor-brand.local.md`.

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

Glob the directory and report what's present vs. missing. Record the actual filenames found — they populate the `{{LOGO_*}}` tokens during substitution. If files are missing, stage the checklist for `contractor-brand.local.md` and tell the user: "No worries — drop them in later and re-run `/initialize logos`." Until then, the `{{LOGO_*}}` tokens stay unsubstituted on purpose — the brand skill is instructed to stop and ask rather than improvise a missing logo.

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

Stage for `.claude/contractor-brand.local.md` under `# Voice`.

---

## Section 7 of 10 — Contact Info

> "Now the boring-but-important stuff."

- **Registered legal address** — for contracts (street, city, state, ZIP)
- **Operating address** — for proposals/marketing (may be same)
- **Main phone**
- **Main email**
- **Website domain** (e.g., `apexbuilds.com`)

Stage for `contractor.local.md` under `# Contact`.

---

## Section 8 of 10 — ICP / Target Client

> "Who are you trying to win work from?"

- **Project type focus** — multi-select via `AskUserQuestion`: Residential, Commercial Tenant Improvement, Ground-Up Commercial, Healthcare, K-12, Higher Ed, Hospitality, Multi-Family, Industrial, Mixed-Use, Government, Other
- **Typical project size** — revenue range ($X–$Y) or sqft range
- **Typical client annual revenue** — rough band
- **Geographic regions** — cities, counties, or states served

Stage for `.claude/contractor.local.md` under `# ICP`.

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

Stage for `.claude/contractor.local.md` under `# Capabilities`. Skills read this section at runtime — it is not token-substituted.

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

Stage for `.claude/contractor-estimating.local.md`.

---

## Stage config and token mapping

Read `references/config-and-token-map.md` after collecting the selected answers. It specifies config shapes and token mappings; every change still requires the safety gate above.

## Verification and confirmation

Use the safety contract's snapshot and exact after-image/parsed-field readback, not a token sweep alone. Report only measured results: selected sections, changed paths, checkpoint, receipt, unresolved tokens and next action. Missing logos remain a blocker for affected final documents and release packages unless a no-logo design is explicitly approved. Do not print a canned success message or fabricate counts. Build release packages only after independent release validation passes.

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

Don't touch sections that weren't requested. Keep existing values. Always finish a re-run with exact after-image/parsed-field readback and the safety-contract receipt.
