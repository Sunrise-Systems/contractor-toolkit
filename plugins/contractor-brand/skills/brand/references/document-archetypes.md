# Document Archetypes

Every {{COMPANY_NAME}} deliverable maps to one of four structural patterns. Pick the archetype first, then fill it with content. This file is the structural source of truth.

## The Decision Matrix

| Deliverable | Archetype | Format |
|---|---|---|
| ROM / conceptual budget / pre-design estimate | Archetype 1 | HTML |
| Investment Guide / capabilities deck | Archetype 1 or 4 | HTML |
| Pre-design feasibility study | Archetype 1 | HTML |
| Formal bid / construction proposal | Archetype 2 | DOCX |
| Subcontractor bid invitation | Archetype 2 | DOCX |
| Subcontractor scope clarification | Archetype 2 or 3 | DOCX |
| Letter of engagement / task order | Archetype 3 | DOCX |
| Change order | Archetype 3 | DOCX |
| Notice to proceed | Archetype 3 | DOCX |
| Owner/architect correspondence | Archetype 3 | DOCX |
| Progress report / site report | Archetype 4 | HTML |
| Monthly owner update | Archetype 4 | HTML |
| Capabilities deck | Archetype 4 | HTML |
| Scope check / gap analysis | Archetype 4 | HTML |

---

## Archetype 1 — ROM / Conceptual Budget

The HTML-first, visual ROM budget — used for pre-design feasibility estimates, conceptual budgets, and investment decks. This is the format prospects see BEFORE they sign with anyone. It has to look like premium, the numbers have to be defensible, and the assumptions have to be airtight.

### Structure (in order)

1. **Dark hero cover block** (`.cover`)
   - Uppercase tag line above wordmark
   - Wordmark (52–56px)
   - Division subtitle (uppercase, tracked, muted)
   - Project title
   - Address
   - 3-column meta grid: Prepared For / Prepared By / Date (or similar)

2. **Scope of Work section**
   - Uppercase section label with hairline underline
   - 2-column scope card grid on Soft_Fill background
   - Each card: short title + 2-3 sentence scope description

3. **Optional notice block**
   - Dark callout with uppercase label + descriptive body
   - Use for site-specific premium conditions, phasing constraints, occupancy adjacency, etc.

4. **Budget by CSI Division table**
   - Header row (uppercase, muted, tracked)
   - CSI division header bands (`.div-header` on Soft_Fill) — `Division XX - Name`
   - Scope rows: line description, optional note line, cost range right-aligned
   - Subtotal row per division: SemiBold, with 1.5px Ink top/bottom rule
   - Tabular numerics throughout the currency column

5. **Totals block**
   - Right-aligned contingency line
   - Right-aligned OH&P line (often 10-15%)
   - Right-aligned permits/fees line
   - **Grand total**: Bold 22px with 1.5px Ink top border, "Investment Range" label

6. **Assumptions & Exclusions**
   - 2-column card grid with clear sections: Included / Excluded / Basis of Estimate / Validity Period
   - Validity period explicit (e.g., "Valid for 30 days from issue date")

7. **Timeline**
   - Uppercase-labeled phase groups
   - Gantt-style bars using tonal grays (darkest for pre-construction/closeout, lightest for exterior/finishes)
   - Milestone markers for permit submission, permit approval, mobilization, substantial completion

8. **Print CTA button** — full-width Primary

9. **Dark footer block** — wordmark + division subtitle on left, prepared-for metadata on right

### Format: HTML

Print-to-PDF via browser. Do NOT render this as DOCX — the visual density only works in HTML/PDF.

### Voice in this archetype

- "Investment Range" not "Total Cost"
- "Basis of Estimate" not "Assumptions" (more professional, signals the right rigor)
- "This is a pre-design ROM. Final pricing requires construction documents." — explicit, candid disclaimer
- No marketing language in scope descriptions. Direct, technical.

---

## Archetype 2 — Formal Bid / Proposal Document

The text-heavy, division-organized construction proposal. This is what the client edits, marks up, redlines, and signs. The DOCX is the artifact of negotiation.

### Structure (in order)

1. **Header**
   - Project name
   - Address
   - Date
   - Client contact (name, role, email, phone)
   - Architect contact (name, firm, email, phone)
   - Document control: revision number, page count

2. **{{COMPANY_NAME}} contacts block**
   - Principal-in-charge or owner
   - Project manager(s)
   - Estimator
   - Accounts receivable / contracts

3. **Project summary** (1-2 sentences, declarative)
   - "This proposal covers the design and construction of a [scope] at [address], totaling approximately [SF or units]."

4. **Schedule of Values**
   - Table: division number + name + total dollar amount
   - One row per CSI division
   - Subtotal at bottom, before OH&P/contingency

5. **Division-by-division scope**
   - Heading: `Division XX - [Name]: $XX,XXX`
   - Sub-items (Foundation, Framing, Doors, etc.) each with:
     - Scope narrative (1-3 sentences, opens with direct verb)
     - Line item price OR budgetary allowance
     - Inline exclusions and alternates per item

