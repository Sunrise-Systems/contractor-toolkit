---
name: brand
description: "Enforce {{COMPANY_NAME}} brand identity — colors, typography, voice, logos, sub-brand guidelines, document archetypes. Auto-invoke for any branded content: proposals, estimates, social, ads, internal docs."
---

# {{COMPANY_NAME}} Brand Enforcement

{{COMPANY_NAME}} is a {{OWNERSHIP_TYPE}} {{COMPANY_TYPE}} in {{MARKET_CITY}} with {{YEARS_EXPERIENCE}} of experience. Everything we produce — every word, every layout, every piece of content — must reflect who we are.

**Tagline:** {{TAGLINE}}

**Core belief:** {{CORE_BELIEF}}

This skill is the source of truth for all visual and verbal identity. Load it for ANY branded output (proposals, estimates, web copy, social, ads, decks, letters, internal docs).

---

## 1. Visual Identity

### Color Palette

The default {{COMPANY_NAME}} system is **premium monochrome**: a primary near-black, a full neutral scale, white paper, and a single optional accent. Weight comes from bold typography, generous whitespace, and hairline separators — not from color. This is what photographs and prints best and what most premium construction brands settle on.

If your `/initialize` chose a colored accent, it is reserved for: cover bars, section underlines, grand-total borders, primary CTAs, and division marks. Never used to "decorate."

| Role | Token | Hex | Usage |
|------|-------|-----|-------|
| **PRIMARY** | Pure primary | `{{PRIMARY_COLOR}}` | Hero/cover blocks, footer blocks, print CTAs (white-on-primary). |
| **INK** | Near-black | `{{INK_COLOR}}` | Titles, bold labels, table header rule, grand total. Used instead of pure black for body text — pure black is too harsh at small sizes. |
| **BODY** | Body text | `{{BODY_COLOR}}` | All body text, table data. |
| **MID** | Mid gray | `{{MID_COLOR}}` | Supporting text, address lines, total supporting lines. |
| **MUTED** | Muted gray | `{{MUTED_COLOR}}` | Section labels, column headers, meta labels, footer sub-label. |
| **LIGHT** | Cool gray | `{{LIGHT_COLOR}}` | Em-dash bullets, tertiary info, page numbers, division number prefix. |
| **RULE** | Hairline gray | `{{RULE_COLOR}}` | Section dividers, table row separators, info-table borders. |
| **SOFT_FILL** | Off-white fill | `{{SOFT_FILL_COLOR}}` | CSI division header bands, scope cards (HTML only — not used in DOCX). |
| **PAPER** | Pure white | `{{NEUTRAL_COLOR}}` | All page, cell, and table backgrounds. |
| **ACCENT** (optional) | Brand accent | `{{ACCENT_COLOR}}` | Cover bar, section underlines, grand-total border, primary CTA. Sparingly. |

**Usage rules — non-negotiable:**
- **Black-on-white is the default.** White-on-primary is reserved for cover/hero blocks, footer blocks, callout/notice blocks, and print CTAs.
- **Dividers are hairlines, not lines.** Use `{{RULE_COLOR}}` at 0.5px. Above subtotals and grand totals, use `{{INK_COLOR}}` at 1.5px. These are the only allowed rule weights.
- **The only fill color on light sections is `{{SOFT_FILL_COLOR}}`** — used for scope cards and CSI division header bands. Everywhere else is white.
- **Never use pure black (`#000000`) for body text** — too harsh at small sizes. Use `{{INK_COLOR}}` for body, reserve pure primary for hero/footer blocks.
- **If an accent color is used, it is "earned."** If accent appears in more than 5 places on a page, it's overused.
- **No gradients. No shadows. No drop-shadows on cards.** Flat only.

### Typography

Typography carries the entire visual load — so weight, size, tracking, and whitespace must be exact.

**Primary font:** {{TYPOGRAPHY_PRIMARY}} (fallback: {{TYPOGRAPHY_FALLBACK}})
**DOCX fallback:** Arial — guaranteed cross-platform match.

The typeface should carry presence at regular weight. Bold is rarely needed. Reserve heavier weights for the wordmark, grand totals, and division headers.

