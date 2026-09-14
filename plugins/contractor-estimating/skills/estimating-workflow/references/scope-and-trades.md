# Phase procedure

Load from the parent SKILL.md after its safety/state gate. Examples are illustrative, not verified project quantities/rates. Reference paths below are relative to the skill root. All outputs remain drafts until the shared gates pass.

## Phase 1: Plan Analysis & Division Scoping

**Purpose:** Review project plans/description and identify which CSI divisions are applicable.

### Process

Ask the user to describe the project. Collect these details conversationally:

- **Building type** — Commercial office, retail, restaurant, industrial, healthcare, education, hospitality, mixed-use, multi-family, religious/assembly
- **Square footage** — Gross SF, number of floors, lot size if relevant
- **Project type** — New construction, renovation, tenant improvement, addition, seismic retrofit, change of use, shell & core, ground-up
- **Scope of work description** — What is being built or renovated? What is the end use?
- **Drawings info** — Are there plans? What design phase? (Concept, SD, DD, CD) Or is this a napkin-sketch estimate?
- **Location** — City, neighborhood — affects labor rates, permitting, seismic/wind/flood zone
- **Service line** — A&E, GC, Electrical, Combined, Full End-to-End — depends on your company's offerings
- **Client name and project name**
- **Target timeline** — Desired start, desired completion, construction start date (for escalation)

### Division Applicability

Based on the project description, generate a **Division Applicability Matrix** using `references/csi-divisions.md`. For each of the CSI divisions, determine:

| Division | Applicable? | Primary / Ancillary | Complexity |
|----------|-------------|---------------------|------------|
| 01 - General Requirements | Yes | Primary | Standard |
| 02 - Existing Conditions | Yes | Primary | Complex (occupied demo) |
| 03 - Concrete | No | — | — |
| ... | ... | ... | ... |

- **Primary scope** = core to the project, significant cost driver
- **Ancillary** = required but minor, supporting role
- **Complexity levels:** Standard, Complex, Specialty

### Guidance

The following are illustrative assumptions for estimator review, not established project facts, current local costs or code determinations. Confirm jurisdiction, source and applicability before using any range.

- For **tenant improvements**, most structural divisions (03-05) are typically out unless there is structural modification
- For **restaurants**, flag Divisions 21-23 (fire suppression, plumbing, HVAC) as complex due to hood systems, grease traps, kitchen exhaust
- For **healthcare**, flag state hospital-authority compliance (e.g., HCAI in California) adds 20-40% and extends timelines
- For **renovations**, flag Division 02 (Existing Conditions) as complex — hazmat survey, selective demo, unforeseen conditions
- For **ground-up**, most divisions are in play — focus on identifying what is NOT needed

### Output

**Division Applicability Matrix** — table showing which divisions are in/out with rationale for each decision.

### Transition

```
Here are the divisions I've identified for this project. [X] divisions
are applicable — [Y] primary and [Z] ancillary.

Let me know if I should add or remove any before I write the scope.
```

---

## Phase 2: Written Scope by Division

**Purpose:** Produce an approvable written scope of work organized by CSI division.

### Process

For each applicable division from Phase 1, write a detailed scope description covering:

- **What work is included** — Specific, measurable scope statements. Reference `references/clarifications-master.md` for standards of work.
- **Key assumptions** — Reference clarifications typed as "Assumption"
- **Quality standards and code references** — Reference clarifications typed as "Standard of Work"
- **Coordination requirements** — Reference clarifications typed as "Coordination"

### Scope Standards

The written scope should be specific enough to:

1. **Get client approval** before proceeding to pricing
2. **Send to subcontractors** for bidding — a sub should understand exactly what they are pricing
3. **Serve as the basis for quantity takeoff** — every scope item becomes a measurable line item in Phase 4

Avoid generic boilerplate. Write scope that is specific to THIS project, THIS building type, THIS square footage. Instead of "Provide HVAC system," write "Provide (2) 5-ton RTU replacements on existing curbs, new ductwork distribution to serve approximately 4,500 SF of open office, and connection to existing BMS."

### For A&E Scope

When the project includes A&E services, organize scope by discipline rather than CSI division:

- Design phases included (SD, DD, CD, CA)
- Disciplines and deliverables per discipline
- Permitting scope and jurisdiction
- Special requirements (LEED, energy code, ADA, seismic)
- Reference `references/clarifications-master.md` (A&E section) for scope boundaries

### Output

**Written Scope Document** — division-by-division (or discipline-by-discipline for A&E) scope narrative with assumptions, standards, and coordination notes.

### Transition

```
Here's the written scope. Once you approve this, I'll identify the
subs we need and start the takeoff.
```

---

## Phase 3: Sub Identification & Trade Mapping

**Purpose:** Map each division to the subcontractors/trades needed.

### Process

For each applicable division, identify:

| Division | Trade | License | Self-Perform / Sub | Est. Sub Count |
|----------|-------|---------|---------------------|----------------|
| 09 - Finishes (Drywall) | Drywall/Plaster | C-35 (CA example) | Self-Perform | — |
| 21 - Fire Suppression | Fire Sprinkler | C-16 | Sub | 1 |
| 22 - Plumbing | Plumber | C-36 | Sub | 1 |
| 23 - HVAC | HVAC Contractor | C-20 | Sub | 1 |
| 26 - Electrical | Electrician | C-10 | Sub (in-house or external) | 1 |
| ... | ... | ... | ... | ... |

### Self-Perform vs. Sub

Most GCs self-perform a similar subset (your scope may differ — set it in `contractor-brand` or `.claude/contractor-estimating.local.md`):

**Typically self-performed:**
- General labor and supervision
- Coordination and project management
- Rough carpentry
- Drywall and painting
- Light demolition
- Cleanup and protection

**Typically subcontracted:**
- MEP (mechanical, electrical, plumbing)
- Roofing
- Fire protection / fire sprinkler
- Glazing and storefronts
- Flooring (specialty)
- Concrete (structural)
- Structural steel
- Elevators
- Low voltage (data, security, AV)
- Specialty trades (millwork, countertops, signage)

### Contractor License Classifications

Default reference is California's CSLB ({{LICENSE_SCHEME}}). If you operate in another state, replace `references/sub-trade-mapping.md` with your state's classification scheme. Common CSLB classifications:

- **C-10** Electrical
- **C-16** Fire Protection
- **C-20** HVAC
- **C-36** Plumbing
- **C-33** Painting and Decorating
- **C-35** Lathing and Plastering
- **C-43** Sheet Metal
- **C-46** Solar
- **C-54** Ceramic and Mosaic Tile
- **C-61/D-28** Doors and Gates
- **B** General Building Contractor

Reference `references/sub-trade-mapping.md` for the full mapping.

### Output

**Subcontractor Matrix** — table showing division, trade, license classification, self-perform/sub designation, and estimated sub count.

### Transition

```
We'll need [X] subcontractors across [Y] trades. Let me quantify
the work for each.
```

---
