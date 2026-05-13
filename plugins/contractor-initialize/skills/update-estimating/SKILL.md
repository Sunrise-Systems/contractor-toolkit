---
name: update-estimating
description: Re-run just the estimating-defaults section of the contractor-toolkit setup — PM contact, default service line, default city, markups. Updates .claude/contractor-estimating.local.md.
argument-hint: ""
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# /update-estimating — Refresh Estimating Defaults

Update the values that pre-fill `/estimate` without touching the rest of the config.

## Behavior

1. Read `.claude/contractor-estimating.local.md`. If missing, tell the user to run `/initialize` first.

2. Show current values:
   ```
   Current estimating defaults:
   • PM: Jordan Reyes — Senior Project Manager
   • Email: jordan@apexbuilds.com
   • Phone: (602) 555-0142
   • Default service line: General Contracting
   • Default city: Phoenix
   • OH&P: 15%
   • Contingency: 10%
   ```

3. Ask conversationally — group naturally:
   - **PM info** — name, title, email, phone (default: keep current)
   - **Default service line** — pick from the company's configured service lines
   - **Default city/market**
   - **Markups** — hourly markup, OH&P %, contingency %

4. Write the updated `.claude/contractor-estimating.local.md` and mirror the values into `.claude/contractor.local.md` frontmatter.

5. Re-substitute these tokens (or old→new string replace) across `plugins/contractor-estimating/**/*.md` and `plugins/contractor-docs/**/*.md`:
   - `{{PM_NAME}}`, `{{PM_TITLE}}`, `{{PM_EMAIL}}`, `{{PM_PHONE}}`
   - `{{DEFAULT_DIVISION}}`, `{{DEFAULT_CITY}}`
   - `{{OHP_PERCENT}}`, `{{CONTINGENCY_PERCENT}}`

6. Confirm: `✓ Estimating defaults updated. /estimate will now use these.`
