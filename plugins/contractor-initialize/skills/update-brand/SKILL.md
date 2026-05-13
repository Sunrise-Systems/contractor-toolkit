---
name: update-brand
description: Re-run just the brand section of the contractor-toolkit setup — primary color, accent, typography. Updates .claude/contractor-brand.local.md and re-substitutes brand placeholders across sibling plugins.
argument-hint: ""
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
  - Glob
---

# /update-brand — Refresh Brand Settings

Quick way to change colors and typography without re-running the full `/initialize` wizard.

## Behavior

1. Read `.claude/contractor.local.md` and `.claude/contractor-brand.local.md`. If neither exists, tell the user to run `/initialize` first.

2. Show current brand:
   ```
   Current brand:
   • Primary: #0A0A0A
   • Accent: (none)
   • Typography: Helvetica Neue, Arial, sans-serif
   ```

3. Ask conversationally:
   - **Primary color** — hex code. Default: keep current.
   - **Accent color** — hex, or "none". Default: keep current.
   - **Typography** — Helvetica Neue / Inter / Monument Grotesk / custom. Default: keep current.

4. Update both `.claude/contractor.local.md` (frontmatter) and `.claude/contractor-brand.local.md`.

5. Re-substitute these tokens across `plugins/**/*.md`:
   - `{{PRIMARY_COLOR}}`
   - `{{ACCENT_COLOR}}`
   - `{{TYPOGRAPHY_PRIMARY}}`

   Note: token-based substitution only works on files that still have the raw `{{TOKEN}}` markers. If the user previously ran `/initialize`, those tokens were already replaced with concrete values. In that case, do a string-replace of the OLD value with the NEW value across the same file set.

6. Confirm: `✓ Brand updated. Re-run /show-config to review.`
