# Phase procedure

Load from the parent SKILL.md after its safety/state gate. Examples are illustrative, not verified project quantities/rates. Reference paths below are relative to the skill root. All outputs remain drafts until the shared gates pass.

## Phase 4: Quantity Takeoff

**Purpose:** Quantify equipment, materials, and labor for each division's scope items.

### Process

For each division's scope items from Phase 2, break down into measurable quantities:

- **Materials:** Type, specification, quantity, unit of measure (SF, LF, CY, EA, TON, etc.)
- **Equipment:** Type, size/capacity, quantity or duration (days/weeks)
- **Labor:** Trade/crew type, estimated hours or crew-days

### Takeoff Format

Present quantities in a structured schedule per division:

```
DIVISION 09 — FINISHES
──────────────────────────────────────────────────────
Item                     Qty      Unit    Notes
──────────────────────────────────────────────────────
Metal stud framing       1,200    LF      3-5/8" 25ga @ 16" OC
5/8" Type X drywall      4,800    SF      Both sides, Level 4 finish
Acoustical ceiling tile  3,500    SF      2x4 tegular
Carpet tile (office)     2,800    SF      Commercial grade
LVP (corridors)          700      SF      Commercial grade, 20mil wear
Paint (walls)            4,800    SF      2 coats, eggshell finish
Paint (ceilings)         500      SF      Exposed areas only
Rubber base              650      LF      4" coved, adhesive
Door frames              12       EA      HM, 3-0 x 7-0, prepped
Doors                    12       EA      Solid core wood, pre-finished
──────────────────────────────────────────────────────
```

### Quantity Estimation Methods

- **From drawings:** When plans are available, quantities come from measurement
- **From ratios:** When estimating without complete plans, use building-type ratios:

**TI Projects — Typical Ratios:**
- ~1 LF of partition wall per 8-10 SF of TI area
- ~1 door per 100-150 SF of office space
- ~1 plumbing fixture per 1,000 SF of office
- ~1 fire sprinkler head per 130 SF (light hazard)
- ~1 electrical panel per 5,000-10,000 SF

**Ground-Up Projects:**
- Use building type benchmarks from `references/cost-reference.md`
- Structural quantities from building dimensions and engineering standards
- MEP quantities from fixture counts and system sizing

### Output

**Quantity Takeoff Schedule** — table per division with line items, quantities, units, and notes.

### Transition

```
Takeoff is checkpointed with evidence and unresolved quantities. Next, review sourced rates or explicit assumptions.
```

---

## Phase 5: Hard Cost Estimation

**Purpose:** Apply unit costs to quantities to build a priced estimate with reasoning for sub negotiation.

### Process

For each line item from the takeoff, apply unit costs and show the math:

```
DIVISION 09 — FINISHES — PRICED
─────────────────────────────────────────────────────────────────────────────
Item                     Qty    Unit   Mat $/Unit   Lab $/Unit   Total
─────────────────────────────────────────────────────────────────────────────
Metal stud framing       1,200  LF     $1.85        $2.40        $5,100
5/8" Type X drywall      4,800  SF     $0.95        $2.30        $15,600
Acoust. ceiling tile     3,500  SF     $2.50        $1.75        $14,875
Carpet tile              2,800  SF     $3.50        $0.85        $12,180
LVP (corridors)          700    SF     $4.25        $1.50        $4,025
Paint (walls)            4,800  SF     $0.35        $0.65        $4,800
Paint (ceilings)         500    SF     $0.35        $0.75        $550
Rubber base              650    LF     $1.25        $1.10        $1,528
Door frames (HM)         12     EA     $285         $125         $4,920
Doors (solid core)       12     EA     $425         $150         $6,900
─────────────────────────────────────────────────────────────────────────────
Division 09 Subtotal                                              $70,478
─────────────────────────────────────────────────────────────────────────────
```

### Unit Cost Sources

- Reference `references/rs-means-reference.md` for guidance on using RS Means data
- Reference `references/cost-reference.md` for SF benchmarks as a sanity check
- Reference `references/fee-reference.md` for A&E fee calculations
- Apply your local market multiplier (see cost-reference.md) — most national RS Means data needs adjustment by city

### Show the Reasoning

**This is what makes the estimate useful for sub negotiation.** For every priced line, include source-backed pricing rationale; the examples below are illustrative, not current market quotes:

