---
name: rom
description: Generate a Rough Order of Magnitude (ROM) budget — Stage 1 of the 3-stage estimating workflow. Quick $/sqft ballpark for feasibility alignment before design work starts. Outputs a clean monochrome HTML ROM document.
argument-hint: "[project description, or leave blank to start interactively]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /rom — Rough Order of Magnitude Budget

Generate a Stage 1 ROM budget — the "are we in the ballpark?" deliverable that aligns client expectations before any real estimating work begins. The canonical use case: *"Hey, here's your conceptual, you're going to be at about $X per square foot. It's 10,000 square feet, you're looking at $XM on this."*

## When to Use This

- Client describes a project idea with basic parameters (type, SF, location)
- Need to answer: *is this project financially feasible before we invest design time?*
- Pre-design, pre-drawings, pre-architect
- Output is a range, never a single number — ROMs are ±25-35%

## What This Produces

**Primary: HTML ROM Budget** — visual, print-to-PDF, client-facing presentation format. Matches your company's example library (typically a black-and-white hairline-grid aesthetic via the `contractor-brand` plugin).

**Optional: DOCX ROM Budget** — text-heavy, editable, working document. Generate only if the client explicitly asks for an editable version.

Both files use the brand palette configured in `contractor-brand`. Print-ready.

The HTML is what the client sees. The DOCX is what the estimator edits when requested.

## Inputs Needed

Collect conversationally — don't interrogate:

1. **Project type** — new construction, renovation, tenant improvement, addition
2. **Building type** — commercial office, retail, restaurant, industrial, healthcare, hospitality, multi-family, SFR
3. **Square footage** — gross SF
4. **Location** — city/neighborhood (affects market multiplier and complexity factors)
5. **Service line** — A&E, GC, Electrical, Combined, or Full End-to-End (depends on `{{COMPANY_NAME}}`'s offerings)
6. **Complicating factors** — hillside, occupied-adjacent, restaurant exhaust, healthcare state-licensing, historic preservation, phased work

## Project Settings

Check for `.claude/contractor-estimating.local.md` to pre-fill PM info, default division, and default city. If not present, suggest `/setup`.

## Pipeline

Invoke the `estimating-workflow` skill but only run **Phases 1-2**:

- **Phase 1** — Plan Analysis & Division Scoping (CSI divisions applicable)
- **Phase 2** — Written Scope by Division (brief — ROM is not detailed scope)

Skip Phases 3-8. Do not do takeoff, do not price line-by-line, do not write sub bid packages.

## Cost Data Sources

Use ratios, not takeoff:
- `references/cost-reference.md` — Cost per SF by building type (customize with your historical data)
- `references/rs-means-reference.md` — Workflow for applying RS Means data
- Company historical ratios from your project archive (if available via `contractor-brand`)

## Complexity Premiums

Apply these to base SF rates when applicable:

| Factor | Premium | Notes |
|--------|---------|-------|
| Hillside / steep site | +20-30% on earthwork, foundation, concrete, framing | Hand-work, limited staging |
| Restaurant with hood/exhaust | +15-25% on MEP | Grease trap, kitchen exhaust |
| Occupied-adjacent TI | +10-15% on GC | After-hours coordination, dust control |
| Healthcare (state-licensed) | +25-40% overall | Compliance + extended timeline |
| Historic preservation | +20-30% | Preservation authority coordination, matching materials |
| Phased / live environment | +10-20% | Swing space, night work |
| Public works / prevailing wage | +30-60% on labor | Davis-Bacon or state PW rates |

## Output — HTML (Primary, Always)

The canonical ROM output is HTML.

Clone the CSS from your company's example template (provided by `contractor-brand`). Never modify the base CSS — substitute only the content blocks:

1. **Hero cover** — "Rough Order of Magnitude — Budget Estimate" tag, company wordmark, division subtitle, project title, address, 3-col meta grid (Project Type / Building Area / Date Issued)
2. **Scope of Work** — 4-6 items in flat 2-column hairline-divided grid (no decorative cards)
3. **Notice block** — if project has any complicating factor, add a callout explaining the premium
4. **Budget by CSI Division** — CSI-structured table with division header bands, scope rows, cost ranges right-aligned, subtotal row
5. **Totals block** — contingency (12-15% typical for ROM), OH&P (your standard), permits & fees, ROM Total with $/SF sublabel
6. **Assumptions & Exclusions** — hairline grid pattern (Included / Excluded / Basis of Estimate / Validity)
7. **Timeline Gantt** — phase groups with tonal bars scaled to project duration
8. **Print CTA + footer** — prepared-for / architect-of-record metadata

**Mandatory:** include `@media print { @page { margin: 0 } ... }` — without it, exported PDFs show the file URL in the margin.

Save as `contractor_rom_[project-slug]_[YYYY-MM].html` to the working directory. Tell the user to open in a browser and click the in-page **↓ Print / Save as PDF** button.

## Output — DOCX (Opt-In Only)

Generate a DOCX sibling only if the client explicitly asks for an editable version. Use the `contractor-docs` plugin's `generate_estimate()` function. Save as `contractor_rom_[project-slug]_[YYYY-MM].docx`.

Do not produce DOCX by default. HTML is the clean, signable, shareable canonical output.

## Transition to Stage 2

At delivery, end with:

```
This is a ROM — ±25-35%. Good for alignment, not for contracts.

When you have actual plans (SD, DD, or CD), run /conceptual-budget
to get a CSI-structured budget checked against master scope lists.
When you're ready for subs to bid, run /formal-bid.
```
