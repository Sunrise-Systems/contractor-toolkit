---
name: setup
description: Configure contractor-estimating defaults for this project — PM contact info, default division, company, and city. Saves to .claude/contractor-estimating.local.md so /estimate pre-fills your info.
argument-hint: "[reset — to overwrite existing settings]"
allowed-tools:
  - Read
  - Write
---

# /setup — Configure Contractor Estimating

Set up project defaults for the estimating workflow. Creates `.claude/contractor-estimating.local.md` which pre-fills PM contact info, default division, and company details so they don't need to be re-entered on each estimate.

## Behavior

1. Check if `.claude/contractor-estimating.local.md` already exists
   - If it exists and the user did not pass `reset`: show current settings and ask if they want to update
   - If it does not exist (or user passed `reset`): proceed to gather settings

2. Ask conversationally — group related questions:

   **PM / Estimator Info:**
   - Name (e.g., "Aaron Torres")
   - Title (e.g., "Senior Project Manager", "Estimator", "Principal")
   - Email
   - Phone

   **Default Division:**
   Which service line does this project typically use? Options depend on what your company offers:
   - General Contracting (GC)
   - Architecture & Engineering (A&E)
   - Electrical
   - Combined (A&E + GC)
   - Full End-to-End

   **Project Location:**
   - Default city/neighborhood (e.g., "Los Angeles", "Austin", "Brooklyn")
   - Default region (e.g., "Southern California", "Central Texas", "NYC Metro")
   - Affects labor rates, permitting context, escalation

   **Company / Client Info:**
   - Default "from" company — the issuing legal entity (e.g., "{{COMPANY_NAME}}, Inc.")
   - Any recurring client name to pre-fill? (optional)

3. Write the settings file at `.claude/contractor-estimating.local.md`

4. Confirm: "Settings saved. Every time you run `/estimate`, I'll pre-fill your info and use these defaults. You can always override during the estimate."

## Settings File Format

```markdown
---
enabled: true
pm_name: [name]
pm_title: [title]
pm_email: [email]
pm_phone: [phone]
default_division: [General Contracting | Architecture & Engineering | Electrical | Combined | Full End-to-End]
default_city: [city]
market_region: [region]
issuing_company: [legal entity name]
---

# Contractor Estimating — Project Configuration

Defaults pre-configured for [pm_name]. Override any value during the estimate.

Last updated: [date]
```

## Notes

- This file is gitignored (`.claude/*.local.md`) — specific to your local setup
- Settings apply to all `/estimate` runs in this project
- Run `/setup reset` to overwrite existing settings
- For company-wide identity (name, divisions, palette, voice), install the `contractor-brand` plugin alongside this one
