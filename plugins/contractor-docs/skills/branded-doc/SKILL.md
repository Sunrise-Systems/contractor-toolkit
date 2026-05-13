---
name: branded-doc
description: Short alias — generate a {{COMPANY_NAME}}-branded document (HTML primary, DOCX secondary). Delegates to document-generator. Triggers on "/branded-doc" or "create a branded document".
---

# /branded-doc — Generate Branded Document

Short command alias for the full `document-generator` skill. Use when the user wants a quick branded deliverable without spelling out the full workflow.

## Instructions

1. **Confirm document type.** Ask the user (or infer from context) which archetype to produce:
   - **rom** — Rough Order of Magnitude / Conceptual Budget (HTML default)
   - **estimate** — Multi-page construction estimate with cover, scope, terms, signatures
   - **proposal** — Service / engagement / project proposal
   - **report** — Progress, site, status, capabilities, audit
   - **letter** — Task order, change order, formal correspondence
   - **bid-invite** — Subcontractor bid invitation package
   - **cost-breakdown** — Internal PM document with unit-cost math
   - **formal-bid** — Division-by-division construction proposal (Residential / Commercial TI archetype)

2. **Confirm the issuing division / sub-brand.** Default: `{{COMPANY_NAME}}`. If the contractor has sub-brands (e.g. `{{COMPANY_NAME}} Electric`, `{{COMPANY_NAME}} A&E`), confirm which one.

3. **Default output format = HTML.** Only switch to DOCX if:
   - The client needs to mark up / edit numbers
   - A signed copy is required (contract, signed agreement, signed bid form)
   - The user explicitly asks for DOCX

4. **Gather required information based on document type:**

   | Type | Required inputs |
   |------|-----------------|
   | rom / estimate | Client name, project name, project address, estimate #, date, prepared-by + title, line items (CSI div / row / subtotal), contingency %, GC O&P %, permits, grand total, SF / $-per-SF context, assumptions, exclusions |
   | proposal | Client name, project name, date, prepared-by + title, project understanding, approach bullets, deliverables, fee lines, total fee, next steps |
   | report | Report title, client name, project name, date, prepared-by + title, sections (label + content + bullets) |
   | letter | Date, recipient name + title + company, subject, body paragraphs, sender name + title |
   | bid-invite | Project name + address, GC name + contact, trade name, bid due date, scope items, bid line items |
   | cost-breakdown | Project name + address, date, prepared by, 8-column line items (div / desc / unit / qty / labor / material / sub / total) |
   | formal-bid | All proposal fields plus division-by-division scope with inclusions, exclusions, alternates, and any inline highlight runs |

5. **Delegate to `document-generator`.** Use the canonical CSS from `references/html-canonical.md` for HTML output, or the helpers + generator function from `references/brand-system.md` + `references/templates.md` for DOCX. Follow every pattern exactly — fonts, colors, spacing, borders, shading.

6. **Save the output** to the current working directory using the convention:

   ```
   {company-slug}_{doctype}_{project-slug}_{YYYY-MM}.{html|pdf|docx}
   ```

   Examples:
   - `acme_rom_riverside-adu_2026-04.html`
   - `acme_proposal_smith-residence_2026-05.docx`
   - `acme_bid-invite_electrical_park-tower_2026-06.html`

7. **Render the PDF sibling** for HTML output via the `render_to_pdf()` helper in `references/html-to-pdf.md`. WeasyPrint primary, Chrome headless fallback, in-page print button as universal last resort.

8. **Report the output path(s)** and remind the user how to share:
   - HTML: open in any browser, click the in-page print button, save as PDF
   - DOCX: open in Word / Google Docs / LibreOffice for review or signing

## Example Usage

```
/branded-doc rom
/branded-doc proposal
/branded-doc letter
/branded-doc bid-invite electrical
```

## See Also

The full skill — including the canonical CSS block, all DOCX helpers, six generator functions, PDF rendering helpers, and the design checklist — lives in `../document-generator/SKILL.md`.
