---
name: sub-pay-app
description: Build a monthly progress payment application against a schedule of values — percent complete, previous billings, stored materials, retainage math, and the lien waiver reminder. Use when the user says "pay app", "progress billing", "monthly invoice to the GC", or "/sub-pay-app".
argument-hint: [application number or billing period]
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(python3 *toolkit_guard.py *)
---

# /sub-pay-app — Progress Payment Application

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** SOV, approved contract/change values, progress and stored-material evidence, retainage terms, previous application identity and prior earned amount.
- **Output:** Reconciled DOCX/XLSX payment application draft, linked prior-period evidence and receipt.
- **AI role:** Extract, reconcile and draft; independently reopen exact saved paths, not merely trust a successful generator call.
- **Human role:** Authorized billing reviewer confirms entitlement, progress, retainage, prior-period reconciliation and approved amount.
- **Risk:** Financial: consequential output; no payment certification or lien release.
- **Checkpoint:** Project-specific output directory with local `checkpoints/` for immutable prior revisions, source/artifact hashes, content expectations, approvals and receipts; outside package inputs.
- **Approval boundary:** Named human approval of exact project/entities/revision, dates, amount/currency where relevant, recipients/use, assumptions/exceptions and semantic-content digest. Material edits or regeneration invalidate approval. Final verified is not issued: issuance remains `not_issued`; no transmission, signature or external mutation.
- **Verifier:** `python3 "$GUARD" verify-artifact --artifact "$ARTIFACT" --expectations "$EXPECTATIONS" --receipt "$RECEIPT"`; check approved semantic fields separately from final-file digest. Required domain/visual checks must also pass.
- **Failure:** Missing evidence, stale approval/receipt or unavailable checks become `needs_human`; keep draft/checkpoint, identify owner and next safe action, withhold final status.



The monthly billing ritual. Build a payment application against your schedule of values: what's complete, what was billed before, what's due now, with retainage math that actually adds up. Follows the G702/G703 continuation-sheet conventions GCs expect, without reproducing AIA forms (if the GC mandates actual AIA forms, this output gives you every number to transcribe).

## Inputs Needed

1. **Application number and period** — App #N, period ending date; check the working directory for the prior app
2. **The schedule of values** — line items with scheduled values, from the subcontract Exhibit (first run establishes it; later runs reuse it). SoV total must equal the subcontract sum + approved COs.
3. **Progress this period** — % complete per SoV line (or completed $ amount)
4. **Stored materials** — on-site or bonded-warehouse materials not yet installed, with invoice backup
5. **Approved change orders** — added as new SoV lines, never blended into base lines
6. **Retainage rate** — from the subcontract (typically 5–10%); record separate stored-material/work rates or release terms where applicable
7. **Prior-period linkage** — exact project, previous application identity/hash, prior earned amount and approved adjustments; no prior app may be assumed from a similar filename

## The Continuation Sheet

```
SCHEDULE OF VALUES — APPLICATION #4, PERIOD ENDING [date]
─────────────────────────────────────────────────────────────────────────────
Item  Description        Sched.    Prev.     This      Stored   Total     %    Balance
                         Value     Billed    Period    Mat'l    to Date        to Finish
─────────────────────────────────────────────────────────────────────────────
1     Mobilization       $8,000    $8,000    —         —        $8,000    100  —
2     Rough-in L1        $64,000   $48,000   $16,000   —        $64,000   100  —
3     Rough-in L2        $64,000   $12,800   $25,600   —        $38,400   60   $25,600
4     Fixtures           $41,000   —         —         $12,300  $12,300   30   $28,700
CO1   Added BMS scope    $8,400    —         $4,200    —        $4,200    50   $4,200
─────────────────────────────────────────────────────────────────────────────
TOTALS                   $185,400  $68,800   $45,800   $12,300  $126,900       $58,500
```

## The Summary Math

```
1. Original subcontract sum                    $177,000
2. Net change by approved COs                  $8,400
3. Subcontract sum to date (1+2)               $185,400
4. Total completed & stored to date            $126,900
5. Retainage ([X]% of line 4)                  $(12,690)
6. Total earned less retainage (4−5)           $114,210
7. Less previous applications                  $(61,920)
8. CURRENT PAYMENT DUE                         $52,290
9. Balance to finish, incl. retainage          $71,190
```

Use Decimal arithmetic with the contract's explicit rounding and retainage basis. Verify every cross-foot before output: continuation sheet totals must equal line 4; line 7 must reconcile to the verified prior app's line 6 plus explicitly approved corrections. SOV must reconcile to approved contract/change values; pending requests are not billable merely because extracted. If the numbers don't tie, stop and reconcile — a pay app that doesn't tie gets rejected and costs a month.

## Outputs

- **Pay application package** — summary page + continuation sheet, DOCX or XLSX (XLSX preferred — GCs check the math): `{company-slug}_payapp_{NN}_{project-slug}_{period}.xlsx`
- **Conditional lien waiver reminder** — every app closes with: "Attach a conditional waiver for this period's amount. Unconditional waivers only for payments already received." Waiver forms are state-prescribed in many states (CA, AZ, TX…) — use the state's statutory form, don't improvise one.

## Rules

1. **Only approved COs get billed.** Pending CORs stay off the SoV — bill them the month they're signed.
2. **Bill only substantiated progress within approved terms.** The billing reviewer confirms entitlement; never infer it from extraction, overstate completion, or treat pending changes as approved.
3. **Stored materials need backup** — vendor invoice + photo or warehouse receipt, every time.
4. **Retainage math compounds across apps** — always recompute from totals-to-date, never increment.
5. **Track retainage release** — at your scope's completion, note the accumulated retainage and prompt the user to request release per the subcontract terms.
