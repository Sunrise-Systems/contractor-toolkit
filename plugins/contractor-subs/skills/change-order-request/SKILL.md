---
name: change-order-request
description: Generate a change order request (COR/PCO) from a subcontractor to the GC — cause, cost breakdown with labor/material/equipment/markup, schedule impact, and backup documentation list. Use when the user says "COR", "change order request", "we need to get paid for this extra", or "/change-order-request".
argument-hint: [COR number or short description of the change]
---

# /change-order-request — COR to the GC

Extra work happened, or is about to. Generate the change order request that gets it paid: what changed, why it's not in your contract, what it costs, and the paper that proves it. The GC's version of this document is `/change-order` (them → owner); this is yours (you → them) — and yours usually has to survive being passed through to the owner, so write it for two audiences.

## Inputs Needed

1. **COR number** — sequential per project (COR-NNN); check the working directory for prior CORs
2. **The change** — what work is added/changed, where, and current status (not started / directed to proceed / already performed)
3. **The cause** — the single most important field. One of:
   - **RFI response** — cite RFI number and response date
   - **Drawing revision** — cite revision/delta and date received
   - **Field directive** — who directed it, when, verbal or written (CCD number if any)
   - **Concealed condition** — what was found vs. what documents showed; discovery date and notice given
   - **Owner/GC change** — the request and who made it
4. **Cost detail** — labor (hours × rate by classification), material (vendor quotes), equipment, subcontractor (if you have lower tiers)
5. **Schedule impact** — days, and whether it hits the critical path
6. **Backup** — T&M tickets (`/tm-ticket`), photos, RFI copies, vendor quotes, directive emails

## Document Structure

```
[YOUR COMPANY] — CHANGE ORDER REQUEST COR-003
To: [GC]   Project: [name]   Subcontract: [ref #]   Date: [date]

DESCRIPTION OF CHANGE
[What work, where, scope delta from subcontract Exhibit A]

CAUSE / ENTITLEMENT
[Why this is extra — citing the RFI/revision/directive/condition with
dates. This section wins or loses the COR.]

COST BREAKDOWN
Labor        [class] [hrs] × $[rate]     $[X]
Material     [item, vendor quote ref]    $[X]
Equipment    [item, duration]            $[X]
Subtotal                                 $[X]
Overhead & Profit ([X]% per subcontract) $[X]
TOTAL THIS COR                           $[X]

SCHEDULE IMPACT: [N] calendar days [— critical path / — absorbed]

BACKUP ATTACHED: [numbered list]

This COR is valid 30 days. Work [will not proceed / proceeded under
directive dated X / is complete] pending your written approval.
```

## Rules

1. **Entitlement before arithmetic.** A perfect cost breakdown with weak cause language gets rejected; state the contractual basis plainly and cite documents by number and date.
2. **Markup per the subcontract.** Use the OH&P % your subcontract allows on changes — not your wish.
3. **Notice timing matters.** If the subcontract requires notice within N days of discovery, state the discovery date and notice date in the cause section. Late notice is the #1 COR-killer; if notice is already late, say so to the user and frame the COR accordingly.
4. **Never proceed silently.** If work hasn't started, the COR says so. If directed to proceed, name who directed it and attach the directive. If already done, lead with the T&M tickets.
5. **Track the log.** Keep a running COR register (number, status, amount, days outstanding) in the working directory; offer the summary whenever a new COR is created.
