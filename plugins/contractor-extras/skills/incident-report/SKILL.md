---
name: incident-report
description: Generate a jobsite incident or near-miss report — facts, classification, witnesses, root cause, corrective actions, and an OSHA recordability checklist. Use when the user says "incident report", "near miss", "someone got hurt on site", "safety report", or "/incident-report".
argument-hint: [project or incident date]
---

# Incident Report

Generate a structured jobsite incident report from the super's account — injury, near-miss, property damage, or utility strike. Outputs DOCX through `contractor-docs`. Written same-day while memories are fresh; this document protects the company, the worker, and the record.

**Not legal or medical advice.** Serious incidents (hospitalization, amputation, fatality) have OSHA reporting deadlines measured in hours — the skill surfaces those timelines but the safety director and counsel own the calls.

## Inputs Needed

Collect conversationally — the super may be rattled; structure their account, don't interrogate:

1. **Project, date, time, exact location on site**
2. **Type** — injury / near-miss / property damage / utility strike / environmental
3. **People** — who was involved (name, employer — yours or a sub's, trade), who witnessed
4. **What happened** — factual sequence, in plain language
5. **Injury detail if any** — body part, apparent severity, treatment (first aid on site / clinic / ER), work status after
6. **Conditions** — weather, lighting, PPE in use, equipment involved
7. **Immediate actions taken** — medical response, area secured, equipment tagged out

## Report Structure

1. **Header block** — project, report number (INC-YYYY-NNN), date/time of incident, date of report, prepared by
2. **Classification** — type + severity (near-miss / first aid / recordable-candidate / serious)
3. **Factual narrative** — what happened, sequence only. **Facts, not fault** — "employee stepped backward off the unprotected edge" not "employee carelessly fell"
4. **People & witnesses** — table with names, employers, roles; witness statements attached or summarized
5. **Conditions & equipment**
6. **Immediate response** — what was done in the first hour
7. **Root cause analysis** — 5-why or contributing-factors format; "worker error" is never a root cause, it's where the analysis starts
8. **Corrective actions** — each with an owner and a due date; these feed the next toolbox talk
9. **OSHA recordability checklist** (see below)
10. **Signatures** — preparer, superintendent, safety director

## OSHA Recordability Checklist

Include this checklist with the relevant boxes marked from the facts gathered — as a flag for the safety director, not a determination:

- ☐ Death → **report to OSHA within 8 hours**
- ☐ Inpatient hospitalization, amputation, or eye loss → **report within 24 hours**
- ☐ Days away from work / restricted duty / job transfer → recordable (OSHA 300 log)
- ☐ Medical treatment beyond first aid → recordable
- ☐ Loss of consciousness → recordable
- ☐ First aid only, no other criteria → not recordable; document anyway
- Sub's employee → recordability lands on the sub's log; your incident report still gets written

## Outputs

- `{company-slug}_incident_INC-{YYYY-NNN}_{project-slug}.docx`
- **Near-misses get the same report.** A near-miss is a free lesson; the report is how it gets banked. Offer a 5-minute toolbox-talk summary of the lesson as a follow-on output.

## Rules

1. **Same-day or note why not.** Late reports read as reconstructed.
2. **Facts, not fault.** No speculation, no blame language, no admissions — the narrative states what happened, the root-cause section does the analysis.
3. **Never minimize on paper.** "Minor cut" that needs stitches tomorrow makes the report look engineered.
4. **Photos referenced, not embedded judgments** — "Photo 3: edge condition at grid line F" with no commentary.
5. **Serious incident = stop and escalate.** Surface the 8/24-hour OSHA clock immediately, before finishing the report.
