---
name: change-order
description: Generate a formal change order document in AIA G701-style format with cost impact, schedule impact, and signature blocks. Use when the user says "draft a change order", "CO for [project]", "change order", or "/change-order".
argument-hint: [CO number or project]
---

# Change Order

Generate a formal change order (CO) modifying an existing contract. Output mirrors the AIA G701 format that owners, architects, and lenders expect. Goes through `contractor-docs` for DOCX or PDF.

Use this any time scope, cost, or schedule changes after contract execution. Document it before the work proceeds.

---

## Inputs Needed

Gather in three chunks.

### 1. Contract Reference
- Original contract number / date
- Project name and address
- Owner name and address
- Architect name (if applicable)
- This CO number (CO-001, CO-002, etc.)

### 2. Scope of Change
- Description of the change (additive, deductive, or substitution)
- Reason for the change (owner request, field condition, design change, code requirement)
- Affected drawings or spec sections
- Reference RFI numbers (if the change originated from an RFI)

### 3. Impact
- Cost impact: amount added or deducted (with backup if requested)
- Schedule impact: calendar days added (or none)
- New contract sum after this CO
- New substantial completion date after this CO

---

## Workflow

```
1. INTAKE     → Contract ref, scope, impact
2. CALCULATE  → New contract sum and new completion date
3. DRAFT      → Formal CO document
4. REVIEW     → User confirms numbers and language
5. EXPORT     → contractor-docs renders DOCX with signature lines
```

If cost impact is unclear, ask whether to include a backup cost breakdown table.

---

## Output

A one- to two-page DOCX with:

1. Header block — "CHANGE ORDER" + CO number, project, dates
2. Parties block — Owner, Contractor (`{{COMPANY_NAME}}`), Architect
3. Original contract reference
4. Description of change
5. Cost impact summary
6. Schedule impact summary
7. Running contract sum table (original → previous COs → this CO → new total)
8. Signature block — Owner, Contractor, Architect

---

## Template

```markdown
# CHANGE ORDER

**Change Order No.:** {CO_NUMBER}
**Date:** {DATE}
**Project:** {PROJECT_NAME}
**Project Address:** {PROJECT_ADDRESS}

---

| Party | Name | Address |
|-------|------|---------|
| **Owner** | {OWNER_NAME} | {OWNER_ADDRESS} |
| **Contractor** | {{COMPANY_LEGAL_NAME}} | {{OPERATING_ADDRESS}} |
| **Architect** | {ARCHITECT_NAME} | {ARCHITECT_ADDRESS} |

**Original Contract Date:** {CONTRACT_DATE}
**Original Contract No.:** {CONTRACT_NUMBER}

---

## Description of Change

{NARRATIVE_DESCRIPTION_OF_THE_CHANGE}

**Reason:** {REASON — owner request / field condition / design change / code}
**Reference Documents:** {DRAWINGS_SPEC_SECTIONS_RFI_NUMBERS}

### Itemized Scope

| Item | Description | Amount |
|------|-------------|--------|
| 1 | {ITEM} | ${AMOUNT} |
| 2 | {ITEM} | ${AMOUNT} |
| | **Subtotal** | **${SUBTOTAL}** |
| | Overhead & Profit ({PCT}%) | ${OHP} |
| | **Total This Change Order** | **${CO_TOTAL}** |

---

## Cost Summary

| Line | Amount |
|------|--------|
| Original Contract Sum | ${ORIGINAL_SUM} |
| Net Change by Previous Change Orders | ${PREV_NET} |
| Contract Sum Prior to This Change Order | ${PRIOR_SUM} |
| **This Change Order** | **${CO_TOTAL}** |
| **New Contract Sum** | **${NEW_SUM}** |

---

## Schedule Impact

| Line | Days |
|------|------|
| Original Substantial Completion Date | {ORIGINAL_DATE} |
| Days Added by Previous Change Orders | {PREV_DAYS} |
| **Days Added by This Change Order** | **{CO_DAYS}** |
| **New Substantial Completion Date** | **{NEW_DATE}** |

---

## Acceptance

The Contract Sum and Contract Time will be changed as set forth above. The change described above and the resulting adjustment to the Contract Sum and Contract Time constitute the entire agreement of the parties regarding this change.

| Party | Signature | Printed Name | Date |
|-------|-----------|--------------|------|
| Owner | ___________________ | {OWNER_NAME} | __________ |
| Contractor | ___________________ | {{PM_NAME}}, {{PM_TITLE}} | __________ |
| Architect | ___________________ | {ARCHITECT_NAME} | __________ |

---

*{{COMPANY_LEGAL_NAME}} · {{OPERATING_ADDRESS}} · {{DOMAIN}}*
```
