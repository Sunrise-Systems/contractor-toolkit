---
name: show-config
description: Display the current contractor-toolkit configuration — company, brand, voice, contact, ICP, estimating defaults. Reads .claude/contractor.local.md.
argument-hint: ""
allowed-tools:
  - Read
  - Glob
---

# /show-config — Review Current Setup

Prints a clean, human-readable summary of what `/initialize` (and the various `/update-*` commands) have configured.

## Behavior

1. Read `.claude/contractor.local.md`. If missing, tell the user: "No config yet. Run `/initialize` to set up the toolkit."

2. Glob for `.claude/contractor-*.local.md` to confirm which per-plugin configs exist.

3. Glob `plugins/contractor-brand/skills/brand/assets/logos/` to report which logo variants are present.

4. Print a formatted summary like this:

```
Contractor Toolkit — Current Configuration
═══════════════════════════════════════════

Company
  Display name      Apex Construction
  Legal name        Apex Construction Group, LLC
  Tagline           Built right. On time.
  Founded           2014

Contact
  Registered        123 Main St, Phoenix, AZ 85001
  Operating         same
  Phone             (602) 555-0100
  Email             hello@apexbuilds.com
  Domain            apexbuilds.com

Brand
  Primary color     #0A0A0A
  Accent            (none)
  Typography        Helvetica Neue, Arial, sans-serif
  Logos             ✓ wordmark-primary  ✓ mark-only  ✓ wordmark-white  ✗ wordmark-black

Voice
  Archetype         Approachable Expert
  Signature phrases "Built right.", "On time, on budget, no surprises.", "We answer the phone."
  Banned words      synergy, world-class, cheap

Services
  Service lines     General Contracting, Design-Build
  Sub-brands        No (unified brand)

ICP
  Project types     Commercial TI, Ground-Up Commercial, Multi-Family
  Project size      $2M–$25M
  Regions           Phoenix metro, Tucson

Estimating Defaults
  PM                Jordan Reyes — Senior Project Manager
  Email             jordan@apexbuilds.com
  Phone             (602) 555-0142
  Default division  General Contracting
  Default city      Phoenix
  Hourly markup     1.5x
  OH&P              15%
  Contingency       10%

Per-plugin config files
  ✓ .claude/contractor.local.md (master)
  ✓ .claude/contractor-brand.local.md
  ✓ .claude/contractor-estimating.local.md
  ✓ .claude/contractor-docs.local.md

To change anything:
  /update-company      basics, addresses, contact
  /update-brand        colors and typography
  /update-estimating   PM and estimating defaults
  /initialize voice    re-run just the voice section
  /initialize logos    re-check logo files
  /initialize          full re-run
```

5. If any required field is empty, flag it with `⚠ not set` so the user knows what's incomplete.