| Element | Weight | Size | Color | Notes |
|---------|--------|------|-------|-------|
| Cover wordmark | Bold | 52–56px | Paper on Primary | Tracked `-0.025em`, uppercase |
| Cover subtitle (division name) | Regular | 12px | Muted | Tracked `0.1em`, uppercase |
| Cover title (project name) | Medium | 22px | Paper | Line-height 1.3 |
| Cover address | Regular | 13px | Muted | |
| Cover meta label | Regular | 10px | Muted | Tracked `0.12em`, uppercase |
| Cover meta value | Medium | 14px | Paper | |
| Section label (micro) | Medium | 10px | Muted | Tracked `0.14em`, uppercase, hairline underline |
| Section body | Regular | 13px | Ink | Line-height 1.5 |
| Scope card title | SemiBold | 12px | Ink | |
| Scope card body | Regular | 11.5px | Mid | Line-height 1.55 |
| Table header | Medium | 10px | Muted | Tracked `0.1em`, uppercase |
| Table body | Regular | 13px | Ink | Line-height 1.45 |
| Division header row | SemiBold | 11px | Mid on Soft_Fill | Tracked `0.08em`, uppercase |
| Division number | Regular | 11px | Light | Inline prefix, `margin-right: 10px` |
| Subtotal row | SemiBold | 13px | Ink | 1.5px Ink rule top/bottom |
| Grand total | Bold | 22px | Ink | Tracked `-0.01em`, 1.5px Ink top border |
| Notice body | Regular | 12px | Paper on Primary | Line-height 1.65 |
| Footer wordmark | Bold | 22px | Paper on Primary | Tracked `-0.02em`, uppercase |
| Footer subtitle | Regular | 11px | Muted | |

**Typographic rules:**
- Headlines are short, punchy, and confident. Never longer than one line on desktop.
- Body text uses line-height 1.45–1.55 for clean readability without feeling airy.
- Letter-spacing on tight headlines: `-0.01em` to `-0.025em`. Letter-spacing on uppercase micro-labels: `0.08em` to `0.14em`.
- ALL CAPS is the signature device — used for micro-labels, section labels, the wordmark, meta labels. Never for running sentences.
- No italic for emphasis — use weight or restructure the sentence.
- `font-variant-numeric: tabular-nums` on any column containing currency or numeric values — figures must align.

### Logo Assets

All logos live at `skills/brand/assets/logos/` inside this plugin. Reference them via `${CLAUDE_PLUGIN_ROOT}/skills/brand/assets/logos/`.

| File | Brand | Use Case |
|------|-------|----------|
| `{{LOGO_PRIMARY_STACKED}}` | {{COMPANY_NAME}} (parent) | Stacked wordmark — primary use on documents, presentations, hero sections |
| `{{LOGO_PRIMARY_HORIZONTAL}}` | {{COMPANY_NAME}} (parent) | Horizontal single-line wordmark — headers, footers, compact spaces |
| `{{LOGO_WHITE}}` | {{COMPANY_NAME}} | White wordmark — dark backgrounds, hero covers, footer blocks |
| `{{LOGO_BLACK}}` | {{COMPANY_NAME}} | Black wordmark — formal contexts, light backgrounds |
| `{{LOGO_SUBBRAND_1}}` | {{SUBBRAND_1_NAME}} | Sub-brand specific documents |
| `{{LOGO_SUBBRAND_2}}` | {{SUBBRAND_2_NAME}} | Sub-brand specific documents |
| `{{LOGO_SUBBRAND_3}}` | {{SUBBRAND_3_NAME}} | Sub-brand specific documents |

**Logo rules — MANDATORY:**
- **Always reference a real bundled file** in `skills/brand/assets/logos/`. Never improvise SVG paths, never recolor a variant that doesn't exist, never substitute a different logo silently.
- **If the file you need is missing, stop and ask the user.** A wrong logo is worse than a delayed one.
- **Minimum clear space:** equal to the height of the first character of the wordmark on all sides.
- **Never stretch, rotate, recolor, or add effects** to logos. Use the bundled variants.
- **On dark backgrounds, use white versions.** On light backgrounds, use black or accent versions per the decision rules below.
- **Parent vs sub-brand:** when content spans divisions or is company-wide, always use the parent wordmark. When content is specifically about one division's service, use that sub-brand.
- **Cover pages only.** Body pages do not get a logo. The footer uses a text wordmark, not the logomark.

