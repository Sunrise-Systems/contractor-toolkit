# Subcontractor Trade Mapping

Maps CSI divisions to specialty contractor license classifications and self-perform vs. subcontract decisions. Used in Phase 3 (Sub Identification & Trade Mapping) of the estimating workflow.

**Licensing scheme:** Default is California's CSLB classifications (B = General Building, C-XX = specialty). If you operate in another state, replace the license column with your state's scheme. Common alternatives:

- **Texas:** No state GC license; trade-specific licenses (e.g., master electrician via TDLR)
- **Florida:** Construction Industry Licensing Board (CILB) — Certified or Registered classifications
- **New York City:** DOB licenses + trade-specific
- **Illinois:** Largely municipal; some state-level (electrical, plumbing)
- **Washington:** L&I specialty contractor registration

For projects in your home state, customize this file once and the rest of the workflow auto-references it.

---

## Self-Performed Scopes

Work GC crews typically handle in-house under a General Building license.

| Scope | CSI Division | License (CA Example) | Typical Crew |
|-------|-------------|----------------------|--------------|
| General conditions / supervision | DIV 01 | B (General) | 1 super + PM |
| Selective demolition | DIV 02 | B | 2-4 laborers |
| Rough carpentry / framing | DIV 06 | B | 2-4 framers |
| Blocking and backing | DIV 06 | B | Included with framing |
| Drywall (hang, tape, finish) | DIV 09 | C-9 or B | 2-4 drywall |
| Painting (interior) | DIV 09 | C-33 or B | 2-3 painters |
| General cleanup | DIV 01 | B | 1-2 laborers |
| Minor concrete (pour-backs, patching) | DIV 03 | B | 2-3 laborers |
| Temporary protection | DIV 01 | B | Included with general labor |

Your self-perform mix may differ — set it in `contractor-brand` or `.claude/contractor-estimating.local.md`. Some GCs self-perform more (carpentry, concrete forming, basic MEP). Some self-perform less (pure CM model — sub everything).

---

## Subcontracted Scopes

All specialty work requiring licensed contractors beyond typical self-perform capability.

### DIV 02 — Hazmat / Abatement

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Hazmat abatement | ASB + HAZ | Specialty abatement firm | Asbestos survey, abatement, air monitoring, disposal | Required for pre-1978 buildings |

### DIV 03 — Concrete (Structural)

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Concrete contractor | C-8 | Concrete subcontractor | Footings, slabs, grade beams, structural concrete, rebar, forming | Self-perform minor pour-backs; sub for structural |

### DIV 04 — Masonry

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Mason | C-29 | Masonry contractor | CMU walls, brick veneer, stone, mortar, control joints | Rare in TI; common in ground-up |

### DIV 05 — Structural Steel

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Steel fabricator/erector | C-51 | Structural steel contractor | Fabrication, delivery, erection, welding, connections | Includes misc metals |

### DIV 07 — Roofing

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Roofer | C-39 | Roofing contractor | Roofing system, flashing, penetration patching, warranty | GC patches own penetrations |

### DIV 07 — Insulation

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Insulation contractor | C-2 | Insulation specialty | Batt, spray foam, rigid, pipe insulation | Sometimes included with drywall sub |

### DIV 07 — Waterproofing

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Waterproofing contractor | C-61 (D-3) | Waterproofing specialty | Below-grade, foundation, deck, shower pan | Often combined with roofing sub |

### DIV 08 — Doors / Frames / Hardware

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Door supplier/installer | C-61 (D-28) | Door and hardware distributor | HM frames, wood doors, hardware sets, closers, keying | Supply and install; GC handles blocking |

### DIV 08 — Glazing / Storefront

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Glazier | C-17 | Glass and glazing contractor | Storefront systems, windows, interior glass, mirrors | Includes aluminum framing |

### DIV 09 — Flooring

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Flooring contractor | C-15 | Flooring installer | VCT, LVT, carpet tile, polished concrete, epoxy | Often 2 subs: hard tile + resilient |

### DIV 09 — Tile

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Tile setter | C-54 | Tile contractor | Ceramic, porcelain, natural stone, waterproofing, substrate prep | Floor and wall tile |

### DIV 09 — ACT Ceilings

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Ceiling contractor | C-61 (D-50) | Acoustical ceiling installer | Grid, tile, suspension, seismic bracing | Sometimes self-performed for small scopes |

### DIV 10 — Specialties

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Specialty supplier | Various | Toilet partition vendor, signage vendor | Toilet partitions, accessories, fire extinguishers, signage | Multiple suppliers; GC installs some |

