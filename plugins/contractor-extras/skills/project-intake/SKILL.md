---
name: project-intake
description: Interview a prospective client to qualify a new project — type, scope, budget, timeline, location, decision-maker, and current design stage. Outputs a project brief for CRM and estimating. Use when the user says "new project intake", "qualify a lead", "project brief", or "/project-intake".
argument-hint: [client or project name]
---

# Project Intake

Walk through a structured interview about a new prospective project. Qualify the lead, classify the project, and produce a structured brief the user can paste into their CRM or hand to the estimating team.

Use this when a new inquiry comes in by phone, email, or referral and you need to capture everything before it goes cold.

---

## Inputs Needed

Conversational, not a form. Group into four chunks.

### 1. Who
- Contact name and title
- Company / entity (LLC, Corp, individual owner)
- Phone and email
- How they found `{{COMPANY_NAME}}` (referral source if any)
- Decision-maker: are they it, or is there someone above them?

### 2. What
- Project type — new build / TI / renovation / addition / electrical
- Project use — office / retail / restaurant / industrial / residential / mixed-use
- Approximate square footage
- Brief description in their own words
- Special requirements (ADA, commercial kitchen, fire suppression, data, seismic, historic, LEED)

### 3. Where & When
- Project address (or cross streets)
- City, neighborhood
- Target start date
- Target completion / open date
- Hard deadlines (lease commencement, grand opening, investor milestone)
- Lease signed? (if applicable)

### 4. Stage & Budget
- Current design stage:
  - **Pre-design** — concept only, no drawings
  - **SD (Schematic Design)** — early massing and layout
  - **DD (Design Development)** — detailed drawings, material selections in progress
  - **CD (Construction Documents)** — full permit set, ready for pricing
  - **Permitted** — approved, ready to build
- Architect / engineer on board? Who?
- Budget — stated number, range, or "TBD"
- Funding source (cash, loan, investor, SBA, owner financing)

---

## Workflow

```
1. WHO        → Capture contact and decision-maker
2. WHAT       → Scope, type, size, special requirements
3. WHERE/WHEN → Location and schedule
4. STAGE      → Design stage and team
5. BUDGET     → Number and funding source
6. ASSESS     → Fit notes — strengths, concerns, next step
7. OUTPUT     → Generate project brief
```

Ask one question at a time. Listen. Let the client talk in chunk 2 — capture everything, classify later.

If the prospect is clearly out of scope (residential-only, out of region, sub-$25K budget on a $200K scope), note it and propose declining gracefully.

---

## Output

A structured markdown summary the user can paste directly into CRM (`component-zero-c0`, HubSpot, etc.) or hand to estimating. Not styled — plain markdown so it's portable.

---

## Template

```markdown
# Project Brief — {PROJECT_NAME}

**Intake Date:** {DATE}
**Intake By:** {{PM_NAME}}, {{PM_TITLE}}
**Source:** {REFERRAL_SOURCE_OR_INBOUND}

---

## Contact

| Field | Value |
|-------|-------|
| Name | {CONTACT_NAME} |
| Title | {TITLE} |
| Company | {COMPANY} |
| Phone | {PHONE} |
| Email | {EMAIL} |
| Decision Maker? | {YES_OR_REPORTS_TO_NAME} |

---

## Project

| Field | Value |
|-------|-------|
| Type | {NEW_BUILD / TI / RENOVATION / ADDITION / ELECTRICAL} |
| Use | {OFFICE / RETAIL / RESTAURANT / INDUSTRIAL / MIXED} |
| Square Footage | {SF} |
| Address | {ADDRESS}, {CITY} |
| Description | {CLIENT_NARRATIVE} |

**Special Requirements:**
- {REQUIREMENT}

---

## Schedule

| Field | Value |
|-------|-------|
| Target Start | {START_DATE} |
| Target Completion | {END_DATE} |
| Hard Deadlines | {DEADLINES_OR_NONE} |
| Lease Signed | {YES_OR_NO_OR_NA} |

---

## Design Stage

| Field | Value |
|-------|-------|
| Current Stage | {PRE_DESIGN / SD / DD / CD / PERMITTED} |
| Architect | {AE_NAME_OR_NONE} |
| Engineer | {ENGINEER_OR_NONE} |
| Plans Available | {NONE / CONCEPTUAL / IN_PROGRESS / READY} |

---

## Budget

| Field | Value |
|-------|-------|
| Stated Budget | {AMOUNT_OR_RANGE_OR_TBD} |
| Funding Source | {CASH / LOAN / INVESTOR / SBA / OWNER_FINANCE} |
| Budget Realistic? | {YES / NEEDS_DISCUSSION / NO} |

---

## Qualification Notes

**Strengths:**
- {WHY_THIS_IS_A_FIT}

**Concerns:**
- {RED_FLAGS_OR_OPEN_QUESTIONS}

**Recommended Next Step:**
{SITE_WALK / PRELIM_ESTIMATE / FULL_PROPOSAL / DECLINE / NURTURE}

**Owner / Assignee:** {{PM_NAME}}

---

*Generated via {{COMPANY_NAME}} project-intake · {DATE}*
```

After the brief is generated, offer to:
1. Save to CRM
2. Hand off to `/proposal` if the lead is hot
3. Schedule a site walk via calendar
4. Add to nurture pipeline if not yet ready
