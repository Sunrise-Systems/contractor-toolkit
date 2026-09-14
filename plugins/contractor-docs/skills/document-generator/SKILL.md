---
name: document-generator
description: Generate {{COMPANY_NAME}}-branded documents — ROM budgets, conceptual budgets, formal bids, proposals, reports, letters, investment decks. HTML primary, DOCX secondary. Triggers on "create a document" or any branded doc request.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(python3 *toolkit_guard.py *)
---

# {{COMPANY_NAME}} Document Generator

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** Project/company/revision, approved semantic fields, intended use, brand assets, source content and format expectations.
- **Output:** Saved HTML/DOCX/XLSX drafts, optional verified PDF and per-artifact readback receipts.
- **AI role:** Extract, reconcile and draft; independently reopen exact saved paths, not merely trust a successful generator call.
- **Human role:** Named domain reviewer approves facts/amounts/purpose; designated reviewer performs required visual inspection.
- **Risk:** Consequential output when financial, legal, safety or external-facing; drafting does not lower that risk.
- **Checkpoint:** Project-specific output directory with local `checkpoints/` for immutable prior revisions, source/artifact hashes, content expectations, approvals and receipts; outside package inputs.
- **Approval boundary:** Named human approval of exact project/entities/revision, dates, amount/currency where relevant, recipients/use, assumptions/exceptions and semantic-content digest. Material edits or regeneration invalidate approval. Final verified is not issued: issuance remains `not_issued`; no transmission, signature or external mutation.
- **Verifier:** `python3 "$GUARD" verify-artifact --artifact "$ARTIFACT" --expectations "$EXPECTATIONS" --receipt "$RECEIPT"`; check approved semantic fields separately from final-file digest. Required domain/visual checks must also pass.
- **Failure:** Missing evidence, stale approval/receipt or unavailable checks become `needs_human`; keep draft/checkpoint, identify owner and next safe action, withhold final status.



Generate clean, professional documents for any contractor brand. The design philosophy is **white pages, typography as brand** — visual hierarchy is carried by font size, weight, and spacing on white, with accent color used only as a precision detail. The result reads as precise, confident, and premium.

**HTML is the primary output format for every document.** The clean black + white + hairline aesthetic only renders correctly when typography is preserved perfectly, and HTML → browser-print-to-PDF is the most reliable path to that fidelity. DOCX is opt-in for editable / signable workflows.

This skill is **token-driven**. Every color, font, logo, and brand string referenced below is a `{{TOKEN}}` placeholder. Substitute the contractor's brand values once, then the entire generation pipeline inherits the brand.

## Brand Tokens

| Token | Purpose | Example default |
|-------|---------|-----------------|
| `{{COMPANY_NAME}}` | Wordmark text on cover + footer | `Acme Builders` |
| `{{TAGLINE}}` | Cover sub-line + footer sub | `Built different.` |
| `{{PRIMARY_COLOR}}` | Hero cover / footer background fill | `#000000` |
| `{{ACCENT_COLOR}}` | Optional accent — bars, total rule, button (omit for pure monochrome) | `#FF5F33` |
| `{{INK_HEX}}` | Titles, header rules, grand total | `1A1A1A` |
| `{{BODY_HEX}}` | All body text, table data | `2B2B2B` |
| `{{MID_HEX}}` | Supporting text, address lines, total lines | `555555` |
| `{{MUTED_HEX}}` | Section labels, column headers, meta labels | `888888` |
| `{{LIGHT_HEX}}` | Em-dash bullets, page numbers, tertiary info | `BBBBBB` |
| `{{RULE_HEX}}` | Hairline separators, data row borders | `DDDDDD` |
| `{{TYPOGRAPHY_PRIMARY}}` | Primary typeface | `Helvetica Neue` |
| `{{TYPOGRAPHY_FALLBACK}}` | CSS fallback stack | `Helvetica, Arial, sans-serif` |
| `{{LOGO_WORDMARK}}` | Cover lockup (preferred) | resolved from `contractor-brand` |
| `{{LOGO_MARK}}` | Standalone mark | resolved from `contractor-brand` |
| `{{LOGO_WHITE}}` | White lockup for dark hero | resolved from `contractor-brand` |
| `{{LOGO_BLACK}}` | Black lockup for white pages | resolved from `contractor-brand` |

Logos are bundled in the sibling `contractor-brand` plugin and resolved via:

