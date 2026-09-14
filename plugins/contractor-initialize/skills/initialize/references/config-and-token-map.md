# Staged configuration and token map

These are proposed after-images only. Do not mutate live files before the parent skill safety gate.

## After all sections — Stage proposed config files

Master file `.claude/contractor.local.md` should have YAML frontmatter with every value, plus a human-readable summary below. Example shape:

```markdown
---
company_name: Apex Construction
company_short: Apex
company_legal_name: Apex Construction Group, LLC
company_type: general contractor
ownership_type: family-owned
tagline: Built right. On time.
founded_year: 2014
years_experience: "12+ years"
core_belief: "A building is only as good as the relationships that built it."
primary_color: "#0A0A0A"
accent_color: ""
ink_hex: "1A1A1A"
body_hex: "2B2B2B"
mid_hex: "555555"
muted_hex: "888888"
light_hex: "BBBBBB"
rule_hex: "DDDDDD"
soft_fill_hex: "F7F7F5"
typography_primary: "Helvetica Neue"
typography_fallback: "Helvetica, Arial, sans-serif"
registered_address: "123 Main St, Phoenix, AZ 85001"
operating_address: "123 Main St, Phoenix, AZ 85001"
phone: "(602) 555-0100"
email: "hello@apexbuilds.com"
domain: "apexbuilds.com"
voice_archetype: "Approachable Expert"
target_revenue_range: "$2M–$25M projects"
project_types: ["Commercial TI", "Ground-Up Commercial", "Multi-Family"]
service_lines: ["General Contracting", "Design-Build"]
self_perform: ["supervision", "rough carpentry", "drywall", "painting"]
pm_name: "Jordan Reyes"
pm_title: "Senior Project Manager"
pm_email: "jordan@apexbuilds.com"
pm_phone: "(602) 555-0142"
default_division: "General Contracting"
default_city: "Phoenix"
market_region: "Greater Phoenix"
license_scheme: "ROC (Arizona)"
ohp_percent: 15
contingency_percent: 10
---

# Apex Construction — Master Config

Last updated: [today's date]

## Capabilities
[differentiators, notable projects, certifications, bonding, key personnel, safety record — prose/list form]
```

Also stage proposed per-plugin files:
- `.claude/contractor-brand.local.md` — colors, tonal scale, typography, logos, voice
- `.claude/contractor-estimating.local.md` — PM, defaults, markups, license scheme
- `.claude/contractor-docs.local.md` — company, contact, domain (for document headers/footers)

---

## Template substitution — apply the config across plugins

Before live writes, inventory candidate SKILL.md/support files in existing sibling plugins and stage selected-section token patches in the change plan. Only approved paths/contexts/counts may change.

Use `Glob` to find candidates:
```
plugins/contractor-brand/**/*.md
plugins/contractor-docs/**/*.md
plugins/contractor-estimating/**/*.md
plugins/contractor-extras/**/*.md
plugins/contractor-subs/**/*.md
```

Use the following mapping to stage exact per-file/context patches; this is not permission to change every occurrence:

### Company & contact

| Placeholder | Source field |
|---|---|
| `{{COMPANY_NAME}}` | company_name |
| `{{COMPANY_SHORT}}` | company_short |
| `{{COMPANY_LEGAL_NAME}}` | company_legal_name |
| `{{COMPANY_TYPE}}` | company_type |
| `{{OWNERSHIP_TYPE}}` | ownership_type |
| `{{TAGLINE}}` | tagline |
| `{{FOUNDED_YEAR}}` | founded_year |
| `{{YEARS_EXPERIENCE}}` | years_experience |
| `{{CORE_BELIEF}}` | core_belief |
| `{{REGISTERED_ADDRESS}}` | registered_address |
| `{{OPERATING_ADDRESS}}` | operating_address |
| `{{PHONE}}` | phone |
| `{{EMAIL}}` | email |
| `{{DOMAIN}}` | domain |

### Brand & typography

