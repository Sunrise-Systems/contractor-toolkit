---
name: conceptual-budget
description: Generate a Stage 2 Conceptual Budget — CSI-structured budget from actual plans, cross-checked against master exclusions/inclusions per discipline. Flags scope gaps proactively. Outputs HTML budget + Excel exclusions sheet.
argument-hint: "[project description with plan set, or leave blank to start interactively]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /conceptual-budget — Stage 2 Conceptual Budget

Generate a structured conceptual budget from an actual plan set (SD, DD, or CD). The bridge between ROM alignment and formal bidding — the client has plans, you have scope, you need a defensible budget that's been scope-checked against master discipline checklists.

The canonical use case: *"Scope the project per CSI division and discipline, check against cost books, and produce a structured budget broken out by division. Act as a scope checker — catch things like: 'Did you forget the emergency power because this is a hospital? You need a generator.'"*

## When to Use This

- Plans exist (SD, DD, or CD phase)
- Client has agreed the ROM is in the ballpark, now wants a real budget
- Still pre-formal-bid, pre-sub-pricing
- Output is still a range, but tighter than ROM — ±10-20%

## What This Produces

**HTML + XLSX — always.** DOCX is opt-in only.

1. **Conceptual Budget HTML (primary)** — Same structure as ROM but with:
   - Cover tag updated to "Conceptual Budget"
   - Expanded Scope of Work section (6-10 scope items)
   - Expanded CSI table with sub-items per division and narrower cost ranges
   - New section: **Scope Check Findings** — after totals, hairline grid listing gaps flagged by severity (Critical / High / Medium / Low)
   - Detailed Assumptions & Exclusions grid
   - Week-by-week Gantt (CD phase) or month-by-month (SD/DD)
   - **Mandatory:** `@page { margin: 0 }` print CSS block

   Save as `contractor_conceptual_budget_[project-slug]_[YYYY-MM].html`.

2. **Excel exclusions/inclusions workbook** — Per-discipline, filtered to this project's divisions. A raw master list freaks people out — the output needs to be contextual to the project's divisions. Save as `contractor_exclusions_[project-slug]_[YYYY-MM].xlsx`.

3. **DOCX (opt-in only)** — Generate via `contractor-docs` only if the client explicitly requests an editable version. Save as `contractor_conceptual_budget_[project-slug]_[YYYY-MM].docx`.

## Inputs Needed

Same as ROM, plus:
- **Plan set** — drawing files or descriptions (SD / DD / CD)
- **Design phase** — determines contingency band
- **Scope narrative** — any written scope from the architect
- **Known constraints** — site conditions, client requirements, schedule drivers

## Pipeline

Invoke the `estimating-workflow` skill for **Phases 1-5** with scope-check emphasis:

- **Phase 1** — Plan Analysis & Division Scoping
- **Phase 2** — Written Scope by Division — **FULL detail, not ROM brief**
- **Phase 3** — Sub Identification & Trade Mapping
- **Phase 4** — Quantity Takeoff (from plans if available, ratios if not)
- **Phase 5** — Hard Cost Estimation (with show-your-math reasoning)

Skip Phases 6-8 (formal exclusions list, sub bid packages, formal proposal generation). Those come in `/formal-bid`.

## Scope Check — The Value-Add

For each applicable discipline, cross-reference against master checklists and call out gaps:

**Process:**
1. Read `references/clarifications-master.md` and `references/exclusions-master.md`
2. Filter to CSI divisions applicable to this project
3. For each filtered item, ask: *is this explicitly addressed in the plan set?*
4. If not addressed, flag as a **scope gap** in the output

**Flag categories:**
- **Missing discipline** — e.g., hospital needs generator, no emergency power on plans
- **Missing clarification** — e.g., plans show HVAC but no specs/capacity
- **Missing coordination** — e.g., MEP sections don't show coordination with structural
- **Missing allowance** — e.g., owner-furnished items not called out
- **Code gap** — e.g., seismic detailing absent for essential service building

## Cost Data Sources

- `references/rs-means-reference.md` — Unit cost workflow with local market multiplier
- `references/cost-reference.md` — SF benchmarks for sanity check
- `references/fee-reference.md` — A&E fee buildup if combined scope
- Your company's historical ratios via `contractor-brand` examples folder

## Outputs

### 1. Conceptual Budget HTML

Structure expanded from ROM:

1. Hero cover — "Conceptual Budget" tag
2. Scope of Work — full scope grid (6-10 cards)
3. Notice block — scope-check findings summary (how many gaps, categorized)
4. Budget by CSI Division — detailed table with sub-line items, quantities + unit rates, narrower cost ranges
5. **NEW: Scope Check section** — bulleted list of flagged gaps per discipline with severity
6. Totals block — tighter contingency (10-15% at DD, 5-10% at CD)
7. Assumptions & Exclusions — detailed grid
8. Timeline Gantt — week-by-week (CD) or month-by-month (SD/DD)
9. Print CTA + footer

File: `contractor_conceptual_budget_[project-slug]_[YYYY-MM].html`

### 2. Excel Exclusions Workbook

Per-discipline filtered exclusions/inclusions as XLSX.

**Workbook structure:**
- Sheet 1: **Summary** — project info, disciplines in scope, total exclusion count, total inclusion/clarification count
- Sheet 2: **Exclusions by Division** — CSI division | Item # | Exclusion description | Category
- Sheet 3: **Inclusions & Clarifications by Division** — CSI division | Item # | Clarification | Type (Assumption / Standard of Work / Coordination)
- Sheet 4: **Scope Check Findings** — Severity | Discipline | Finding | Recommended action

Generated via `openpyxl`. File: `contractor_exclusions_[project-slug]_[YYYY-MM].xlsx`.

## Transition to Stage 3

At delivery, end with:

```
Conceptual Budget delivered with [N] scope-check findings flagged.

Review the findings, coordinate with the architect/engineer to close
any gaps, then run /formal-bid when you're ready to send packages
to subcontractors for pricing.
```
