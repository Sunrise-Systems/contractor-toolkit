# contractor-docs

Generate branded construction documents — ROM budgets, conceptual budgets, formal bids, proposals, reports, letters, investment decks — for any contractor. HTML is the primary output (browser print-to-PDF); DOCX is the secondary, editable format.

The skill ships as a **token-driven template**. Drop in your company name, colors, fonts, and logo paths and the canonical CSS + python-docx helpers produce the same precise, premium output as a custom-built system.

## Skills

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `document-generator` | "create a document", "branded doc", "ROM", "proposal", any branded doc request | Full HTML + DOCX system with canonical CSS, python-docx helpers, and six document archetypes |
| `branded-doc` | `/branded-doc` | Short command alias that delegates to `document-generator` after collecting doc type + division |

## Brand Tokens (set per project)

Every reference file uses these placeholders. Replace them once per contractor and the entire system inherits the brand:

| Token | Example | Where it lands |
|-------|---------|----------------|
| `{{COMPANY_NAME}}` | Acme Builders | Wordmark, footer, cover |
| `{{TAGLINE}}` | Built different. | Cover sub-line, footer sub |
| `{{PRIMARY_COLOR}}` | `#000000` | Hero/footer fills, headings |
| `{{ACCENT_COLOR}}` | `#FF5F33` | Accent bars, section underlines, total borders (optional — omit for monochrome) |
| `{{INK_HEX}}` | `1A1A1A` | Titles, table header rules, grand totals |
| `{{BODY_HEX}}` | `2B2B2B` | Body text, table data |
| `{{MID_HEX}}` | `555555` | Supporting text, totals lines |
| `{{MUTED_HEX}}` | `888888` | Section labels, column headers |
| `{{LIGHT_HEX}}` | `BBBBBB` | Bullet dashes, page numbers |
| `{{RULE_HEX}}` | `DDDDDD` | Hairline separators |
| `{{TYPOGRAPHY_PRIMARY}}` | `Helvetica Neue` | Primary font family |
| `{{TYPOGRAPHY_FALLBACK}}` | `Helvetica, Arial, sans-serif` | CSS fallback stack |
| `{{LOGO_WORDMARK}}` / `{{LOGO_MARK}}` / `{{LOGO_WHITE}}` / `{{LOGO_BLACK}}` | resolved via `contractor-brand` plugin | Cover + footer marks |

Logos resolve from the sibling **contractor-brand** plugin:
`${CLAUDE_PLUGIN_ROOT}/../contractor-brand/skills/brand/assets/logos/`

## Output Format Defaults

HTML is the default for every deliverable. DOCX is a deliberate choice (client editing, contract signing, internal markup). See `skills/document-generator/SKILL.md` for the full output matrix.

## Install

This plugin ships as part of the `contractor-toolkit` marketplace. When installed alongside `contractor-brand`, logo paths resolve automatically. When used standalone, set the `LOGO_*` tokens to absolute paths.