| Placeholder | Source field |
|---|---|
| `{{PRIMARY_COLOR}}` | primary_color (with `#`) |
| `{{ACCENT_COLOR}}` | accent_color (with `#`, or empty) |
| `{{INK_HEX}}` | ink_hex (no `#`) |
| `{{BODY_HEX}}` | body_hex (no `#`) |
| `{{MID_HEX}}` | mid_hex (no `#`) |
| `{{MUTED_HEX}}` | muted_hex (no `#`) |
| `{{LIGHT_HEX}}` | light_hex (no `#`) |
| `{{RULE_HEX}}` | rule_hex (no `#`) |
| `{{INK_COLOR}}` | `#` + ink_hex |
| `{{BODY_COLOR}}` | `#` + body_hex |
| `{{MID_COLOR}}` | `#` + mid_hex |
| `{{MUTED_COLOR}}` | `#` + muted_hex |
| `{{LIGHT_COLOR}}` | `#` + light_hex |
| `{{RULE_COLOR}}` | `#` + rule_hex |
| `{{SOFT_FILL_COLOR}}` | `#` + soft_fill_hex |
| `{{NEUTRAL_COLOR}}` | `#FFFFFF` |
| `{{TYPOGRAPHY_PRIMARY}}` | typography_primary |
| `{{TYPOGRAPHY_FALLBACK}}` | typography_fallback |
| `{{VOICE_ARCHETYPE}}` | voice_archetype |
| `{{VOICE_ARCHETYPE_DESCRIPTION}}` | archetype description (Section 6) |
| `{{TONE_ATTRIBUTES}}` | tone attributes, comma-joined |
| `{{PILLAR_1}}`…`{{PILLAR_5}}` | brand pillars in order (if fewer than 5 pillars were given, delete the unused pillar lines from the target file instead of leaving tokens) |

### Logos & sub-brands (only substitute what exists)

| Placeholder | Source |
|---|---|
| `{{LOGO_WORDMARK}}` / `{{LOGO_PRIMARY_HORIZONTAL}}` | filename of the horizontal wordmark found in Section 5 |
| `{{LOGO_PRIMARY_STACKED}}` | filename of the stacked wordmark |
| `{{LOGO_MARK}}` | filename of the mark-only file |
| `{{LOGO_WHITE}}` | filename of the white variant |
| `{{LOGO_BLACK}}` | filename of the black variant |
| `{{SUBBRAND_1_NAME}}`…`{{SUBBRAND_3_NAME}}` | sub-brand names from Section 2 |
| `{{LOGO_SUBBRAND_1}}`…`{{LOGO_SUBBRAND_3}}` | sub-brand logo filenames |
| `{{SUBBRANDS}}` / `{{SUBBRAND_ROSTER}}` | comma-joined sub-brand names |

**The `{{SUBBRAND_N_*}}` template block:** `plugins/contractor-brand/skills/brand/references/sub-brands.md` contains one repeatable block of `{{SUBBRAND_N_*}}` tokens (name, full name, abbreviation, scope, voice nuance, proof points, sample copy, logos). For each sub-brand the user has, duplicate the block and fill it from their answers — collect scope and 2–3 proof points per sub-brand during Section 2 if sub-brands exist.

If the user has **no sub-brands**: delete the sub-brand rows from the logo table in `plugins/contractor-brand/skills/brand/SKILL.md`, replace the body of `references/sub-brands.md` with a one-line "This company operates as a single unified brand." note, and substitute `{{SUBBRANDS}}`/`{{SUBBRAND_ROSTER}}` with the company name. If a logo file is missing, leave its token in place — the brand skill treats an unresolved `{{LOGO_*}}` token as "ask the user before rendering."

### Market & estimating

| Placeholder | Source field |
|---|---|
| `{{TARGET_REVENUE_RANGE}}` | target_revenue_range |
| `{{PROJECT_TYPES}}` | project_types (comma-joined) |
| `{{SERVICE_LINES}}` | service_lines (comma-joined) |
| `{{PM_NAME}}` | pm_name |
| `{{PM_TITLE}}` | pm_title |
| `{{PM_EMAIL}}` | pm_email |
| `{{PM_PHONE}}` | pm_phone |
| `{{DEFAULT_DIVISION}}` | default_division |
| `{{DEFAULT_CITY}}` | default_city |
| `{{MARKET_CITY}}` | default_city |
| `{{MARKET_REGION}}` | market_region |
| `{{LICENSE_SCHEME}}` | license_scheme |
| `{{OHP_PERCENT}}` | ohp_percent |
| `{{CONTINGENCY_PERCENT}}` | contingency_percent |

Apply only approved exact-context edits after the safety gate. If previously substituted values have no trustworthy occurrence history, stop for targeted human review; never match old values globally.

**Do NOT substitute** the literal meta-tokens `{{TOKEN}}` and `{{PLACEHOLDER}}` — those are documentation examples in `contractor-docs`, not real placeholders.

---
