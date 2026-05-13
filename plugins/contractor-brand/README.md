# contractor-brand

The brand identity reference plugin for any construction company — colors, typography, voice, logos, sub-brand guidelines, and the four canonical document archetypes that every GC ships (ROM, formal bid, letter, multi-page report).

This plugin is **templated**. Every company-specific value is a `{{PLACEHOLDER}}` token. Run the `/initialize` command from `contractor-initialize` to populate them with your company's specifics, or edit the files directly.

## What's in here

```
contractor-brand/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── skills/
    └── brand/
        ├── SKILL.md                                  Main brand reference, auto-invoked
        ├── references/
        │   ├── voice-guide.md                        Voice archetypes, tone, language rules
        │   ├── sub-brands.md                         Sub-brand setup template
        │   ├── document-archetypes.md                The four canonical document patterns
        │   └── brand-compliance-checklist.md         Pre-publish QA checklist
        └── assets/
            └── logos/                                Drop your logo files here
```

## When this skill auto-invokes

Anything that produces or reviews branded content: proposals, estimates, ROMs, letters of intent, change orders, capabilities decks, web copy, social posts, email outreach, ad creative, internal documents.

## Setup

1. Run `/initialize` (from the `contractor-initialize` plugin) to fill in placeholders, OR
2. Edit `skills/brand/SKILL.md` and the files in `skills/brand/references/` directly. Replace every `{{TOKEN}}` with your company's value.
3. Drop logo files into `skills/brand/assets/logos/`. Reference them in the Logo Assets table inside `SKILL.md`.

## Placeholder tokens

The main ones you'll see:

| Token | Meaning | Example |
|---|---|---|
| `{{COMPANY_NAME}}` | Full legal/marketing company name | "Acme Construction Group" |
| `{{COMPANY_SHORT}}` | Short form used in body copy | "Acme" |
| `{{TAGLINE}}` | Your tagline | "Built different." |
| `{{FOUNDED_YEAR}}` | Year founded | 1971 |
| `{{YEARS_EXPERIENCE}}` | Derived from founded year | "50+ years" |
| `{{MARKET_CITY}}` | Primary market city | "Los Angeles" |
| `{{MARKET_REGION}}` | Primary market region | "Southern California" |
| `{{PRIMARY_COLOR}}` | Primary brand color (hex) | `#0A0A0A` |
| `{{ACCENT_COLOR}}` | Accent color (hex) | `#FF5F33` |
| `{{NEUTRAL_COLOR}}` | Neutral / paper color (hex) | `#FFFFFF` |
| `{{TYPOGRAPHY_PRIMARY}}` | Primary typeface | "Helvetica Neue" |
| `{{TYPOGRAPHY_FALLBACK}}` | Fallback stack | "Arial, sans-serif" |
| `{{VOICE_ARCHETYPE}}` | Voice archetype name | "Approachable Expert" |
| `{{SUBBRANDS}}` | List of sub-brands | "A&E, General, Electric" |
| `{{CORE_BELIEF}}` | One-line core belief | "Every building reflects the society we want to live in." |
| `{{OWNERSHIP_TYPE}}` | Ownership story | "Family-owned and operated" |

See each individual file for additional context-specific tokens.

## License

MIT
