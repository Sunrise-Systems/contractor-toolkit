---
name: submittal
description: Generate a submittal cover sheet for product data, shop drawings, or samples — with spec section, manufacturer, status, and action required. Use when the user says "draft a submittal", "submittal cover", "submittal for [spec section]", or "/submittal".
argument-hint: [spec section or item]
---

# Submittal

Generate a submittal cover sheet for product data, shop drawings, samples, or O&M data. Outputs DOCX through `contractor-docs`. One submittal per item — keeps the log clean.

Use this before installing any product that requires architect/engineer approval. Most contracts list submittal requirements in the specs (Section 01 33 00 or similar).

---

## Inputs Needed

Gather in two chunks.

### 1. Identification
- Submittal number (e.g., SUB-016, often tied to spec section: 09 65 00.001)
- Spec section the submittal addresses
- Project name and number
- Submittal type: Product Data / Shop Drawing / Sample / O&M Manual / Mock-Up / Test Report
- Date submitted
- Date response needed (typical 14 days)

### 2. Item Detail
- Item description (e.g., "Resilient sheet flooring — Patient corridors")
- Manufacturer
- Product name / model number
- Supplier or subcontractor providing the submittal
- Number of copies / attachments
- Any deviations from spec (call them out — do not hide them)
- Prior submittal number if this is a resubmittal

---

## Workflow

```
1. INTAKE     → ID + item detail
2. CHECK      → Flag any deviations from spec for explicit callout
3. DRAFT      → Cover sheet with status checkboxes
4. EXPORT     → contractor-docs renders DOCX
```

If this is a resubmittal, reference the prior submittal number and what changed.

---

## Output

A one-page cover sheet with:

1. Header — "SUBMITTAL" + number, spec section, project
2. Item description block
3. Manufacturer / product / supplier block
4. Contractor's review stamp (signed by `{{PM_NAME}}`)
5. Status checkboxes — for architect/engineer to mark
6. Action required block — for the contractor

---

## Template

```markdown
# SUBMITTAL

**Submittal No.:** {SUBMITTAL_NUMBER}
**Spec Section:** {SPEC_SECTION}
**Type:** ☐ Product Data  ☐ Shop Drawing  ☐ Sample  ☐ O&M  ☐ Mock-Up  ☐ Test Report
**Date Submitted:** {DATE_SUBMITTED}
**Date Response Needed:** {DATE_NEEDED}
**Resubmittal of:** {PRIOR_NUMBER_OR_NA}

---

| Field | Value |
|-------|-------|
| **Project** | {PROJECT_NAME} |
| **Project No.** | {PROJECT_NUMBER} |
| **Contractor** | {{COMPANY_NAME}} |
| **Architect / Engineer** | {AE_NAME} |

---

## Item

**Description:** {ITEM_DESCRIPTION}
**Manufacturer:** {MANUFACTURER}
**Product / Model:** {PRODUCT_MODEL}
**Supplier / Sub:** {SUPPLIER}
**Copies / Attachments:** {COUNT}

**Deviations from Spec:** {DEVIATIONS_OR_NONE}

---

## Contractor's Review

I have reviewed this submittal and certify that the item meets the requirements of the Contract Documents, except as noted under Deviations above.

**Reviewed by:** {{PM_NAME}}, {{PM_TITLE}}
**Date:** {DATE_SUBMITTED}
**Signature:** ___________________________

---

## Architect / Engineer Action

☐ **No Exceptions Taken** — Proceed with fabrication and installation
☐ **Make Corrections Noted** — Proceed; corrections do not require resubmittal
☐ **Revise and Resubmit** — Do not proceed; resubmit with corrections
☐ **Rejected** — Submitted item does not comply; submit alternative
☐ **Submit Specified Item** — The submitted item is not the specified product

**Reviewer Comments:**

_______________________________________________________________________

_______________________________________________________________________

**Reviewed by:** ___________________________
**Title:** ___________________________
**Date Returned:** ___________________________

---

## Action Required by Contractor

- ☐ Proceed with fabrication
- ☐ Order material
- ☐ Schedule installation
- ☐ Resubmit with corrections by {DATE}
- ☐ Other: {ACTION}

---

*{{COMPANY_LEGAL_NAME}} · {{OPERATING_ADDRESS}} · {{DOMAIN}}*
```
