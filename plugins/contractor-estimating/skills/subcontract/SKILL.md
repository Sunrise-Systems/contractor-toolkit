---
name: subcontract
description: Generate a subcontract agreement for an awarded trade — scope exhibit from the bid package, leveled price, flow-down provisions, insurance and retention terms, signature blocks. Use after /bid-leveling selects a sub. Triggers on "issue the subcontract", "subcontract for [trade]", or "/subcontract".
argument-hint: "[trade or sub name, or leave blank to select from leveled trades]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
  - Glob
---

# /subcontract — Subcontract Agreement Generator

The prime contract covers you and the owner. This covers you and the sub. Generate a signable subcontract agreement from the awarded bid — scope from the bid package, price from the leveling sheet, terms that flow down from the prime.

Runs after `/bid-leveling` (award decided) and ideally after `/contract` (prime executed, so flow-downs reference a real document).

## Inputs Needed

1. **Awarded sub** — legal entity name, license number and classification, address, signatory
2. **The trade scope** — from the `/sub-bid-package` output, adjusted for anything negotiated during leveling
3. **Subcontract sum** — the awarded amount from `/bid-leveling`, plus accepted alternates
4. **Prime contract reference** — project, owner, prime contract date (from `/contract` output if present)
5. **Schedule** — the sub's work window and milestones
6. **Commercial terms** — retention % (default: match the prime), payment timing, insurance limits required of the sub

## Document Structure

1. **Parties & project block** — Contractor ({{COMPANY_LEGAL_NAME}}), Subcontractor (legal name + license), Project, Prime Contract reference
2. **Scope of Work (Exhibit A)** — the bid package scope verbatim, plus negotiated clarifications from leveling. Include the sub's confirmed inclusions of previously-silent items.
3. **Subcontract Sum** — base + alternates, in words and figures
4. **Payment terms** — progress payments tied to Contractor's receipt of corresponding owner payment where state law allows (pay-when-paid language is state-sensitive — **flag for attorney review**), retention %, conditions to final payment (lien waivers, warranties, closeout docs)
5. **Flow-down clause** — sub bound to Contractor as Contractor is bound to Owner under the prime contract, for the sub's scope
6. **Schedule** — work window, coordination obligations, recovery obligations if the sub falls behind
7. **Changes** — written change orders only; markup limits on changed work
8. **Insurance & indemnity** — CGL/auto/WC limits, additional insured + waiver of subrogation in favor of Contractor and Owner, indemnification (**state-sensitive — flag for attorney review**)
9. **Safety** — compliance with Contractor's site safety program and OSHA
10. **Warranty** — match the prime's correction period for the sub's scope
11. **Default & termination** — notice + cure, supplementation rights, termination for convenience
12. **Lien waiver schedule (Exhibit B)** — conditional progress waiver with each payment application, unconditional final at closeout
13. **Signature blocks** — both entities, with license numbers

## Process

1. Locate the leveling sheet and bid package for the trade (Glob the working directory); confirm the awarded number with the user
2. Assemble the agreement per the structure above — `[BRACKETED CAPS]` for any unknown fill point, never silently blank
3. Generate DOCX via `contractor-docs` styling (white pages, hairlines, no color)
4. Save as `{{COMPANY_NAME}}_Subcontract_[Trade]_[ProjectName]_[YYYY-MM-DD].docx`

## Rules

1. **Scope must match the leveled scope exactly** — the negotiated gaps from `/bid-leveling` get written in as explicit inclusions. That's the whole point of leveling.
2. **Subcontract sum must match the award.** No re-derivation.
3. **Use legal entity names** on both sides, with license numbers.
4. **Pay-when-paid / pay-if-paid and indemnity clauses vary by state.** Generate neutral versions and flag both for attorney review — always, every time.
5. **Attorney review before signature.** This output is a drafting aid, not legal advice. Same caveat as `/contract`.

## Transition

```
Subcontract for [Trade] is at [path].

Before sending:
1. Attorney review — payment and indemnity clauses are state-sensitive
2. Verify the sub's license is active and insurance certs are current
3. Attach the prime contract reference documents

After signature: collect their COI naming you + owner as additional insured,
then release them to schedule.
```