```python
LOGO_DIR = os.path.join(
    os.environ.get("CLAUDE_PLUGIN_ROOT", os.getcwd()),
    "..", "contractor-brand", "skills", "brand", "assets", "logos"
)
```

## Output Format — HTML is the Default for Everything

| Deliverable | Primary | Secondary (only if needed) |
|---|---|---|
| ROM Budget | **HTML** | DOCX only if client explicitly wants to edit numbers |
| Conceptual Budget | **HTML** | DOCX + XLSX exclusions |
| Scope Check Report | **HTML** | — |
| Formal Bid / Construction Proposal | **HTML** | DOCX required (client marks it up) |
| Sub Bid Invitation | **HTML** | DOCX if the sub specifically asks for it |
| Investment Deck / Capabilities | **HTML** | — |
| Report (progress, site, status) | **HTML** | DOCX only for internal edits |
| Letter / Task Order / Change Order | **HTML** | DOCX for client-signed version |
| Contract — preview | **HTML** | — |
| Contract — signable | DOCX | HTML preview attached |
| Exclusions Workbook | XLSX | HTML summary sheet for presentation |
| Internal Cost Breakdown | **HTML** | DOCX for PM markup |

**The default is HTML. DOCX is a deliberate choice, not a fallback.**

## Clean HTML styling

Read `references/html-styling-guide.md` for the mandatory variables, print block and component examples; copy the full canonical CSS from `references/html-canonical.md`. Preserve the brand design rules, then independently verify saved content and layout.

## HTML Generation Process

1. Open `references/html-canonical.md` and copy the full `<style>` block verbatim.
2. Substitute the brand tokens (`{{PRIMARY_COLOR}}`, `{{ACCENT_COLOR}}`, font, etc.) once at the top of the `:root` block.
3. Fill in the markup skeleton — cover metadata, scope items, notice body, CSI division rows, totals, assumptions, timeline phases, footer.
4. Save to the working directory: `{company-slug}_{doctype}_{project-slug}_{YYYY-MM}.html`
5. Independently verify the saved HTML and record browser visual review; only then offer browser Print / Save as PDF as a draft conversion path. Verify any saved PDF separately.

## DOCX Design Philosophy (when DOCX is unavoidable)

**White pages. Typography is the brand.** No dark cover blocks (DOCX). No colored fills. No decorative backgrounds. The entire visual hierarchy is carried by font size, weight, and spacing on white.

