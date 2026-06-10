---
name: contract
description: Generate a curated AIA A201-based construction contract from an accepted estimate. Fills in project-specific blanks, attaches scope + exclusions as exhibits, adds standard payment/insurance terms, and applies project-type riders. Outputs a signable DOCX.
argument-hint: "[path to accepted estimate, or leave blank to select from recent formal bids]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /contract — AIA A201 Contract Curator

Generate a project-specific construction contract from an accepted estimate using the AIA A201 General Conditions as the boilerplate. *Contract templates / terms / clarifications — boilerplate legal and clarification language per project type.*

## When to Use This

- A formal bid has been accepted by the client
- Client has approved the scope, exclusions, and price
- You need a signable contract — NOT a proposal
- Runs AFTER `/formal-bid` has produced the proposal + exclusions workbook

## What This Produces

Two deliverables:

1. **Contract Preview HTML** (primary for review) — Cover tag: "Construction Contract — Preview". Summarizes party info, contract sum, exhibits list, applied riders. Save as `contractor_contract_preview_[project-slug]_[YYYY-MM].html`. This is what the owner and estimator review BEFORE the signable DOCX is generated.

2. **Contract DOCX** (signable) — ready for signature, assembled from:

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

When the project matches these types, append the corresponding rider to the base A201:

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

1. **Do not modify the AIA A201 base articles.** The 15 Articles are legal boilerplate — any changes must be made via Modifications (Article 16+ via rider) not by editing base text.
2. **Use the exact legal names** — your company's registered legal entity name, not marketing name.
3. **Contract sum must match the accepted formal bid exactly.** No rounding, no estimation range. The contract is a fixed number.
4. **All exhibits must be dated and version-stamped** — if the formal bid was revised, track which revision is attached.
5. **Architect of Record is listed as a contract party** under AIA — make sure the architect's signature block is included.
6. **Review with legal before sending.** Output is 85-90% done; the last 10-15% is legal review.
7. **AIA documents are copyrighted.** If you don't have an AIA license, use ConsensusDocs, EJCDC, or your attorney's custom boilerplate as the base.

## Transition

At delivery, end with:

```
Contract is ready at [path].

Before sending to the client:
1. Have legal review the exhibits and any applied riders
2. Verify all contact information and signature blocks
3. Confirm insurance certificates are current
4. Schedule the signing with the owner and architect

Once signed: issue Notice to Proceed (NTP) and schedule pre-construction kickoff.
```
