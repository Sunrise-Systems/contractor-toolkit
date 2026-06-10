---
name: bid-leveling
description: Compare and normalize returned subcontractor bids per trade — scope gaps, plug comparison, apples-to-apples adjustments, and an award recommendation. Use when sub bids come back after /sub-bid-package or /formal-bid. Triggers on "level these bids", "compare sub bids", "bid leveling", or "/bid-leveling".
argument-hint: "[trade name, or leave blank to level all trades with returned bids]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
  - Glob
---

# /bid-leveling — Sub Bid Comparison & Leveling

Sub bids are back. Before anyone gets awarded, normalize them so you're comparing the same scope at the same terms — then recommend an award with the reasoning that survives an owner's audit.

This closes the loop that `/sub-bid-package` opens: invitation → bids returned → **level** → select → `/subcontract`.

## Inputs Needed

1. **The bids** — PDFs, emails pasted in, or numbers dictated. Per bidder: base bid, alternates, unit prices, stated exclusions, stated inclusions, bond/insurance notes, schedule commitments.
2. **The bid package** — the scope each sub was asked to price (from `/sub-bid-package` output in the working directory, or described by the user).
3. **The plug** — your internal estimate for the trade from Phase 5. If a cost breakdown DOCX exists in the working directory, pull it; otherwise ask.

## Process

### 1. Build the scope baseline
List every scope item from the bid package for the trade. This is the row set for the leveling matrix — bids are measured against the package, not against each other.

### 2. Normalize each bid
For each bidder, mark every scope item: **Included / Excluded / Silent / Qualified**. "Silent" is not "included" — flag it as a risk. Capture:
- Stated exclusions that conflict with the package scope
- Items priced as allowances rather than firm
- Alternates and unit prices
- Bond capacity, insurance compliance, schedule commitment

### 3. Apples-to-apples adjustments
For every gap, add a **plug adjustment**: the cost to buy the missing scope elsewhere (use Phase 5 unit costs). Adjusted bid = base bid + gap plugs − scope the bidder included that others were told to exclude. Show the math per adjustment.

### 4. The leveling matrix

```
TRADE: HVAC (Division 23)                    Plug: $186,000
──────────────────────────────────────────────────────────────────
Scope Item                    Sub A       Sub B       Sub C
──────────────────────────────────────────────────────────────────
(2) 5-ton RTU replacement     Incl        Incl        Incl
Ductwork distribution         Incl        Incl        EXCL +$22k
BMS connection                Incl        SILENT +$8k Incl
Permits & fees                Incl        Incl        Qualified
──────────────────────────────────────────────────────────────────
Base Bid                      $192,000    $171,500    $158,000
Adjustments                   —           +$8,000     +$22,000
ADJUSTED BID                  $192,000    $179,500    $180,000
vs. Plug                      +3.2%       −3.5%       −3.2%
──────────────────────────────────────────────────────────────────
```

### 5. Recommendation
Rank on adjusted bid, then qualify with non-price factors (scope confidence, schedule, bond, past performance if the user offers it). State the recommendation and the negotiation angle, using the Phase 5 pricing rationale: *"Sub A is $12.5k over our plug; RS Means supports $X–$Y for this scope in our market — here's the conversation to have."*

## Outputs

- **HTML leveling sheet** (primary, one per trade) — leveling matrix, adjustments with math, recommendation. Styled per `contractor-docs` canonical HTML. `{company-slug}_bid-leveling_{trade}_{project-slug}_{YYYY-MM}.html`
- **XLSX workbook** (optional, on request) — one tab per trade, formulas live so the PM can test scenarios. Generated via openpyxl.

## Rules

1. **Never average bids.** Each bid is leveled against the package scope, not against the other bids.
2. **Silent ≠ included.** Price every silence as a gap until the sub confirms in writing.
3. **Show every adjustment's math.** An unexplained adjustment is an argument waiting to happen.
4. **Low bid is a finding, not a decision.** If the low bid is >10% under the plug, treat it as a scope-gap signal and say so.
5. **This document is internal.** It never goes to subs or the owner — it contains your plug.

## Transition

```
Leveling sheet is at [path]. Recommendation: [Sub], adjusted $[X] ([±Y]% vs plug).

Next steps:
1. Confirm the silent/qualified items with [Sub] in writing
2. /subcontract to issue their agreement once confirmed
3. Re-run /formal-bid pricing if awarded numbers move the estimate
```