### Logo Color Decision Tree

Pick the logo color top-to-bottom:

1. **Is this artifact specifically about a single sub-brand or department?** → use that sub-brand's logo.
2. **Is the surface dark (hero, footer, dark UI)?** → use the white variant.
3. **Otherwise (company-wide, multi-department, ops/admin/leadership, unsure)** → use the primary/default variant.
4. **If still unsure, ASK the user before rendering.**

### Layout Principles

- **Generous whitespace.** Let content breathe. Padding of 36–56px between sections minimum.
- **Left-aligned by default.** Center alignment only for hero sections and single-line CTAs.
- **Maximum content width:** 900px for full documents. 720px for body text when wrapped.
- **No clutter.** If a visual element doesn't serve the content, remove it. No decorative borders, no drop shadows, no ornamental rules. The only lines allowed are hairline section dividers and the 1.5px subtotal/grand-total rules.
- **Grid:** 12-column grid for web layouts. 4-column for mobile.
- **Premium through restraint.** The document feels expensive because of what it leaves out — not what it adds. Every element earns its place.
- **Test without color.** Remove all accent color. If the document still reads as professional and structured, the hierarchy is correct.

---

## 2. Document Archetypes — The Four Canonical Patterns

Every {{COMPANY_NAME}} deliverable maps to one of these four structural patterns. See `references/document-archetypes.md` for full structural specs.

### Picking the Right Archetype

| Deliverable | Archetype | Format |
|---|---|---|
| ROM / conceptual budget / pre-design estimate | Archetype 1 | HTML |
| Investment Guide / capabilities deck | Archetype 1 or 4 | HTML |
| Formal bid / construction proposal | Archetype 2 | DOCX |
| Subcontractor bid invitation | Archetype 2 | DOCX |
| Letter of engagement / task order | Archetype 3 | DOCX |
| Change order | Archetype 3 | DOCX |
| Progress report / site report | Archetype 4 | HTML |
| Scope check / gap analysis | Archetype 4 | HTML |

### Archetype Quick Reference

**Archetype 1 — ROM / Conceptual Budget Document.** HTML-first visual budget for pre-design feasibility, conceptual estimates, and investment decks. Black hero cover, scope cards on Soft_Fill, CSI-division-organized budget table with subtotals and grand total, assumptions/exclusions, timeline, dark footer block. Format: HTML (print-to-PDF via browser).

**Archetype 2 — Formal Bid / Proposal Document.** Text-heavy, division-organized construction proposal. Header, contacts, project summary, schedule of values, division-by-division scope with line items and inline exclusions, optional contract appendix. Voice: direct, "Provide and install…" opens most scope lines. Format: DOCX (the client needs to mark it up).

**Archetype 3 — Letter / Agreement / Short Correspondence.** One-to-three-page professional correspondence. Wordmark header (horizontal, 2.0" wide), date + recipient + `Re:` line, 3–4 body paragraphs, closing + signature, enclosures. Format: DOCX (or HTML for eSignature delivery).

**Archetype 4 — Multi-Page Report.** Progress reports, site reports, status updates, capabilities decks. Dark cover block, uppercase section labels with hairline underlines, body at 13px / 1.5 leading with 2-column info blocks, optional Gantt/progress tracker, footer with page number + document reference. Format: HTML (external) or DOCX (internal/editable).

**Universal rules for every archetype:**
- Use "Investment" not "Cost" or "Price" for the pricing section.
- CSI division terminology when organizing scope: `Division 03 - Concrete`, `Division 05 - Metals`, etc. Division number prefix in Light gray, division name in Mid.
- Schedule of Values uses division number + name + total dollar amount, right-aligned currency.
- Line items open with "Provide and install…", "Furnish and install…", or "Demo and dispose…" — direct verbs.
- Inline exclusions and alternates per scope item — not buried in a separate appendix.
- Tabular numerics on any currency column.

---

## Required brand guidance

Read `references/voice-and-audience.md` for voice, language and audiences (sections 3–4).
Read `references/content-enforcement.md` for content, sub-brands and enforcement (sections 5–8).
