---
name: proposal
description: Generate a polished client proposal — cover, project summary, scope by CSI division, schedule of values, investment summary, timeline, and terms. Use when the user says "draft a proposal", "write a proposal", "proposal for [project]", or "/proposal".
argument-hint: [project name or client]
---

# Proposal

Generate a sales proposal for a construction project. Outputs a DOCX through `contractor-docs` styled with the configured brand identity. The proposal sounds like it came from a seasoned principal in the `{{VOICE_ARCHETYPE}}` voice — not a marketing department.

Use this when a prospect has been qualified (via `/project-intake` or otherwise) and you need a formal document to send.

---

## Inputs Needed

Gather in three conversational chunks. Do not present as a form.

### 1. Project Basics
- Project name and address
- Client contact (name, title, company, email, phone)
- Project type (TI, ground-up, renovation, addition, electrical)
- Approximate square footage
- Plan status (none, schematic, permit-ready, permitted)

### 2. Scope & Pricing
- High-level scope summary (what we're building)
- Scope items grouped by CSI division (if known) or by trade
- Allowance line items vs. fixed-price items
- Total proposed price (or ranges per scope area)
- Exclusions (what is NOT in the price)

### 3. Schedule & Terms
- Estimated start date
- Estimated duration (weeks or months)
- Major milestones (mobilization, rough-in, finishes, closeout)
- Payment terms (deposit %, progress draws, retention)
- Proposal validity period (default 30 days)

---

## Workflow

```
1. INTAKE     → Gather basics, scope, schedule chunk-by-chunk
2. STRUCTURE  → Organize scope into CSI divisions or trade sections
3. DRAFT      → Generate full proposal in {{VOICE_ARCHETYPE}} voice
4. REVIEW     → Show the user, allow edits
5. EXPORT     → Send to contractor-docs for DOCX generation
```

If scope is thin, ask one clarifying question per chunk — never a list of 10 questions.

---

## Output

A DOCX document with these sections, in order:

1. **Cover** — `{{COMPANY_NAME}}` logo block, proposal title, client name, date, proposal number
2. **Cover Letter** — 3-4 paragraphs in `{{VOICE_ARCHETYPE}}` voice, signed by `{{PM_NAME}}`, `{{PM_TITLE}}`
3. **Project Summary** — narrative overview, 2-3 paragraphs
4. **Scope of Work** — organized by CSI division or trade, bullet lists
5. **Schedule of Values** — table with division, description, amount
6. **Investment Summary** — total price, allowances called out, exclusions
7. **Project Timeline** — major milestones with target dates
8. **Terms & Conditions** — payment schedule, change order policy, warranty, validity
9. **Signature Block** — client signature, `{{COMPANY_NAME}}` signature, date

---

## Template

```markdown
# Proposal — {PROJECT_NAME}

**Prepared for:** {CLIENT_NAME}, {CLIENT_TITLE}
**Prepared by:** {{COMPANY_NAME}}
**Date:** {DATE}
**Proposal #:** {PROPOSAL_NUMBER}
**Valid through:** {VALIDITY_DATE}

---

## Cover Letter

{CLIENT_FIRST_NAME},

Thank you for the opportunity to propose on {PROJECT_NAME}. After {SITE_WALK_OR_REVIEW}, we're confident this is a strong fit for our team.

A few things I want to highlight up front:

**Timeline.** We're projecting {DURATION} from {START_TRIGGER} to completion. That's based on our experience with similar {PROJECT_TYPE} work and our relationships with {CITY} permitting.

**Pricing.** Our number is comprehensive. {ALLOWANCE_CALLOUTS}. If something unexpected comes up during construction, we'll call you before it costs you a dollar.

**Why {{COMPANY_NAME}}.** {DIFFERENTIATOR_PARAGRAPH}

Best,
{{PM_NAME}}
{{PM_TITLE}}
{{PM_EMAIL}} · {{PM_PHONE}}

---

## Project Summary

{NARRATIVE_OVERVIEW}

| Field | Value |
|-------|-------|
| Project Type | {PROJECT_TYPE} |
| Address | {PROJECT_ADDRESS} |
| Square Footage | {SF} |
| Plan Status | {PLAN_STATUS} |
| Estimated Start | {START_DATE} |
| Estimated Duration | {DURATION} |

---

## Scope of Work

### Division 01 — General Requirements
- {ITEM}

### Division 02 — Existing Conditions
- {ITEM}

### Division 03 — Concrete
- {ITEM}

*(Continue through relevant CSI divisions: 04 Masonry, 05 Metals, 06 Wood/Plastics, 07 Thermal/Moisture, 08 Openings, 09 Finishes, 10 Specialties, 21 Fire Suppression, 22 Plumbing, 23 HVAC, 26 Electrical, 27 Communications, 31 Earthwork, 32 Exterior Improvements.)*

---

## Schedule of Values

| Division | Description | Amount |
|----------|-------------|--------|
| 01 | General Conditions | ${AMOUNT} |
| 02 | Demolition | ${AMOUNT} |
| ... | ... | ${AMOUNT} |
| | **Subtotal** | **${SUBTOTAL}** |
| | Contingency ({PCT}%) | ${CONTINGENCY} |
| | **Total** | **${TOTAL}** |

---

## Investment Summary

**Total Proposed Price: ${TOTAL}**

**Allowances Included:**
- {ALLOWANCE_ITEM}: ${AMOUNT}

**Exclusions:**
- {EXCLUSION}

---

## Project Timeline

| Milestone | Target Date |
|-----------|-------------|
| Contract Execution | {DATE} |
| Mobilization | {DATE} |
| Rough-In Complete | {DATE} |
| Finishes Start | {DATE} |
| Substantial Completion | {DATE} |
| Closeout & Punch | {DATE} |

---

## Terms & Conditions

- **Payment Schedule:** {DEPOSIT_PCT}% deposit, progress draws billed monthly, {RETENTION_PCT}% retention released at closeout.
- **Change Orders:** Any change in scope is documented in writing and signed before work proceeds.
- **Warranty:** {WARRANTY_TERM} on workmanship from substantial completion.
- **Validity:** This proposal is valid for 30 days from the date above.

---

## Acceptance

By signing below, the parties agree to the scope, price, and terms outlined in this proposal.

**Client:** ___________________________ Date: __________
{CLIENT_NAME}, {CLIENT_TITLE}

**{{COMPANY_NAME}}:** ___________________________ Date: __________
{{PM_NAME}}, {{PM_TITLE}}

---

*{{COMPANY_LEGAL_NAME}} · {{OPERATING_ADDRESS}} · {{DOMAIN}}*
```

Pass the filled template to `contractor-docs` for DOCX styling.
