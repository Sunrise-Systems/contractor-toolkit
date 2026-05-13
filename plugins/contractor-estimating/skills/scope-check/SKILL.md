---
name: scope-check
description: Cross-reference a project's plans against master exclusions/inclusions/clarifications by discipline to flag scope gaps BEFORE pricing. Outputs a scope check report identifying missing disciplines, clarifications, coordination items, and allowances.
argument-hint: "[project description with plan set]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /scope-check — Scope Gap Analysis

Run a scope check against master discipline checklists to flag gaps in the plan set BEFORE pricing begins. Acts as a second set of eyes — catching things like *"Did you forget the emergency power because this is a hospital? You need a generator."*

## When to Use This

- Plans are in hand (any design phase)
- Before running `/conceptual-budget` or `/formal-bid`
- Whenever the PM or estimator wants a second set of eyes on a plan set
- Can run standalone OR as a sub-step of `/conceptual-budget`

## What This Produces

A **Scope Check Report** (HTML primary) organized by discipline with severity-ranked findings.

## Inputs Needed

- **Plan set or scope description** — the more detail, the more thorough the check
- **Project type** — commercial TI, residential, healthcare, etc. — determines which master checklists apply
- **Design phase** — SD / DD / CD (determines severity threshold for findings)
- **Known constraints** — anything the architect has called out as TBD or owner-furnished

## Process

1. **Identify applicable CSI divisions** using `references/csi-divisions.md`
2. **Load master checklists** filtered to those divisions:
   - `references/clarifications-master.md`
   - `references/exclusions-master.md`
3. **For each checklist item**, ask: *is this explicitly addressed in the plan set or scope narrative?*
4. **Categorize each gap** by severity:
   - **Critical** — missing discipline or code requirement that will stop the project
   - **High** — missing clarification that will cause sub pricing variance
   - **Medium** — missing coordination item that will cause field RFIs
   - **Low** — missing allowance or owner-furnished call-out

## Common Scope Check Patterns

**Healthcare projects:**
- Emergency power / generator sized for life-safety loads
- State hospital-authority compliance package
- Medical gas scope
- Seismic anchoring of equipment
- Infection control measures during construction

**Restaurants:**
- Type I kitchen hood + make-up air
- Grease trap/interceptor
- Grease duct shaft enclosure
- Walk-in cooler condensate line routing
- FOG (fats/oils/grease) management

**Hillside / steep-site projects:**
- Geotech investigation referenced
- Shoring plan for adjacent improvements
- Stormwater management plan
- Haul route permit
- Retaining wall drainage

**Occupied-adjacent TI:**
- After-hours work plan
- Dust/noise/vibration protection
- Tenant notification schedule
- Life-safety pathways during construction
- Coordination with building ownership

**Historic preservation:**
- Preservation authority coordination scope
- Matching-material specifications
- Historical fabric protection plan
- Tax credit / preservation incentive compliance if applicable

## Output — HTML Scope Check Report

Clone the CSS from your company's example template via `contractor-brand`. Substitute content:

1. **Hero cover** — tag "Scope Check Report — Plan Gap Analysis", company wordmark, project title, address, 3-col meta (Design Phase / Disciplines Reviewed / Date Issued)
2. **Summary stats** — uppercase section label "Findings Summary" + 4-col info strip (Total / Critical / High / Medium-Low)
3. **Findings by discipline** — one CSI-style table per discipline group. Division header row, then finding rows with columns: Severity | Finding | Recommended Action. Severity uses text only (CRITICAL / HIGH / MEDIUM / LOW), no color.
4. **Assumptions** — flat hairline grid listing what the check covered and what it did not
5. **Footer** — prepared-by estimator, reviewed-by PM

**Mandatory:** include the `@page { margin: 0 }` print CSS block.

Save as `contractor_scope_check_[project-slug]_[YYYY-MM].html`. DOCX output is NOT produced — scope checks are reviewed digitally.

## Transition

At delivery, end with:

```
Scope check complete — [N] findings flagged ([X] critical, [Y] high,
[Z] medium, [W] low).

Close critical/high findings with the architect before running
/conceptual-budget. Medium/low findings can be flagged as assumptions
in the budget and closed during CD phase.
```
