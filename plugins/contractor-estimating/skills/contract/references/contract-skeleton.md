# Generic Construction Contract Skeleton

A generic fixed-sum construction agreement structure for when no licensed boilerplate (AIA, ConsensusDocs, EJCDC) is available. This is an **article outline with neutral working language** — it follows the article structure the industry expects, but it is NOT AIA text and is NOT legal advice.

> **Legal disclaimer — surface this to the user every time this skeleton is used:**
> This skeleton is a drafting aid. The generated contract MUST be reviewed by a licensed attorney in the project's jurisdiction before signature. If the company holds an AIA license, prefer the licensed A201 document — place it at `plugins/contractor-brand/skills/brand/resources/AIA_A201_GeneralConditions.docx` and `/contract` will use it instead of this skeleton.

## Document structure

```
COVER — Agreement title, parties, project, date
ARTICLES 1–15 — General terms (below)
SIGNATURE PAGE — Owner, Contractor, (Architect acknowledgment if applicable)
EXHIBITS A–F+ — Scope, SoV, Exclusions, Payment Terms, Insurance, Riders
```

## Article outline

### Article 1 — The Contract Documents
The contract consists of this Agreement, the listed Exhibits, the Drawings and Specifications enumerated in Exhibit A, and any Modifications issued after execution. List every document by title, date, and revision. State the order of precedence when documents conflict (typically: Modifications > this Agreement > Exhibits > Specifications > Drawings).

### Article 2 — The Work
Define the Work by reference to Exhibit A (Scope of Work). State what the Contractor is and is not responsible for at the boundary (by reference to Exhibit C — Exclusions & Clarifications).

### Article 3 — Date of Commencement and Substantial Completion
- Commencement date (fixed date or upon Notice to Proceed)
- Substantial Completion date or duration in calendar days
- Liquidated damages, if any (rate per day, cap) — flag to attorney if included
- Extensions of time: causes beyond Contractor's control (weather per local norms, owner changes, concealed conditions, regulatory delay)

### Article 4 — Contract Sum
- Fixed Contract Sum in words and figures (must match the accepted formal bid exactly)
- Enumerate accepted alternates
- Enumerate allowances (from the estimate's "Budgetary Allowance" items) and the true-up mechanism
- Unit prices, if any

### Article 5 — Payments
- Application schedule (typically monthly, per Exhibit B Schedule of Values)
- Application cut-off date and payment due date
- Retainage percentage and release terms (at Substantial Completion / Final Completion)
- Conditions to final payment (closeout deliverables, lien releases, warranties)
- Interest on late payments per applicable state statute

### Article 6 — Dispute Resolution
- Initial decision maker (Architect, or direct negotiation if none)
- Mediation as condition precedent
- Binding arbitration or litigation election; venue and governing law (project state)

### Article 7 — Termination and Suspension
- Termination by Owner for cause (notice + cure period) and for convenience (payment for work executed + reasonable demobilization)
- Termination by Contractor (nonpayment, extended suspension)
- Suspension by Owner: time + cost adjustment

### Article 8 — Changes in the Work
- Changes only by written Change Order stating cost and time impact
- Construction Change Directive mechanism for disputed changes (proceed + reserve rights)
- Markup limits on changed work (state OH&P % on self-performed and subcontracted changes)
- Minor changes not affecting cost/time may be ordered in writing without CO

### Article 9 — Time
- Time is of the essence
- Delay claims: notice period (typically 21 days from event), substantiation requirements
- No damages for delay clauses are state-sensitive — flag to attorney

### Article 10 — Protection of Persons and Property
- Contractor responsible for site safety programs and OSHA compliance
- Protection of adjacent property and existing improvements
- Hazardous materials: discovery procedure, Owner responsibility for pre-existing hazmat unless estimate includes abatement

### Article 11 — Insurance and Bonds
Reference Exhibit E. Typical schedule:
- Commercial General Liability (per-occurrence and aggregate limits)
- Auto liability, Workers' Compensation (statutory), Employer's Liability
- Builder's Risk (state who carries it — Owner or Contractor)
- Umbrella/excess if required
- Additional insured + waiver of subrogation requirements
- Performance and Payment bonds if required (public work or by Owner election)

### Article 12 — Uncovering and Correction of Work
- Correction of rejected/nonconforming work at Contractor's cost
- One-year correction period from Substantial Completion (distinct from warranties)
- Uncovering work for inspection: who pays depending on notice and conformance

### Article 13 — Miscellaneous Provisions
- Governing law (project state); successors and assigns; no assignment without consent
- Written notice requirements and addresses (pull from the parties block)
- Severability; survival of payment/warranty/indemnity obligations
- Mutual waiver of consequential damages — flag to attorney
- Indemnification (state-law-sensitive; flag to attorney)

### Article 14 — Concealed and Unforeseen Conditions
- Differing site conditions: notice within stated days of discovery, equitable adjustment mechanism
- Reference the estimate's standard qualification: "Does not include costs for unforeseen conditions"

### Article 15 — Warranties
- Workmanship warranty (typically 1 year from Substantial Completion unless company standard differs)
- Pass-through of manufacturer warranties at closeout
- Warranties survive termination/final payment

## Exhibit templates

| Exhibit | Content | Source |
|---|---|---|
| A — Scope of Work | Division-by-division scope | Formal bid Phase 2 output |
| B — Schedule of Values | Division totals | Formal bid SoV |
| C — Exclusions & Clarifications | Filtered lists | `/exclusions-excel` output |
| D — Payment Terms | Company standard schedule | `.claude/contractor-estimating.local.md` |
| E — Insurance & Bonds | Coverage schedule | Company COIs |
| F+ — Project Riders | Per project type | `/contract` rider table |

## Fill conventions

Use `[BRACKETED CAPS]` for every fill point in the generated DOCX (e.g., `[OWNER LEGAL NAME]`, `[CONTRACT SUM]`). Never leave a fill point silently blank — if a value is unknown at generation time, keep the bracket so it's visible in legal review.
