---
name: contract
description: Generate a curated AIA A201-based construction contract from an accepted estimate. Fills in project-specific blanks, attaches scope + exclusions as exhibits, adds standard payment/insurance terms, and applies project-type riders. Outputs an unsigned DOCX draft for legal review.
argument-hint: "[path to accepted estimate, or leave blank to select from recent formal bids]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /contract — AIA A201 Contract Curator

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** Accepted bid identity/revision and accepted commercial values, parties, licensed boilerplate or explicitly identified generic skeleton.
- **Output:** Contract preview HTML, unsigned DOCX draft, exhibits and verification receipts.
- **AI role:** Extract, reconcile and draft; independently reopen exact saved paths, not merely trust a successful generator call.
- **Human role:** Authorized commercial reviewer and authorized legal review; counsel selects agreement forms, legal parties, riders and signature requirements.
- **Risk:** Legal: consequential output; no legal sufficiency claim.
- **Checkpoint:** Project-specific output directory with local `checkpoints/` for immutable prior revisions, source/artifact hashes, content expectations, approvals and receipts; outside package inputs.
- **Approval boundary:** Named human approval of exact project/entities/revision, dates, amount/currency where relevant, recipients/use, assumptions/exceptions and semantic-content digest. Material edits or regeneration invalidate approval. Final verified is not issued: issuance remains `not_issued`; no transmission, signature or external mutation.
- **Verifier:** `python3 "$GUARD" verify-artifact --artifact "$ARTIFACT" --expectations "$EXPECTATIONS" --receipt "$RECEIPT"`; check approved semantic fields separately from final-file digest. Required domain/visual checks must also pass.
- **Failure:** Missing evidence, stale approval/receipt or unavailable checks become `needs_human`; keep draft/checkpoint, identify owner and next safe action, withhold final status.



Generate a project-specific construction contract from an accepted estimate using a counsel-selected agreement and, where appropriate, licensed AIA A201 General Conditions. A201 alone is not the owner-contractor agreement. *Contract templates / terms / clarifications — boilerplate legal and clarification language per project type.*

## When to Use This

- A formal bid has been accepted by the client
- Client has approved the scope, exclusions, and price
- You need a contract draft for legal review — NOT a proposal
- Runs AFTER `/formal-bid` has produced the proposal + exclusions workbook

## What This Produces

Two deliverables:

1. **Contract Preview HTML** (primary for review) — Cover tag: "Construction Contract — Preview". Summarizes party info, contract sum, exhibits list, applied riders. Save as `contractor_contract_preview_[project-slug]_[YYYY-MM].html`. This is what the owner and estimator review before final content approval.

2. **Contract DOCX** (unsigned draft) — assembled for legal review from:

   1. **Base boilerplate** — resolved in this order:
      a. `plugins/contractor-brand/skills/brand/resources/AIA_A201_GeneralConditions.docx` — the company's licensed AIA boilerplate, if they've placed it there (preferred; AIA documents are copyrighted and not bundled)
      b. Any other licensed base the company specifies (ConsensusDocs, EJCDC, attorney-drafted)
      c. **Fallback (ships with this skill):** `references/contract-skeleton.md` — a generic 15-article structure with neutral working language. When using the skeleton, state plainly that the output is NOT AIA text and MUST go through attorney review before signature.
   2. **Project-specific fills** — Owner name/address, Architect name/address, Contractor ({{COMPANY_NAME}}), Project name/location, Contract sum, dates
   3. **Scope exhibit** — Division-by-division scope pulled from the formal bid
   4. **Schedule of Values exhibit** — Pulled from the formal bid
   5. **Exclusions & Inclusions exhibit** — Pulled from `/exclusions-excel` workbook or formal bid inline exclusions
   6. **Payment terms rider** — Your company's standard payment schedule
   7. **Insurance & bonds rider** — Your insurance certificates and bond requirements
   8. **Project-specific riders** — Hillside, healthcare, occupied-adjacent, historic preservation, etc.

## Inputs Needed

Preferably pull from an existing formal bid artifact. If running standalone:

