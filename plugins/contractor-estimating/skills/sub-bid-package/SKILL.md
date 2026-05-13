---
name: sub-bid-package
description: Generate a single subcontractor bid invitation package for a specific trade. Self-contained DOCX with scope, quantities, specs, schedule, and bid form. Useful when you need to send one trade out to bid without running the full formal-bid workflow.
argument-hint: "[trade name, or leave blank to select from project trade roster]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /sub-bid-package — Single Trade Bid Invitation

Generate a self-contained subcontractor bid invitation package for one trade. A sub should be able to price their work from this document alone, without seeing the full project estimate.

Useful when:
- You already have a formal-bid workflow in progress and need to re-issue one trade
- A specific trade dropped out and you're going back to market
- You want to pre-bid a long-lead trade (elevators, custom glazing, specialty equipment) before the rest of the project is ready

## Inputs Needed

- **Trade** — which subcontractor trade (HVAC, electrical, plumbing, fire sprinkler, drywall, etc.)
- **Project info** — name, address, building type, SF
- **Trade-specific scope** — what this trade is pricing
- **Quantities** — line items with quantities and units
- **Schedule** — project timeline and this trade's work window
- **Coordination** — other trades they need to coordinate with
- **Bid deadline** — due date and time

## Pipeline

Invoke only **Phase 7** of `estimating-workflow` scoped to the single specified trade.

## Output — HTML (Primary) + DOCX (Optional)

**HTML primary:** `contractor_sub_bid_[trade-slug]_[project-slug]_[YYYY-MM].html`

Clone the CSS from your company's example template. Cover block uses tag "Subcontractor Bid Invitation — [Trade Name]", project title/address, 3-col meta (Trade / CSI Division / Bid Due).

Include a high-contrast callout block for **"BID DUE: [date] at [time]"** — white text on company's primary block color (default: black).

**DOCX optional:** `{{COMPANY_NAME}}_BidInvite_[Trade]_[ProjectName]_[YYYY-MM-DD].docx` — generate only if the specific sub requests Word format.

Structure (from Phase 7 of estimating-workflow):

1. **Header** — Company wordmark, "Subcontractor Bid Invitation"
2. **Project description** — name, location, building type, SF
3. **Trade identification** — trade name, CSI division, license classification required
4. **Callout block** — "BID DUE: [date] at [time]"
5. **Scope of work** — trade-specific scope
6. **Quantities** — line items with quantities and units
7. **Specifications & standards** — pulled from `references/clarifications-master.md` for relevant divisions
8. **Schedule** — project timeline, trade work window, coordination milestones
9. **Coordination items** — other trades to coordinate with
10. **Exclusions from this trade** — so there are no scope gaps
11. **Bid form** — Lump Sum line + Unit Price Alternates section + {{COMPANY_NAME}} contact + submission method

## Visual Rules

- Pure black text on white (or your company palette per `contractor-brand`)
- Arial 10pt body, Arial 11pt bold for section headings
- Hairline rules only
- Callout box for BID DUE (white text on company primary block color)
- No accent color unless `contractor-brand` defines one

## Trade License Quick Reference (CA / CSLB Default)

| Trade | License | CSI |
|-------|---------|-----|
| Electrical | C-10 | 26 |
| Fire Protection | C-16 | 21 |
| HVAC | C-20 | 23 |
| Plumbing | C-36 | 22 |
| Painting | C-33 | 09 |
| Lathing & Plastering | C-35 | 09 |
| Sheet Metal | C-43 | 07 |
| Solar | C-46 | 26/33 |
| Ceramic Tile | C-54 | 09 |
| Doors & Gates | C-61/D-28 | 08 |

Replace with your state's license scheme if not operating in California. See `references/sub-trade-mapping.md` for full list.
