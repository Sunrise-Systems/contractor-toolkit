---
name: rfi-log
description: Maintain the project RFI register — append new RFIs, update statuses and responses, track ball-in-court and aging, and report cost/schedule impacts. Use when the user says "RFI log", "update the RFI register", "what RFIs are open", or "/rfi-log".
argument-hint: [project name]
---

# RFI Log

Maintain a per-project RFI register as an XLSX workbook. Single RFIs come from `/rfi`; this skill is the running record — numbering, status, ball-in-court, aging, and impact tracking. Re-run it to append, update, or report.

The register is the document that wins delay arguments: "RFI-014 sat with the architect for 19 days" only works if the log shows it.

## The Register

One XLSX per project: `{company-slug}_rfi-log_{project-slug}.xlsx`. Columns:

| Column | Notes |
|---|---|
| RFI # | Sequential, never reused. Next number = max existing + 1 |
| Subject | One line |
| Date Submitted | |
| Submitted By | |
| Directed To | Architect / Owner / Engineer |
| Drawing / Spec Ref | |
| Status | Open / Answered / Closed / Void |
| Ball In Court | Who owes the next action — the column the weekly meeting runs on |
| Date Answered | |
| Days Open | Formula: today − submitted (frozen at answer date once answered) |
| Cost Impact | None / TBD / $ amount → feeds `/change-order` |
| Schedule Impact | None / TBD / days → feeds `/lookahead` constraints |
| CO Ref | Change order number if the answer triggered one |
| Response Summary | One line |

## Operations

- **Append** — when `/rfi` generates a new RFI (or the user reports one sent), add a row with the next number. If `/rfi` runs while a log exists in the working directory, it should get its number from here.
- **Update** — record answers, flip statuses, set impacts. An answer with cost impact prompts: "Draft the change order? (`/change-order`)"
- **Report** — generate an HTML summary on request: open RFIs by ball-in-court, aging buckets (0–7 / 8–14 / 15+ days), items with unresolved cost/schedule impact, average response time. The 15+ bucket is the escalation list.

## Process

1. Glob the working directory for an existing register; create it (openpyxl) if absent
2. Apply the requested operation(s)
3. Confirm what changed: "RFI-016 added. 5 open — 3 with the architect, oldest is 11 days."

## Rules

1. **Numbers are sacred.** Never renumber, never reuse a voided number.
2. **Every open RFI has a ball-in-court.** "Open" without an owner is how RFIs die quietly.
3. **TBD impacts get chased.** Any RFI answered >7 days ago with impact still TBD shows up in every report until resolved.
4. **The log is the source of truth for `/lookahead`** — open RFIs blocking scheduled work surface there automatically.