- **No color fills** — Every DOCX page is white. Tables have no background shading except white.
- **Hairline rules only** — Section separators are thin `{{RULE_HEX}}` paragraph borders. Table headers use a single heavy `{{INK_HEX}}` bottom rule. Data rows use `{{RULE_HEX}}` hairlines.
- **Logo once, on the cover** — Single logo image at top-left of cover, ~1.6" wide. No logo on body pages. Footer uses the company wordmark in bold text.
- **No letter-spacing** — Do not use kern/tracking on any text. Natural type spacing throughout.
- **One font** — `{{TYPOGRAPHY_PRIMARY}}` (or Arial fallback if the custom font isn't installed). Size and weight create all hierarchy.
- **HTML archetype exception** — HTML documents DO use a colored hero cover block. This is intentional — HTML is the presentation format; DOCX is the working format. They are visually related but not identical.

## Color Palette (token map)

| Name        | Token         | Default  | Usage |
|-------------|---------------|----------|-------|
| PRIMARY     | `{{PRIMARY_COLOR}}` | `#000000` | HTML hero cover blocks / footers ONLY. Not used in DOCX. |
| ACCENT      | `{{ACCENT_COLOR}}`  | optional  | Accent bars, total top borders, buttons. Omit for monochrome. |
| INK         | `{{INK_HEX}}` | `1A1A1A` | Titles, bold labels, table header rule, grand total |
| BODY        | `{{BODY_HEX}}` | `2B2B2B` | All body text, table data |
| MID         | `{{MID_HEX}}` | `555555` | Supporting text, address lines, totals lines |
| MUTED       | `{{MUTED_HEX}}` | `888888` | Section labels, column headers, meta labels, footer sub |
| LIGHT       | `{{LIGHT_HEX}}` | `BBBBBB` | Em-dash bullets, tertiary info, page numbers |
| RULE        | `{{RULE_HEX}}` | `DDDDDD` | Hairline separators, data row borders, info table borders |
| WHITE       | `FFFFFF`       | —        | All backgrounds — pages, cells, tables |

Never introduce an accent color outside the token system. Never use alternating row backgrounds (`F5F5F5` stripes) — flat white only. Never use a "Black" font weight on body type — use the primary typeface with `bold=True` instead.

## Typography

| Use | Font | Size | Bold |
|-----|------|------|------|
| Cover project title | `{{TYPOGRAPHY_PRIMARY}}` | 26pt | Yes |
| Cover doc-type label | `{{TYPOGRAPHY_PRIMARY}}` | 9pt | No |
| Cover meta label | `{{TYPOGRAPHY_PRIMARY}}` | 8pt | No |
| Cover meta value | `{{TYPOGRAPHY_PRIMARY}}` | 11pt | No |
| Section label | `{{TYPOGRAPHY_PRIMARY}}` | 8.5pt | No |
| Body text | `{{TYPOGRAPHY_PRIMARY}}` | 10pt | No |
| Bullet text | `{{TYPOGRAPHY_PRIMARY}}` | 10pt | No |
| Table column header | `{{TYPOGRAPHY_PRIMARY}}` | 8pt | No |
| Table division header | `{{TYPOGRAPHY_PRIMARY}}` | 8.5pt | No |
| Table data — main | `{{TYPOGRAPHY_PRIMARY}}` | 10pt | No |
| Table data — note | `{{TYPOGRAPHY_PRIMARY}}` | 8.5pt | No |
| Subtotal / grand total | `{{TYPOGRAPHY_PRIMARY}}` | 10.5–14pt | Yes |
| Info table key | `{{TYPOGRAPHY_PRIMARY}}` | 8.5pt | No |
| Info table value | `{{TYPOGRAPHY_PRIMARY}}` | 10pt | No |
| Running header | `{{TYPOGRAPHY_PRIMARY}}` | 7.5pt | No |
| Footer wordmark | `{{TYPOGRAPHY_PRIMARY}}` | 8pt | Yes |
| Footer sub-label | `{{TYPOGRAPHY_PRIMARY}}` | 8pt | No |
| Page number | `{{TYPOGRAPHY_PRIMARY}}` | 8pt | No |

**Never use the "Black" or "Heavy" weight of the primary typeface.** Bold creates all heavy weight.

## Logo Files

Resolve from the sibling `contractor-brand` plugin:

```
${CLAUDE_PLUGIN_ROOT}/../contractor-brand/skills/brand/assets/logos/
```

| Token | Variant | Usage |
|-------|---------|-------|
| `{{LOGO_WORDMARK}}` | Full wordmark + mark | **Cover page primary** — preferred on cover |
| `{{LOGO_MARK}}` | Standalone mark | Body-page accents, favicons |
| `{{LOGO_WHITE}}` | White lockup | Dark hero cover blocks, dark footer |
| `{{LOGO_BLACK}}` | Black lockup | Formal contexts on white |

**Cover logo width: `Inches(1.6)`** — sized down, top-left only.
**Body pages: no logo** — footer uses the company wordmark text instead.

If the contractor-brand plugin is not present, set `{{LOGO_*}}` to absolute paths to the brand's logo files.

## Document Types

| Document | Function in `templates.md` | When to use |
|----------|----------------------------|-------------|
| Construction Estimate / ROM | `generate_estimate()` §1 | Client-editable budget, CSI-structured line items |
| Proposal | `generate_proposal()` §2 | A&E fee proposal or service engagement |
| Report | `generate_report()` §3 | Progress, site, status, capabilities |
| Letter / Agreement | `generate_letter()` §4 | Task order, change order, formal correspondence |
| Sub Bid Invitation | `generate_bid_invitation()` §5 | Subcontractor bid package per trade |
| Detailed Cost Breakdown | `generate_cost_breakdown()` §6 | Internal PM document with unit-cost math |
| Formal Bid (Residential / Commercial TI archetype) | Custom — see `references/templates.md` | Division-by-division construction proposal with inline highlights, inclusions, exclusions |

### Formal Bid — Residential / Commercial TI archetype

Key features:

- Header block: project, address, date, client + architect contacts, contractor contact roster
- Schedule of Values: division number + name + dollar total
- Division-by-division scope: `Division XX - [Name]: $XX,XXX` heading, sub-item narratives, prices as `Budgetary Allowance $X`, `Estimated cost $X`, or firm amount
- Inline highlights: highlighted runs for items "already included in prior contract" (or any other color-coded category — use text highlight, not font color)
- Inline inclusions and exclusions: "Provide and install…" and "Excludes…" within the same section
- Alternate additions and deductions called out in line

Use the standard `r()` + `body()` + `section_label()` helpers but structure the output per the archetype. To add a highlight run, set `run.font.highlight_color = WD_COLOR_INDEX.BLUE` (or other index) on the relevant text run.

## Critical Rules

1. **No background fills** — `set_cell_shading(cell, "FFFFFF")` on every cell. Never use any other color. (Exception: HTML hero/footer blocks use `{{PRIMARY_COLOR}}`.)
2. **No letter-spacing** — Never pass `kern=` to the `r()` helper. Natural type spacing only.
3. **One logo, cover only** — `add_picture()` only on the cover page at `Inches(1.6)`.
4. **Table width = Inches(6.5)** — Always. Page is 8.5" − 1" − 1" margins = 6.5" printable.
5. **Column widths must sum to 6.5"** — Verify before running.
6. **Font on every run** — Use the `r()` helper which sets both `run.font.name` and `w:rFonts` XML.
7. **Cell shading via parse_xml** — Always `w:val="clear"`. Never use python-docx's shading enum.
8. **No empty paragraph spacers** — Use `space_before` / `space_after` on paragraphs instead.
9. **Section labels** — Small muted text followed immediately by a `{{RULE_HEX}}` hairline rule.
10. **Table headers** — Muted uppercase text, white background, heavy `{{INK_HEX}}` bottom border only.
11. **Never use display-weight body type** — Use the primary typeface with `bold=True`.
12. **Accent is precision, not theme** — If accent appears in more than five places per page, it's overused. If a document feels flat, fix the typography and spacing, not the color.

## Optional PDF conversion

A PDF sibling is optional and only verified when extraction and visual checks are available. Use the unified `render_to_pdf()` helper in `references/html-to-pdf.md`. It tries **WeasyPrint** first (pure Python, no browser) and falls back to **Chrome headless** if WeasyPrint isn't installed.

```python
html_path = os.path.join(output_dir, f"{company_slug}_rom_{slug}_{date}.html")
pdf_path  = os.path.join(output_dir, f"{company_slug}_rom_{slug}_{date}.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

render_to_pdf(html_path, pdf_path)   # emits the PDF alongside the HTML
```

Install optional render dependencies only in an isolated environment. Browser print is a conversion fallback, not proof of verified PDF output.

## File Naming Convention

```
{company-slug}_{doctype}_{project-slug}_{YYYY-MM}.{html|pdf|docx}
```

Examples (replace `{company-slug}` with the contractor's slug — e.g. `acme`, `delta`, `pinnacle`):

- `acme_rom_riverside-adu_2026-04.html`
- `acme_proposal_smith-residence_2026-05.docx`
- `acme_bid-invite_electrical_park-tower_2026-06.html`

## References

| File | Contents |
|------|----------|
| `references/brand-system.md` | Complete Python — all helpers: constants, page setup, r(), hairline(), add_cover, section_label, body, bullet, info_table, line_item_table, totals_block, signature_block, setup_header_footer, add_page_break |
| `references/templates.md` | Complete generator functions for all 6 base document types with full source + usage example |
| `references/html-canonical.md` | Full copy-paste `<style>` block + HTML markup skeleton for every document |
| `references/html-to-pdf.md` | `render_to_pdf()` helpers — WeasyPrint primary, Chrome headless fallback, unified function |
| `references/python-setup.md` | Imports, page setup, LOGO_DIR pattern, column width math, common issues |

## Format-aware verification

Always use the explicit verifier regardless of Write, Bash or Python generation. The HTML Write hook only checks a subset and may not exist in standalone packages. Missing parsers block the relevant gate, never skip to green.

- HTML: parse visible identity/revision, required sections, approved numbers, tokens and canonical print CSS; record browser visual review separately.
- DOCX: reopen paragraphs/tables plus headers and footers; compare approved content, not merely filenames or nonempty bytes.
- XLSX: check sheets/cells, tokens, prior-period linkage and cross-foot totals; recompute covered arithmetic independently. Formula text and stale/absent cached values are not results; unsupported formulas block financial finalization.
- PDF: compare extracted identity/text/totals to verified source and check pages/clipping/layout visually. If either check is unavailable, mark PDF unverified, withhold final status, and offer the verified source draft.

Standalone packages do not include sibling brand assets by implication. Resolve installed companion assets explicitly, or obtain approved local assets/no-logo design before rendering; do not guess paths or leave output tokens unresolved.
