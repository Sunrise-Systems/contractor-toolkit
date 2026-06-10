---
name: sub-pay-app
description: Build a monthly progress payment application against a schedule of values — percent complete, previous billings, stored materials, retainage math, and the lien waiver reminder. Use when the user says "pay app", "progress billing", "monthly invoice to the GC", or "/sub-pay-app".
argument-hint: [application number or billing period]
---

# /sub-pay-app — Progress Payment Application

The monthly billing ritual. Build a payment application against your schedule of values: what's complete, what was billed before, what's due now, with retainage math that actually adds up. Follows the G702/G703 continuation-sheet conventions GCs expect, without reproducing AIA forms (if the GC mandates actual AIA forms, this output gives you every number to transcribe).

## Inputs Needed

1. **Application number and period** — App #N, period ending date; check the working directory for the prior app
2. **The schedule of values** — line items with scheduled values, from the subcontract Exhibit (first run establishes it; later runs reuse it). SoV total must equal the subcontract sum + approved COs.
3. **Progress this period** — % complete per SoV line (or completed $ amount)
4. **Stored materials** — on-site or bonded-warehouse materials not yet installed, with invoice backup
5. **Approved change orders** — added as new SoV lines, never blended into base lines
6. **Retainage rate** — from the subcontract (typically 5–10%)

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

Verify every cross-foot before output: continuation sheet totals must equal line 4; line 7 must equal the prior app's line 6. If the numbers don't tie, stop and reconcile — a pay app that doesn't tie gets rejected and costs a month.

## Outputs

- **Pay application package** — summary page + continuation sheet, DOCX or XLSX (XLSX preferred — GCs check the math): `{company-slug}_payapp_{NN}_{project-slug}_{period}.xlsx`
- **Conditional lien waiver reminder** — every app closes with: "Attach a conditional waiver for this period's amount. Unconditional waivers only for payments already received." Waiver forms are state-prescribed in many states (CA, AZ, TX…) — use the state's statutory form, don't improvise one.

## Rules

1. **Only approved COs get billed.** Pending CORs stay off the SoV — bill them the month they're signed.
2. **Don't front-load beyond defensibility.** Overbilling early feels good until the GC's PM walks the site; underbilling is donating float to the GC. Bill what you can defend in a walk.
3. **Stored materials need backup** — vendor invoice + photo or warehouse receipt, every time.
4. **Retainage math compounds across apps** — always recompute from totals-to-date, never increment.
5. **Track retainage release** — at your scope's completion, note the accumulated retainage and prompt the user to request release per the subcontract terms.