6. **Standard contract language appendix** (optional)
   - Payment terms
   - Change order process
   - Insurance and bonding
   - Dispute resolution

### Voice in this archetype

- **Direct, specific, no-fluff.** "Provide and install…" opens most scope lines.
- **Alternate additions and deductions are called out in line** — not in a separate section.
- **Exclusions are inline with each scope item**, not buried in an appendix.
- **No marketing language.** This document is doing transactional work; voice is professional and matter-of-fact.

### Format: DOCX

Primary — this format is text-dense and the client needs to mark it up. The DOCX should use Arial (or {{TYPOGRAPHY_FALLBACK}}) 10pt body, 11pt bold division headings, no decorative elements, no color. Hairline section rules only.

---

## Archetype 3 — Letter / Agreement / Short Correspondence

One-to-three-page professional correspondence. Change orders, letters of engagement, notices, simple agreements.

### Structure (in order)

1. **Wordmark header** — horizontal logo, 2.0" wide, top-left
2. **Date** (right-aligned or left, beneath header)
3. **Recipient block** — name, title, company, address
4. **`Re: [Subject]`** — bold, single line
5. **Body** — 3-4 paragraphs max, plain professional language
6. **Closing** — "Sincerely," / "Best," / "Respectfully," + signature block (name, title, contact)
7. **Enclosures list** if applicable — "Enc: [doc 1], [doc 2]"

### Voice in this archetype

- More formal than the ROM voice, less formal than legal boilerplate.
- Address the recipient by name.
- State the purpose in the first sentence.
- Make any ask or next step explicit and time-bound.

### Format: DOCX

Primary. Or HTML if delivered via eSignature platform.

---

## Archetype 4 — Multi-Page Report

Progress reports, site reports, status updates, capabilities decks. Anything that is more than three pages and is read more than skimmed.

### Structure (in order)

1. **Dark cover block** (or white cover with wordmark at top if report is internal/lightweight)
2. **Table of contents** (for reports over 6 pages)
3. **Executive summary** (one page max — the only page some readers will read)
4. **Body sections**
   - Each major section opens with an uppercase section label with hairline underline
   - Body text at 13px / 1.5 line-height
   - 2-column info blocks or data tables where dense information needs to land
   - Photos sized at 100% of content width or 48% in a 2-up grid
5. **Optional Gantt-style timeline or progress tracker** for project status
6. **Appendix** for supporting docs, photos, RFIs, change orders
7. **Footer** with page number + document reference + revision number on every page

### Voice in this archetype

- Calmer and more measured than the ROM voice.
- Status reports use direct, factual phrasing: "Framing is 80% complete. Roof load testing is scheduled for [date]."
- No surprises. Anything off-track gets called out explicitly with a recovery plan.
- Photos have captions. Captions are short.

### Format: HTML (external, visual) or DOCX (internal, editable)

---

## Universal Rules — Across All Archetypes

These apply to every document {{COMPANY_NAME}} produces.

### Language
- "Investment" not "Cost" or "Price" in pricing sections.
- "Provide and install…", "Furnish and install…", "Demo and dispose…" — direct verbs to open scope lines.
- CSI MasterFormat division terminology when organizing scope.
- "Basis of Estimate" not "Assumptions" in formal estimate contexts.
- "Validity Period" explicit on every quoted price.

### Numbers
- Tabular numerics on all currency columns.
- Currency uses thousands separators: `$1,234,567`.
- Ranges use en-dash, not hyphen: `$1.2M–$1.5M`.
- Percentages rounded to whole numbers in body text unless precision is meaningful.

### Structure
- Inline exclusions per scope item — not buried in appendices.
- Subtotal per division before grand total.
- Grand total always with a heavier rule than subtotals (1.5px Ink top border).
- Page numbers and document reference in the footer of every multi-page document.

### Visual
- Hairline rules only. 0.5px {{RULE_COLOR}} for dividers, 1.5px {{INK_COLOR}} above subtotals and grand totals.
- Soft_Fill ({{SOFT_FILL_COLOR}}) is the only fill color on light sections — used for scope cards and CSI division header bands.
- No drop shadows. No gradients. No decorative borders.
- Logo on cover only. Body pages get no logo. Footer uses text wordmark.

---

## Example File References

If you have canonical reference files (gold-standard examples of each archetype), list them here. Suggested locations:

- `assets/examples/rom_residential.html` — ROM gold standard (single-family or hillside)
- `assets/examples/rom_commercial_ti.html` — ROM gold standard (commercial TI)
- `assets/examples/proposal_residential.docx` — Formal bid gold standard (residential)
- `assets/examples/proposal_commercial_ti.docx` — Formal bid gold standard (commercial TI)
- `assets/examples/change_order.docx` — Letter/agreement gold standard
- `assets/examples/monthly_progress_report.html` — Multi-page report gold standard

Drop your examples into `skills/brand/assets/examples/` and update this list.
