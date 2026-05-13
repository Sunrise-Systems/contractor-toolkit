# RS Means Workflow Reference

How to use RS Means data effectively for the hard cost estimation phase. This file describes the **methodology** for using national unit cost data and adjusting it to your market — not a replacement for an RS Means subscription.

If you have an RS Means license, this is the workflow. If you don't, treat the unit cost ranges in `csi-divisions.md` as starting points and refine with your historical data.

---

## What RS Means Is

RS Means is the construction industry's standard published source for unit cost data. It publishes:

- **Building Construction Cost Data (BCCD)** — Annual reference with unit costs for ~30,000 line items, organized by CSI MasterFormat
- **City Cost Index (CCI)** — Multipliers that adjust national-average data to local markets (~700 U.S. and Canadian cities)
- **Square Foot Costs** — High-level cost-per-SF data by building type for conceptual estimating
- **Specialty data** — Mechanical, electrical, heavy construction, facility maintenance

It's the most-cited published source in U.S. construction estimating. Owners, architects, and lawyers all reference it.

---

## When to Use RS Means

| Phase | Use RS Means For | Don't Use RS Means For |
|-------|------------------|------------------------|
| ROM | Square Foot Costs by building type | Line-item takeoff |
| Conceptual Budget | Validating $/SF and major line items | Final pricing |
| Phase 5 Hard Cost | Unit cost reference for each line item | Sub bid replacement |
| Sub negotiation | Defensible reference when arguing with a sub | The sub's actual cost |

**RS Means is a benchmark, not a quote.** Your sub bids are the real numbers. RS Means is what you compare them to.

---

## The Three-Step Workflow

### Step 1: Look Up the National Average

Find the CSI-coded line item in BCCD. Note:

- **Material** ($/unit)
- **Labor** (hours/unit and $/unit)
- **Equipment** ($/unit if applicable)
- **Total Including O&P** (with subcontractor overhead and profit)

Use **Total Including O&P** as your installed unit cost — that's what subs will quote you.

### Step 2: Apply the City Cost Index

Find your city in the CCI. There are separate multipliers for:

- **Material** — typically 0.90 to 1.20 nationally
- **Installation (labor)** — typically 0.70 to 1.60 nationally (more variable than material)
- **Total** — weighted blend

For Phase 5 estimating, apply the **Total CCI** to the **Total Including O&P** national figure:

```
Local Unit Cost = National Unit Cost × (Local CCI ÷ 100)
```

Example: National BCCD shows drywall (Level 4 finish) at $2.85/SF. Local CCI for your city = 122. Local unit cost = $2.85 × 1.22 = $3.48/SF.

### Step 3: Apply Project-Specific Adjustments

CCI doesn't capture everything. Layer on:

- **Escalation** — months from the BCCD publication date to your construction midpoint, at the rate from `cost-reference.md`
- **Quantity adjustment** — small quantities cost more per unit than large quantities; large quantities at full crew productivity cost less
- **Access difficulty** — hand-carry, working overhead, occupied spaces, restricted hours
- **Schedule pressure** — compressed schedule = overtime, multiple crews, premium rates
- **Market conditions** — labor shortage, material shortage, regional rebuild demand

These layered adjustments are how you turn a published number into a real one.

---

## Common Sense Checks

For every line item, ask:

1. **Does this unit cost make intuitive sense?** If RS Means says drywall is $3/SF installed and you're carrying $7/SF, you have a problem. Investigate why.
2. **Where does this rate fall in the range?** RS Means publishes "Low / Mean / High" or 25th/50th/75th percentile rates. Pick the percentile that matches the project's complexity.
3. **Did I catch all the labor?** Material costs are easy to verify (call a supplier). Labor is where estimates miss. Cross-check against labor-hours-per-unit benchmarks.
4. **Is the crew composition right?** A "drywall crew" in RS Means assumes a specific labor mix. If your sub has only 1-person crews, productivity drops.

---

## Line Items That Most Often Diverge from RS Means

Watch for these — historical RS Means data lags reality:

| Item | Why RS Means Often Underestimates |
|------|-----------------------------------|
| Electrical materials (copper, aluminum) | Commodity price swings |
| Structural steel | Mill capacity and tariff shifts |
| Insulation (spray foam, mineral wool) | Demand spikes from energy code changes |
| Glazing (high-performance) | Demand and supply chain constraints |
| Specialty equipment (RTUs, switchgear) | Long lead times and component shortages |
| Skilled labor (electricians, plumbers, HVAC techs) | Aging workforce, shortage of new entrants |
| Asbestos / lead abatement | Regulatory changes, certified contractor pool |

When pricing these items, validate against **current sub quotes**, not RS Means.

---

## Line Items Where RS Means Is Reliable

| Item | Why It Holds Up |
|------|-----------------|
| Concrete (ready-mix, basic finishing) | Stable supply, well-defined production |
| Standard drywall, paint, ACT | High-volume commodity work |
| Carpentry rough framing | Stable labor and material |
| Standard plumbing fixtures (commercial-grade) | Mature supply chain |
| Doors and hardware (HM, wood, standard) | Catalog-driven |
| Striping, fencing, basic site work | Routine production work |

For these items, RS Means + CCI is usually within 5-10% of actual market.

---

## Using RS Means in Sub Negotiation

This is the highest-value use of RS Means data. When a sub comes in over budget:

1. Show them the RS Means line item with CCI applied
2. Show them the project-specific adjustments you've layered on
3. Ask: "What are we missing? Material, labor, schedule, scope?"

This converts the negotiation from "your number is too high" (which the sub will defend) to "let's find where we disagree" (which surfaces real cost drivers).

If the sub holds firm, you've at least documented the variance for the owner. The estimate becomes a defensible position, not a guess.

---

## Subscription and Access

RS Means is published by Gordian. Access options:

- **Online subscription** (Gordian Cloud Estimator / RSMeans Online) — typical $1,500-$3,500/year per seat
- **Printed annual books** — typical $300-$500 each for BCCD, Mechanical, Electrical
- **Academic / library access** — available at many university and public libraries
- **Free CCI access** — Gordian publishes CCI summary tables on their website (multipliers only, not full unit costs)

If you don't have a subscription, fall back to:

- Your historical project data (most accurate for your market)
- The unit cost ranges in `csi-divisions.md` (national-average templates)
- Current sub quotes (the ultimate reality check)

---

## What Goes in Your Estimate Documents

**Internal cost breakdown:** include the RS Means reference for major line items. This is your defensible reasoning.

**Client-facing proposal:** do NOT cite RS Means line by line. Cite it only at the division-summary level if relevant ("Division 09 finishes priced at $X/SF, within RS Means range of $Y-$Z for this finish level"). Clients don't want to read estimating manuals — they want to see a competent number with credible backing.

**Sub bid invitation:** do NOT include RS Means numbers. You're soliciting the sub's price, not telling them what you think it should be.

---

## Sources

- Gordian Group — RS Means Building Construction Cost Data, annual editions
- ENR Construction Cost Index — quarterly publication, real-time market index
- Construction Specifications Institute (CSI) MasterFormat — line item taxonomy
