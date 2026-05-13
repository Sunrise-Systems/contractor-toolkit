---
name: update-company
description: Update basic company info in the contractor-toolkit setup — display name, legal name, tagline, founded year, addresses, phone, email, domain. Updates .claude/contractor.local.md.
argument-hint: ""
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# /update-company — Refresh Company Info

Use this when something basic changes — you renamed, moved, changed phone numbers, registered a new entity, picked up a new domain.

## Behavior

1. Read `.claude/contractor.local.md`. If missing, route the user to `/initialize`.

2. Show current values:
   ```
   Current company info:
   • Display name: Apex Construction
   • Legal name: Apex Construction Group, LLC
   • Tagline: Built right. On time.
   • Founded: 2014
   • Registered address: 123 Main St, Phoenix, AZ 85001
   • Operating address: same
   • Phone: (602) 555-0100
   • Email: hello@apexbuilds.com
   • Domain: apexbuilds.com
   ```

3. Ask conversationally which fields they want to change. For each, accept "skip" / "default" to keep current.

4. Update `.claude/contractor.local.md` frontmatter and `.claude/contractor-docs.local.md`.

5. Re-substitute (or old→new string replace) across all `plugins/**/*.md`:
   - `{{COMPANY_NAME}}`, `{{COMPANY_LEGAL_NAME}}`, `{{TAGLINE}}`, `{{FOUNDED_YEAR}}`
   - `{{REGISTERED_ADDRESS}}`, `{{OPERATING_ADDRESS}}`
   - `{{PHONE}}`, `{{EMAIL}}`, `{{DOMAIN}}`

6. Confirm: `✓ Company info updated. Run /show-config to review.`
