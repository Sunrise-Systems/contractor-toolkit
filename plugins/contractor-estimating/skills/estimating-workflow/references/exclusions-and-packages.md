# Phase procedure

Load from the parent SKILL.md after its safety/state gate. Examples are illustrative, not verified project quantities/rates. Reference paths below are relative to the skill root. All outputs remain drafts until the shared gates pass.

## Phase 6: Exclusions & Inclusions

**Purpose:** Define what is in and what is out, using the master library.

### Process

**Auto-populate exclusions from:**

- `references/exclusions-master.md` — combined library categorized by A&E, GC, Electrical, Mechanical, Plumbing, Civil, and General
- Filter to only relevant items based on project type and applicable divisions from Phase 1

**Auto-populate inclusions/clarifications from:**

- `references/clarifications-master.md` — combined library by CSI division
- Filter to only applicable CSI divisions from Phase 1

### Presentation

Present the exclusions and inclusions organized by division/category:

```
Based on a [project type] project, here are the exclusions and
inclusions I've pulled from our standard library.

EXCLUSIONS (what is NOT included):
  General:
    1. [Exclusion item]
    2. [Exclusion item]
  Division 03 - Concrete:
    3. [Exclusion item]
  ...

INCLUSIONS & CLARIFICATIONS (what IS included):
  Division 09 - Finishes:
    1. [Clarification — assumption]
    2. [Clarification — standard of work]
  Division 23 - HVAC:
    3. [Clarification — coordination]
  ...

Review these and let me know what to add, remove, or modify.
```

### Standard Qualifications

Propose the following qualifications for estimator review; use only those supported by this project's evidence and approved terms:

1. Estimate valid for 30 days from date of issue
2. Based on [design phase] level documents; design changes may affect costs
3. Does not include costs for unforeseen conditions
4. Based on current building codes; future changes may affect costs
5. Pricing provenance/date/market and explicitly approved allowances are disclosed; do not claim current market accuracy without evidence
6. Permit timelines carry source/date or are labeled assumptions pending jurisdiction review
7. Hazmat abatement excluded unless specifically included
8. Based on standard working hours (Mon-Fri, 7am-3:30pm)
9. Assumes reasonable site access for construction activities
10. Assumes existing utilities are adequate; temporary services as noted

### Output

**Exclusions & Inclusions Schedule** — organized by division/category, with qualifications.

---

## Phase 7: Subcontractor Coordination Packages

**Purpose:** Generate bid packages for each sub trade identified in Phase 3.

### Process

For each subcontractor identified in Phase 3, assemble a self-contained bid package:

1. **Project Description** — Brief project overview, location, building type, SF
2. **Scope of Work** — Their specific scope from Phase 2, filtered to their divisions
3. **Quantities** — Their line items from Phase 4 with quantities and units
4. **Specifications and Standards** — Standards of work from `references/clarifications-master.md` for their divisions
5. **Schedule Requirements** — Project timeline, their work window, coordination milestones
6. **Coordination Items** — What other trades they need to coordinate with
7. **Exclusions** — What is excluded from their scope (so there are no gaps)
8. **Bid Requirements:**
   - Bid due date
   - Format requirements (lump sum, unit prices, or both)
   - Alternates to price (if any)
   - {{COMPANY_NAME}} contact information
   - Submission method

### Package Standard

Each sub package should be **self-contained** — a subcontractor should be able to price their work from the package alone without needing to see the full project estimate.

### Example Package Structure

```
{{COMPANY_NAME}} — SUBCONTRACTOR BID INVITATION

Project:     [Project Name]
Location:    [Address]
Building:    [Type], [SF]
Trade:       HVAC (Division 23)
License:     C-20 Required
Bid Due:     [Date]

SCOPE OF WORK:
  [Division 23 scope from Phase 2]

QUANTITIES:
  [Division 23 quantities from Phase 4]

SPECIFICATIONS:
  [Standards of work for Div 23]

SCHEDULE:
  [Work window, coordination milestones]

COORDINATION:
  [Other trades to coordinate with]

EXCLUSIONS FROM THIS TRADE:
  [Items explicitly not in HVAC scope]

BID FORM:
  Lump Sum: $_________
  Unit Price Alternates:
    Additional RTU (5-ton): $_____/EA
    ...

Submit to: [{{COMPANY_NAME}} contact]
Questions: [Contact info]
```

### Output

**Sub Bid Packages** — one per trade/sub, self-contained drafts pending review; not issued.

---