1. **Owner** — full legal name, entity type (LLC, Trust, individual), mailing address
2. **Architect of Record** — firm name, license number, address
3. **Project** — name, full address, APN if available, building type
4. **Contract Sum** — from accepted formal bid
5. **Contract Dates** — effective date, substantial completion target, final completion target
6. **Scope** — from `/formal-bid` output
7. **Exclusions** — from `/exclusions-excel` or formal bid inline exclusions
8. **Contractor entity** — which {{COMPANY_NAME}} division is party to the contract (if multiple divisions exist)
9. **Project-specific risk factors** — triggers riders

## Project Type Riders

When the project matches these types, propose the corresponding rider for counsel review; do not assume entitlement or legal applicability:

| Project Type | Rider Content |
|--------------|---------------|
| **Hillside / steep site** | Hillside grading premium acknowledgment, unforeseen subsurface conditions allocation, shoring of adjacent improvements, stormwater management plan |
| **Healthcare (state-licensed)** | State hospital-authority compliance scope, infection control during construction, medical gas trade coordination, life-safety pathway maintenance |
| **Restaurant / Food Service** | Grease trap / interceptor scope, Type I hood commissioning, health department coordination, tenant fixture/equipment protocol |
| **Occupied-adjacent TI** | After-hours work provisions, dust/noise/vibration protection, tenant notification schedule, life-safety pathway, landlord approval requirements |
| **Historic / Preservation** | Preservation authority coordination scope, matching-material specifications, historical fabric protection plan, tax credit compliance if applicable |
| **Phased work / Live environment** | Swing-space coordination, sequencing requirements, operational continuity commitments |
| **Public works** | Prevailing wage compliance, certified payroll, bonding requirements |

## Process

1. **Locate accepted estimate** — user provides path OR picks from recent formal bids in working directory
2. **Extract project data** — parse the formal bid DOCX for: project name, address, owner, architect, contract sum, scope divisions, exclusions list
3. **Load contract base** — Glob for the licensed boilerplate first; fall back to `references/contract-skeleton.md` and announce which base is in use
4. **Fill placeholder fields** — the A201 has `«»` French-quote placeholders for project name, owner, architect, etc. Replace with project-specific values.
5. **Identify riders** — based on project type + risk factors, select applicable riders
6. **Append exhibits:**
   - Exhibit A: Scope of Work (from formal bid, division-by-division)
   - Exhibit B: Schedule of Values (from formal bid)
   - Exhibit C: Exclusions & Inclusions (from exclusions workbook or formal bid)
   - Exhibit D: Payment Terms ({{COMPANY_NAME}} standard)
   - Exhibit E: Insurance & Bonds
   - Exhibit F+: Project-specific riders
7. **Generate signature pages** — Owner, Contractor ({{COMPANY_NAME}}), Architect witness if applicable
8. **Save as DOCX** — `{{COMPANY_NAME}}_Contract_[ProjectName]_[YYYY-MM-DD].docx`

## Output Styling

The A201 base document has its own AIA formatting (which must NOT be modified — it's industry-standard). Exhibits and riders use the styling from `contractor-docs`:

- Arial 10pt body
- Section labels for exhibit headings
- Info tables for contract metadata
- Line item tables for scope + SoV
- Hairlines between sections
- No color, no fills, no accent

## Critical Rules

1. **Preserve licensed boilerplate unless counsel authorizes exact modifications.** Counsel chooses the appropriate supplementary conditions/rider mechanism; do not invent AIA articles.
2. **Use the exact legal names** — your company's registered legal entity name, not marketing name.
3. **Contract sum must match the accepted formal bid exactly.** No rounding, no estimation range. The contract is a fixed number.
4. **All exhibits must be dated and version-stamped** — if the formal bid was revised, track which revision is attached.
5. **Do not assume the architect is a contracting party.** Counsel confirms parties and any required witness/signature blocks under the selected agreement.
6. **Authorized legal review is mandatory before finalization.** Do not quantify completeness or imply the draft is legally sufficient.
7. **AIA documents are copyrighted.** If you don't have an AIA license, use ConsensusDocs, EJCDC, or your attorney's custom boilerplate as the base.

## Handoff

Present exact paths/status, accepted-bid revision and digest, reconciled commercial values, selected legal base, unresolved issues, approvals and readback receipts. Unsigned drafts stay `needs_review` until authorized legal review and all artifact checks pass. No signature, issuance, Notice to Proceed or scheduling action is performed by this skill.