```
Drywall priced at $3.25/SF (material + labor) — RS Means shows
$2.80–$3.50 for Level 4 finish in our market. If a sub quotes
$4.50/SF, the delta is $6,000 on this project and here's why we
think it should be lower.
```

The reasoning behind each price is what allows the PM to negotiate intelligently with subs. Without it, the estimate is just a number — with it, it is a negotiation tool.

### Investment vs. Cost — Premium Positioning

When presenting numbers to clients, prefer the word **Investment** over **Cost**. "Total Investment: $1.2M" reads as value delivered; "Total Cost: $1.2M" reads as money spent. This is a universal premium-positioning practice and should be used in client-facing documents. Internal documents (the cost breakdown) keep "Cost" — that's a working tool, not a sales document.

### Markups and Indirect Costs

After direct costs are totaled, add:

| Markup | Rate | Basis | Notes |
|--------|------|-------|-------|
| **General Conditions** | 8-15% of direct costs | Broken out: superintendent, insurance, cleanup, temp facilities, dumpsters, safety | Duration-dependent |
| **Overhead** | 8-15% | Per company standard | Home office allocation |
| **Profit** | 8-15% | Per company standard | Risk-adjusted return |
| **Contingency** | Varies by design phase | Applied to subtotal before O&P | See table below |
| **Escalation** | 3-6% annualized | From estimate date to construction midpoint | Only if start is future |
| **Bond Premium** | 1-3% of contract | If required by owner | Typically public work |

### Contingency by Design Phase

| Design Phase | Contingency Range | Rationale |
|-------------|-------------------|-----------|
| Concept/Programming | 25-35% | High uncertainty, minimal design definition |
| Schematic Design (SD) | 15-20% | General layout defined, systems conceptual |
| Design Development (DD) | 10-15% | Major systems defined, details emerging |
| Construction Documents (CD) | 5-10% | Most decisions made, details largely resolved |
| GMP / Bid | 2-5% | Based on actual subcontractor pricing |

### General Conditions Breakdown

| Item | Monthly Cost Range |
|------|-------------------|
| Project Superintendent | $12,000 - $22,000/mo |
| Project Manager (allocation) | $5,000 - $12,000/mo |
| Site Office/Trailer | $1,500 - $3,500/mo |
| Temporary Utilities | $1,000 - $3,500/mo |
| Temporary Protection | $2,000 - $5,000/mo |
| Dumpsters/Waste Removal | $2,000 - $5,000/mo |
| Equipment/Tools | $1,000 - $3,500/mo |
| Safety | $500 - $2,000/mo |
| Cleaning (progressive + final) | $1,000 - $3,500/mo |

General conditions total = monthly rate × project duration in months.

### Estimate Summary

```
DIRECT COSTS:
  Division 01 - General Requirements:    $[amount]
  Division 02 - Existing Conditions:     $[amount]
  Division 06 - Wood/Plastics:           $[amount]
  Division 07 - Thermal/Moisture:        $[amount]
  Division 08 - Openings:                $[amount]
  Division 09 - Finishes:                $[amount]
  Division 10 - Specialties:             $[amount]
  Division 21 - Fire Suppression:        $[amount]
  Division 22 - Plumbing:                $[amount]
  Division 23 - HVAC:                    $[amount]
  Division 26 - Electrical:              $[amount]
  Division 27 - Communications:          $[amount]
  Division 28 - Safety/Security:         $[amount]
  ─────────────────────────────────────────
  Direct Cost Subtotal:                  $[amount]

INDIRECT COSTS & MARKUPS:
  General Conditions ([X]%):             $[amount]
  Overhead ([X]%):                       $[amount]
  Profit ([X]%):                         $[amount]
  Contingency ([X]% at [phase]):         $[amount]
  Escalation ([X]% to [date]):           $[amount]
  Bond ([X]%):                           $[amount]
  ─────────────────────────────────────────

  TOTAL INVESTMENT:                      $[amount]
  Investment per SF:                     $[amount]/SF
```

### Output

**Priced Estimate** — line-by-line with unit costs, totals, markup breakdown, and pricing reasoning per division.

### Transition

```
Here's the hard cost breakdown with pricing reasoning. Let me add
the exclusions and inclusions.
```

---