### DIV 14 — Elevator

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Elevator contractor | Elevator contractor | Elevator company | Elevator installation, modernization, pit, shaft work | 3-6 month lead time |

### DIV 21 — Fire Sprinkler

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Fire sprinkler contractor | C-16 | Licensed FP contractor | System design (deferred submittal), pipe, heads, testing | Design-build; FP engineer included |

### DIV 22 — Plumbing

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Plumber | C-36 | Licensed plumbing contractor | Supply, DWV, gas piping, fixtures, water heater, testing | Code-required license |

### DIV 23 — HVAC

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| HVAC contractor | C-20 | Licensed HVAC contractor | Ductwork, equipment, controls, commissioning, energy code testing | Code-required license |

### DIV 26 — Electrical

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Electrician | C-10 | Licensed electrical contractor | Power distribution, circuits, lighting, panels, service | Code-required license |

### DIV 27 — Low Voltage / Data

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Low voltage contractor | C-7 | Low voltage/data cabling firm | Structured cabling, data drops, WiFi, AV rough-in | Separate from electrical |

### DIV 28 — Fire Alarm

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Fire alarm contractor | C-10 + NICET | Licensed fire alarm installer | Fire alarm panel, devices, programming, testing, monitoring | NICET certification required |

### DIV 28 — Security

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Security integrator | C-7 | Security/access control firm | Cameras, access control, burglar alarm, programming | Often combined with fire alarm sub |

### DIV 31 — Earthwork

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Grading/excavation contractor | A (General Engineering) or C-12 | Earthwork contractor | Grading, excavation, compaction, import/export | Ground-up and major site work |

### DIV 32 — Paving

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Paving contractor | C-12 or C-32 | Paving and striping firm | Asphalt, concrete paving, striping, ADA improvements | Parking lots, driveways |

### DIV 32 — Landscaping

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Landscape contractor | C-27 | Licensed landscape contractor | Planting, irrigation, hardscape, site furnishings | Often separate from paving |

### DIV 33 — Utilities

| Trade | License (CA) | Typical Sub Type | Bid Package Scope | Notes |
|-------|--------------|------------------|-------------------|-------|
| Underground utility contractor | C-34 or A | Pipeline/utility contractor | Water, sewer, storm drain, gas, dry utility trenching | Code-required license |

---

## Sub Selection Guidance

### TI Projects (Most Common GC Work)

**Typical sub count:** 6-10

| Category | Trades |
|----------|--------|
| Core subs (always needed) | Electrical, Plumbing, HVAC, Fire Sprinkler |
| Common additions | Flooring, Glazing, Fire Alarm, ACT Ceiling |
| Occasional | Concrete, Steel, Low Voltage, Security |

### Ground-Up Projects

**Typical sub count:** 12-20

All TI subs plus: Concrete, Steel, Masonry, Roofing, Earthwork, Paving, Landscaping, Elevator, Utilities, Waterproofing.

### Restaurant TI

Same as TI plus:

| Additional Trade | Notes |
|------------------|-------|
| Kitchen hood suppression | Fire protection sub or hood vendor |
| Grease interceptor | Included with plumber |
| Walk-in cooler | Specialty vendor |
| Exhaust hood | Sheet metal contractor |

### Healthcare TI

Same as TI plus:

| Additional Trade | Notes |
|------------------|-------|
| Medical gas | Specialty plumber or vendor |
| Backup power / generator | Electrical with NICET-certified switchgear |
| Lead-lined construction | Specialty contractor (imaging suites) |
| Infection control | Specialty contractor for negative pressure during work |

---

## Coordination Matrix

Sub-to-sub coordination requirements that affect scheduling and sequencing.

| Sub A | Sub B | Coordination Item |
|-------|-------|-------------------|
| Electrician | HVAC | Power connections to RTUs, disconnect switches |
| Electrician | Plumber | Water heater power, disposal circuits |
| Electrician | Fire Alarm | Power and circuit supervision |
| HVAC | Fire Sprinkler | Head placement below ductwork |
| HVAC | Ceiling | Diffuser placement, above-ceiling clearance |
| Plumber | Concrete | Underslab plumbing before pour |
| Framing | All MEP | Stud wall layout before rough-in |
| Drywall | All MEP | Close-in inspection before hanging board |
| Flooring | Painting | Sequence: paint first, then flooring |
| Glazier | Electrician | Power for automatic doors |

---

## Sources

- California Contractors State License Board (CSLB) classifications — primary reference
- National Association of State Contractors Licensing Agencies (NASCLA)
- Aggregated GC historical data on subcontractor roster composition
