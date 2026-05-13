---
name: daily-log
description: Generate a daily construction site report — weather, crews on-site, work performed, deliveries, visitors, safety, and look-ahead. Use when the user says "daily log", "site report", "daily report", or "/daily-log".
argument-hint: [date or project]
---

# Daily Log

Generate a daily construction site report from a superintendent's field notes. Outputs DOCX or PDF through `contractor-docs`. Daily logs are the contractor's primary contemporaneous record — they protect against delay claims, RFI disputes, and liability issues.

Use this every day work happens on site. If the super dictates rough notes, the skill structures them into the standard daily log format.

---

## Inputs Needed

Gather in three quick chunks. Skip empty sections rather than padding.

### 1. Header & Conditions
- Project name and number
- Date (and day of week)
- Superintendent on duty (default `{{PM_NAME}}` if not given)
- Weather: temperature high/low, conditions (sunny / overcast / rain), wind, any work stoppages caused by weather
- Site conditions (dry, muddy, etc.)

### 2. People & Work
- Crews on-site — by trade with headcount (e.g., "Framers: 6, Electricians: 3, Plumbers: 2")
- Work performed today — by area or zone, bullet points
- Equipment on-site (cranes, lifts, generators)
- Visitors (owner, architect, inspector, vendor) — names and reason
- Inspections performed and outcomes

### 3. Issues & Look-Ahead
- Deliveries received (material, supplier, quantity)
- Safety incidents or near-misses (or "none")
- Delays or disruptions (and cause)
- Photos referenced (file names or sequence)
- Tomorrow's planned work and crew count

---

## Workflow

```
1. INTAKE     → Three chunks above
2. STRUCTURE  → Organize into standard sections; preserve user wording
3. SAFETY     → Always include the safety section, even if "none"
4. DRAFT      → Single document, dated and signed
5. EXPORT     → contractor-docs renders DOCX/PDF, archived by date
```

Daily logs are a legal record. Do not fabricate or "fill in" missing detail. If the user did not provide info for a section, mark it "None reported" or "N/A".

---

## Output

A one- to two-page report with:

1. Header — project, date, day of week, superintendent
2. Weather and site conditions
3. Crews on-site (table by trade)
4. Work performed (by area)
5. Equipment on-site
6. Deliveries received
7. Visitors and inspections
8. Safety
9. Delays / disruptions
10. Photos referenced
11. Look-ahead (next day)
12. Signature line

---

## Template

```markdown
# DAILY LOG

**Project:** {PROJECT_NAME}  ·  **Project No.:** {PROJECT_NUMBER}
**Date:** {DATE} ({DAY_OF_WEEK})
**Superintendent:** {{PM_NAME}}

---

## Weather & Conditions

| Field | Value |
|-------|-------|
| Temperature | {LOW}°F – {HIGH}°F |
| Conditions | {SUNNY/OVERCAST/RAIN/SNOW} |
| Wind | {WIND} |
| Site Conditions | {DRY/MUDDY/ICY/NORMAL} |
| Weather Stoppages | {NONE | DURATION + DETAIL} |

---

## Crews On-Site

| Trade | Company | Headcount | Area |
|-------|---------|-----------|------|
| {TRADE} | {SUB} | {N} | {AREA} |

**Total workers on-site:** {TOTAL}

---

## Work Performed

### {AREA_1}
- {ITEM}

### {AREA_2}
- {ITEM}

---

## Equipment On-Site

- {EQUIPMENT}

---

## Deliveries Received

| Time | Material | Supplier | Quantity | Received By |
|------|----------|----------|----------|-------------|
| {TIME} | {MATERIAL} | {SUPPLIER} | {QTY} | {NAME} |

---

## Visitors & Inspections

| Time | Name | Company | Purpose / Outcome |
|------|------|---------|-------------------|
| {TIME} | {NAME} | {COMPANY} | {PURPOSE} |

---

## Safety

**Incidents:** {NONE | DETAIL}
**Near-Misses:** {NONE | DETAIL}
**Toolbox Talk:** {TOPIC_OR_NONE}
**PPE Compliance:** {OBSERVATIONS}

---

## Delays / Disruptions

{NONE_OR_NARRATIVE_WITH_CAUSE_AND_DURATION}

---

## Photos Referenced

- {FILE_NAME_OR_DESCRIPTION}

---

## Look-Ahead — {NEXT_DATE}

- Planned work: {SUMMARY}
- Expected crew count: {N}
- Expected deliveries: {LIST}
- Inspections scheduled: {LIST}

---

**Logged by:** {{PM_NAME}}, {{PM_TITLE}}
**Signature:** ___________________________

*{{COMPANY_LEGAL_NAME}} · {{OPERATING_ADDRESS}} · {{DOMAIN}}*
```
