---
name: lookahead
description: Generate a 3-week look-ahead schedule — activities by trade and week, with constraints, deliveries, inspections, and blockers that need clearing. Use when the user says "look-ahead", "three week schedule", "what's coming up on site", or "/lookahead".
argument-hint: [project name]
---

# Look-Ahead Schedule

Generate the rolling 3-week look-ahead the super runs the job from — what's happening, who's on site, and what has to be cleared *now* for week 3 to happen at all. One page, HTML primary (tonal-gray bars matching `/project-timeline`), DOCX on request.

Use weekly, typically after the OAC or foreman's meeting. The master timeline says where the project should be; the look-ahead says what the field does about it.

## Inputs Needed

1. **Project + week-of date**
2. **Current activities** — from the master timeline (`/project-timeline` output if present), recent `/daily-log` entries in the working directory, or dictated by the super
3. **Constraints** — open RFIs (pull ball-in-court items from `/rfi-log` if present), pending submittals, material lead times, inspection scheduling, weather risk

## Structure

```
WEEK 1 (Jun 15–19) — committed work
──────────────────────────────────────────────────────────────
Trade          Activity                          Area      Crew
──────────────────────────────────────────────────────────────
Drywall        Hang + tape Level 2 north         L2-N      4
HVAC           Set RTU-2, start distribution     Roof/L2   3
Electrical     Rough-in Suite 210                L2        2
──────────────────────────────────────────────────────────────

WEEK 2 — planned        WEEK 3 — forecast
[same format]           [same format]

CONSTRAINTS — clear these or week 3 slips
──────────────────────────────────────────────────────────────
☐ RFI-014 (storefront head detail) — ball in court: Architect, 6 days old
☐ Light fixture delivery — confirm ship date, need on site by Jun 24
☐ Rough electrical inspection — schedule for Jun 19
──────────────────────────────────────────────────────────────
```

Week 1 is commitments, week 2 is plans, week 3 is forecast — label them as such. The constraints block is the most important section: every week-2/3 activity with an unmet precondition gets a constraint line with an owner and a needed-by date.

## Outputs

- **HTML one-pager** — `{company-slug}_lookahead_{project-slug}_{week-of}.html`, print-ready for the job trailer wall
- Carry-over flagging: when re-run weekly, items that were "week 1 committed" last week and didn't happen get called out — that's the schedule slipping in real time

## Rules

1. **Constraints have owners and dates.** "Waiting on fixtures" is a worry; "confirm fixture ship date with vendor by Wed, need on site Jun 24" is a look-ahead line.
2. **Don't restate the master schedule.** This is the field-level slice, by crew and area.
3. **Carry-overs are findings.** Two consecutive carry-overs of the same activity = escalate to the PM in the document.
