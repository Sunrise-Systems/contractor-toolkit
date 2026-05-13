---
name: project-timeline
description: Generate a Gantt-style construction timeline as an HTML document with tonal-gray phase bars and milestone markers. Use when the user says "build a timeline", "Gantt chart", "construction schedule", "project timeline", or "/project-timeline".
argument-hint: [project name]
---

# Project Timeline

Generate a Gantt-style construction timeline as a styled HTML document. Phase bars render in tonal grays (light gray to charcoal) so the timeline reads as a single document, not a rainbow. Milestone markers use `{{PRIMARY_COLOR}}` for emphasis.

Use this when a client or internal stakeholder needs a one-page visual of how the project flows from pre-construction to closeout.

---

## Inputs Needed

Gather in two chunks.

### 1. Project Basics
- Project name
- Project type (TI, ground-up, renovation, addition)
- Start date
- Total duration (weeks)
- Approximate square footage (helps calibrate phase lengths)

### 2. Phase Detail
- Which phases apply (skip ones that don't — e.g., no demo on ground-up greenfield)
- Any known milestone dates (permit issuance, inspection windows, client deadlines)
- Any sequencing constraints (long-lead items, owner-furnished equipment)

Default phase set (in order):
1. Pre-Construction
2. Demolition
3. Site Work
4. Foundation
5. Structure
6. MEP Rough-In
7. Finishes
8. Closeout & Punch

---

## Workflow

```
1. INTAKE     → Project basics + applicable phases
2. CALCULATE  → Distribute duration across phases based on project type
3. RENDER     → Generate HTML Gantt with tonal-gray bars
4. ANNOTATE   → Add milestone markers and percentages
5. EXPORT     → Hand to contractor-docs for HTML/PDF output
```

### Phase Duration Heuristics (% of total duration)

| Phase | TI | Ground-Up | Renovation |
|-------|----|-----------|------------|
| Pre-Con | 10% | 15% | 10% |
| Demo | 10% | 5% | 15% |
| Site | — | 15% | 5% |
| Foundation | — | 15% | — |
| Structure | 5% | 20% | 10% |
| MEP Rough | 25% | 15% | 25% |
| Finishes | 35% | 10% | 25% |
| Closeout | 15% | 5% | 10% |

Adjust based on inputs. Overlap is expected — MEP rough typically overlaps with structure tail.

---

## Output

An HTML document with:

- Header block: project name, `{{COMPANY_NAME}}`, start date, duration, total weeks
- Gantt grid: weeks on the X axis, phases on the Y axis
- Phase bars in tonal grays (`#E5E5E5`, `#C8C8C8`, `#A8A8A8`, `#888888`, `#606060`, `#404040`)
- Milestone diamonds in `{{PRIMARY_COLOR}}` at key dates
- Percentage labels at the end of each phase bar
- Footer: `{{COMPANY_NAME}}` · `{{DOMAIN}}` · prepared by `{{PM_NAME}}`

Print-friendly — fits on landscape letter or A3.

---

## Template

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{PROJECT_NAME} — Construction Timeline</title>
<style>
  body { font-family: -apple-system, "Helvetica Neue", sans-serif; margin: 40px; color: #1A1A1A; }
  .header { border-bottom: 2px solid #1A1A1A; padding-bottom: 16px; margin-bottom: 24px; }
  .header h1 { margin: 0 0 4px; font-size: 22px; }
  .header .meta { color: #606060; font-size: 12px; }
  table.gantt { width: 100%; border-collapse: collapse; font-size: 11px; }
  table.gantt th { text-align: left; padding: 6px 4px; font-weight: 500; border-bottom: 1px solid #C8C8C8; color: #606060; }
  table.gantt td { padding: 8px 0; vertical-align: middle; }
  td.phase-label { width: 180px; font-weight: 500; padding-right: 12px; }
  td.bar-cell { position: relative; height: 22px; background: linear-gradient(to right, #F5F5F5 0, #F5F5F5 100%); }
  .bar { position: absolute; height: 18px; top: 2px; border-radius: 2px; display: flex; align-items: center; justify-content: flex-end; padding-right: 6px; color: #FFF; font-size: 10px; }
  .milestone { position: absolute; top: -4px; width: 12px; height: 12px; transform: rotate(45deg); background: {{PRIMARY_COLOR}}; border: 1px solid #1A1A1A; }
  .footer { margin-top: 32px; font-size: 10px; color: #888; border-top: 1px solid #C8C8C8; padding-top: 12px; }
</style>
</head>
<body>
  <div class="header">
    <h1>{PROJECT_NAME} — Construction Timeline</h1>
    <div class="meta">{{COMPANY_NAME}} · Start: {START_DATE} · Duration: {WEEKS} weeks · Prepared {DATE}</div>
  </div>

  <table class="gantt">
    <thead>
      <tr>
        <th>Phase</th>
        <th colspan="{WEEKS}">Weeks 1 – {WEEKS}</th>
      </tr>
    </thead>
    <tbody>
      <!-- One row per phase. Bar left/width set as % of total weeks. Background shade steps darker each phase. -->
      <tr>
        <td class="phase-label">Pre-Construction</td>
        <td class="bar-cell"><div class="bar" style="left:0%; width:{PCT}%; background:#E5E5E5; color:#1A1A1A;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">Demolition</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#C8C8C8; color:#1A1A1A;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">Site Work</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#A8A8A8;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">Foundation</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#888888;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">Structure</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#707070;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">MEP Rough-In</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#585858;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">Finishes</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#404040;">{PCT}%</div></td>
      </tr>
      <tr>
        <td class="phase-label">Closeout & Punch</td>
        <td class="bar-cell"><div class="bar" style="left:{L}%; width:{W}%; background:#2A2A2A;">{PCT}%</div></td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    {{COMPANY_NAME}} · {{DOMAIN}} · Prepared by {{PM_NAME}}, {{PM_TITLE}}
  </div>
</body>
</html>
```

Hand the rendered HTML to `contractor-docs` for final styling and PDF export if requested.
