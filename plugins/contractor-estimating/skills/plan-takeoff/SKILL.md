---
name: plan-takeoff
description: Read an uploaded plan set PDF and draft a quantity takeoff schedule by CSI division — areas, counts, linear measures, with a confidence rating per quantity. Feeds Phase 4 of the estimating pipeline. Triggers on "take off these plans", "quantities from the drawings", "plan takeoff", or "/plan-takeoff".
argument-hint: "[path to plan set PDF, or leave blank to be prompted]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
  - Glob
---

# /plan-takeoff — Quantity Takeoff from Drawings

Read a plan set PDF and produce a draft quantity takeoff schedule, division by division. This replaces the "describe the project and I'll use ratios" path in Phase 4 with quantities pulled from the actual drawings — clearly marked by how they were derived.

**Honest accuracy framing:** reading drawings as images yields counts and area reasoning, not scaled measurement. Every quantity carries a confidence rating, and anything that needs true scaling gets flagged for the estimator to verify. This is a draft takeoff that saves hours — not a replacement for a measured takeoff on bid-day numbers.

## Inputs Needed

1. **Plan set PDF** — path to the file. Read it page-by-page (use the `pages` parameter; 20 pages per pass on large sets).
2. **Design phase** — SD / DD / CD (affects how much can be trusted)
3. **Which divisions to take off** — default: all applicable divisions from Phase 1 if the pipeline is running; otherwise ask

## Process

### 1. Index the set
First pass: identify each sheet — number, title, discipline (A/S/M/E/P/FP/C), scale noted in the title block. Build a sheet index. Report any disciplines missing from the set (no M sheets = HVAC quantities will be ratio-based — say so).

### 2. Extract per discipline
Work through sheets in discipline order:
- **Architectural** — floor areas by room/zone (from area tables or room schedules when present — prefer stated numbers over visual estimates), door/window counts from schedules, wall types and approximate partition runs, finish schedules, ceiling types
- **Structural** — foundation type, framing system, notable members; counts from schedules
- **MEP** — fixture counts (plumbing schedule), equipment schedules (RTUs, panels, fixtures), sprinkler density from FP notes
- **Civil/Site** — paving areas, utility connections noted

**Schedules and legends are gold** — a door schedule beats counting door swings. Always check for schedule sheets before counting symbols.

### 3. Rate every quantity

| Rating | Meaning | Source |
|---|---|---|
| **A — Stated** | Read directly from a schedule, area table, or note | Use as-is |
| **B — Counted** | Counted symbols/fixtures off the drawing | Spot-check recommended |
| **C — Derived** | Computed from stated areas + standard ratios | Verify before bid |
| **D — Assumed** | No drawing basis; building-type ratio | Replace with measurement |

### 4. Output the takeoff schedule
Standard Phase 4 format, with source and rating columns added:

```
DIVISION 09 — FINISHES                              Sheets: A2.1, A6.0, A6.1
─────────────────────────────────────────────────────────────────────────────
Item                      Qty     Unit   Rating  Source
─────────────────────────────────────────────────────────────────────────────
Partition walls (Type 2)  1,140   LF     B       Counted, A2.1 floor plan
5/8" Type X drywall       9,120   SF     C       Derived: 1,140 LF × 8' both sides
ACT ceiling               3,420   SF     A       Stated, A6.0 RCP area table
Doors                     14      EA     A       Door schedule, A6.1
─────────────────────────────────────────────────────────────────────────────
```

Close with a **verification list**: every C/D quantity plus anything that genuinely needs scaled measurement, ordered by cost impact.

## Outputs

- **Takeoff schedule** — inline for pipeline use, plus optional XLSX (`contractor_takeoff_[project-slug]_[YYYY-MM].xlsx`) with one tab per division
- Feeds directly into Phase 5 pricing — ratings carry through so pricing confidence is visible

## Rules

1. **Never present a D-rated quantity without saying it's assumed.** False precision in a takeoff becomes a real dollar dispute later.
2. **Prefer schedules over symbol-counting**, and say which sheet each number came from — the estimator must be able to check your work in seconds.
3. **Missing disciplines are findings.** "No mechanical sheets in this set" changes the contingency conversation.
4. **Large sets:** index first, then take off only the divisions that matter — don't burn the session reading 40 detail sheets for a TI.
