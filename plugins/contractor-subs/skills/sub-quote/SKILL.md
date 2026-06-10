---
name: sub-quote
description: Respond to a GC bid invitation as a subcontractor — review the package scope against your trade, build the price, and generate a quote letter with explicit inclusions, exclusions, and alternates. Use when the user says "quote this bid invite", "respond to this bid package", "price this RFQ", or "/sub-quote".
argument-hint: "[path to the bid invitation, or paste/describe it]"
---

# /sub-quote — Bid Invitation Response

A GC sent a bid package. Read it, find what's really in scope (and what they left silent), price it, and produce a quote letter that protects your margins with explicit inclusions and exclusions. This is the mirror of the GC's `/sub-bid-package` — and gets leveled by their `/bid-leveling`, so silence costs you: anything you don't state, they'll plug at your expense.

## Inputs Needed

1. **The bid invitation** — PDF, paste, or description: scope items, quantities, specs, schedule, bid form, due date
2. **Your pricing** — unit costs / labor rates the estimator provides, or work through line items together
3. **Your standard exclusions** — trade-specific list (saved to `.claude/contractor.local.md` under `# Standard Exclusions` after first use, offered as the starting point every run after)

## Process

### 1. Scope review — before any pricing
Walk the package and classify every item: **In my trade / Not my trade / Ambiguous / Missing from package but needed**. The ambiguous and missing buckets are where subs lose money:
- "Connection to existing BMS" in an HVAC package — controls sub or you?
- Patching/painting after your penetrations — you or the GC?
- Equipment by owner, installation by you?

Present the questions list first. Each unresolved item either becomes an RFI to the GC before bid day or an explicit exclusion in the quote.

### 2. Price the confirmed scope
Line items with quantity × unit cost, labor at your rates, material with current vendor pricing, equipment, then markup. Show the math internally; the quote letter shows what you choose to show (lump sum, or unit breakdown if the form requires it).

### 3. The quote letter

```
[YOUR COMPANY] — QUOTATION
To: [GC], Attn: [estimator]      Project: [name]     Trade: [yours]
Bid Due: [date]                  Valid: 30 days

BASE BID: $[amount]

INCLUSIONS — this price includes:
  1. [Specific scope item, mirroring the package language]
  ...

EXCLUSIONS — this price does not include:
  1. [Every ambiguous item you resolved OUT]
  2. [Your standard trade exclusions, filtered to relevance]
  ...

ALTERNATES:                       UNIT PRICES:
  Alt 1: [scope] — Add $[X]         [item]: $[X]/[unit]

QUALIFICATIONS: [bond/insurance compliance, lead times, schedule
assumptions, payment terms you're bidding under]
```

## Outputs

- **Quote letter** — DOCX or HTML through `contractor-docs`, on your letterhead: `{company-slug}_quote_{gc-slug}_{project-slug}_{YYYY-MM-DD}.docx`
- **Internal pricing sheet** — your math, never sent
- **RFI list** — questions to fire at the GC before bid day, if any remain

## Rules

1. **Mirror the package's scope language** in inclusions — it makes their leveling easy and disputes hard.
2. **Never leave an ambiguous item silent.** In, out, or asked — pick one per item.
3. **Exclusions are specific.** "Excludes patching and painting at new penetrations" survives; "excludes patching" gets argued.
4. **Validity period on every quote.** Material volatility is your problem after you've signed, not before.
5. **Flag bid-form traps** — unit-price requests with no quantities, "complete per plans and specs" catch-alls, schedule acceleration buried in qualifications. Tell the user what they're agreeing to.
