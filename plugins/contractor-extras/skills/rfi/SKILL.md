---
name: rfi
description: Generate a one-page Request for Information with drawing/spec references, question, urgency, and response field. Use when the user says "draft an RFI", "RFI for [topic]", "request for information", or "/rfi".
argument-hint: [RFI subject]
---

# RFI — Request for Information

Generate a Request for Information directed to the architect or owner. One-page document. Outputs DOCX or PDF through `contractor-docs`.

Use this any time a drawing conflict, missing detail, field condition, or spec ambiguity needs a written answer. RFIs create the paper trail that protects everyone when issues escalate.

---

## Inputs Needed

Gather in two chunks. Keep it fast — RFIs are time-sensitive.

### 1. Identification
- RFI number (sequential, e.g., RFI-014)
- Project name
- Date
- From: `{{COMPANY_NAME}}`, `{{PM_NAME}}`
- To: Architect or Owner contact name + email

### 2. The Question
- Subject (5-8 words)
- Drawing reference (sheet number, detail bubble) and/or spec section
- The actual question — clear, specific, one issue per RFI
- What we propose (if we have a recommendation — speeds the response)
- Urgency: Routine (5 business days), Priority (2 business days), Urgent (24 hours)
- Date response needed by

---

## Workflow

```
1. INTAKE     → ID + question
2. CLARIFY    → If the question is vague, ask the user to tighten it
3. DRAFT      → Single-page RFI
4. EXPORT     → contractor-docs renders DOCX/PDF
```

One issue per RFI. If the user has three questions, generate three RFIs. Bundled RFIs slow down responses.

---

## Output

A one-page document with:

1. Header — "REQUEST FOR INFORMATION" + RFI number
2. Project / parties block
3. Reference block (drawings, specs, prior RFIs)
4. Question section
5. Contractor's proposed solution (optional)
6. Urgency and response-needed date
7. Response section (blank, to be filled by architect/owner)
8. Signature lines

---

## Template

```markdown
# REQUEST FOR INFORMATION

**RFI No.:** {RFI_NUMBER}
**Date Submitted:** {DATE}
**Response Needed By:** {RESPONSE_DATE}
**Urgency:** {ROUTINE | PRIORITY | URGENT}

---

| Field | Value |
|-------|-------|
| **Project** | {PROJECT_NAME} |
| **Project Address** | {PROJECT_ADDRESS} |
| **From** | {{PM_NAME}}, {{PM_TITLE}} — {{COMPANY_NAME}} |
| **To** | {RECIPIENT_NAME}, {RECIPIENT_TITLE} — {RECIPIENT_COMPANY} |
| **CC** | {CC_LIST} |

---

## Subject

{SUBJECT_LINE}

## Reference

- **Drawing(s):** {DRAWING_SHEET} — {DETAIL_BUBBLE}
- **Specification:** Section {SPEC_SECTION}
- **Related RFIs:** {PRIOR_RFI_NUMBERS_OR_NONE}

## Question

{CLEAR_SPECIFIC_QUESTION}

## Contractor's Proposed Solution

{PROPOSED_APPROACH_OR_NA}

Implementing this proposal will affect:
- Cost: {YES_WITH_ESTIMATE | NO | TBD}
- Schedule: {YES_WITH_DAYS | NO | TBD}

---

## Response

*(To be completed by {RECIPIENT_NAME}.)*

**Response:**

_______________________________________________________________________

_______________________________________________________________________

_______________________________________________________________________

**Cost Impact Acknowledged:** ☐ Yes  ☐ No  ☐ Submit Change Order
**Schedule Impact Acknowledged:** ☐ Yes  ☐ No  ☐ Submit Change Order

**Responded By:** ___________________________
**Title:** ___________________________
**Date:** ___________________________

---

## Submitted By

{{PM_NAME}}, {{PM_TITLE}}
{{COMPANY_NAME}} · {{PM_EMAIL}} · {{PM_PHONE}}

*{{COMPANY_LEGAL_NAME}} · {{OPERATING_ADDRESS}} · {{DOMAIN}}*
```
