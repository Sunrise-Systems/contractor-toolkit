---
name: exclusions-excel
description: Export filtered exclusions, inclusions, and clarifications as a project-specific Excel workbook. The output subs and clients actually use to review scope boundaries. Contextual to the project's divisions only, never a raw master list dump.
argument-hint: "[project description, or leave blank to select from recent estimates]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /exclusions-excel — Filtered Exclusions/Inclusions Workbook

Export a project-filtered XLSX workbook of exclusions, inclusions, and clarifications organized by CSI division. *A raw master list freaks people out — the output needs to be contextual to the project's divisions.*

## When to Use This

- After running `/conceptual-budget` or `/formal-bid`
- When a sub or client specifically asks for an Excel scope boundary sheet
- When the PM needs to mark up exclusions during a pre-bid review
- Standalone — for any project where you want to lock the scope boundary before pricing

## Inputs Needed

- **Project type** — TI, new construction, renovation, restaurant, healthcare, etc.
- **Service line** — A&E, GC, Electrical, or combined
- **Applicable CSI divisions** — from `/conceptual-budget` output OR manually confirmed

## Pipeline

Invoke `estimating-workflow` **Phase 6** only, scoped to this project's divisions.

## Data Sources

Filter from:
- `references/exclusions-master.md` — combined exclusions library
- `references/clarifications-master.md` — combined clarifications library

**Filter rule:** Include an item only if its category/division is in this project's scope. Do NOT dump the entire master list.

## Output — XLSX + HTML Summary

Two deliverables:

1. **XLSX Workbook** (primary — this is what gets marked up and sent to subs) — file: `contractor_exclusions_[project-slug]_[YYYY-MM].xlsx`
2. **HTML Summary** (optional, for presentation) — single-page summary showing exclusion counts per division, most-flagged items, and highlights from Custom Additions. Useful for pre-bid meetings. Save as `contractor_exclusions_summary_[project-slug]_[YYYY-MM].html`.

Generated via `openpyxl`. Matches your brand aesthetic per `contractor-brand` — typically pure black + white, no color, no cell fills other than header bars.

### Workbook Structure

**Sheet 1: Summary**
| Field | Value |
|-------|-------|
| Project Name | [name] |
| Project Type | [type] |
| Service Line | [A&E / GC / Electric / Combined] |
| Date Generated | [date] |
| Divisions in Scope | [list] |
| Total Exclusions | [count] |
| Total Inclusions/Clarifications | [count] |

**Sheet 2: Exclusions by Division**
| CSI Division | Item # | Exclusion | Category | Status |
|--------------|--------|-----------|----------|--------|
| 03 - Concrete | E001 | … | General | Confirmed |
| 03 - Concrete | E002 | … | Structural | Confirmed |
| 22 - Plumbing | E015 | … | Fixtures | Confirmed |

Status column is a dropdown: `Confirmed` / `Review` / `Remove`. PM/estimator marks up before sending.

**Sheet 3: Inclusions & Clarifications by Division**
| CSI Division | Item # | Clarification | Type | Status |
|--------------|--------|---------------|------|--------|
| 09 - Finishes | I001 | … | Assumption | Confirmed |
| 09 - Finishes | I002 | … | Standard of Work | Confirmed |
| 23 - HVAC | I007 | … | Coordination | Confirmed |

Type column: `Assumption` / `Standard of Work` / `Coordination` / `Allowance`.

**Sheet 4: Custom Additions** (empty table)
| CSI Division | Item # | Description | Type | Notes |

For the PM/estimator to add project-specific exclusions/inclusions not in the master library. Additions here can be harvested back into the master library later — that's how the master library grows over time.

## Formatting Rules

- **Font:** Arial 10pt body, 11pt bold headers
- **Header row:** Black background (`#000000`), white text, bold
- **Body rows:** White background, black text, hairline `#E5E5E5` borders
- **Status/Type columns:** Data validation dropdowns
- **Column widths:** Auto-fit, max 60 characters per column
- **Freeze header row** on each sheet

## Transition

At delivery, end with:

```
Exclusions workbook ready at [path].

Review and mark up the Status column, then send to subs or attach
to the formal bid proposal. Any custom additions get harvested back
into the master exclusions library.
```
