---
name: incident-report
description: Generate a jobsite incident or near-miss report — facts, classification, witnesses, root cause, corrective actions, and an OSHA recordability checklist. Use when the user says "incident report", "near miss", "someone got hurt on site", "safety report", or "/incident-report".
argument-hint: [project or incident date]
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(python3 *toolkit_guard.py *)
---

# Incident Report

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** Attributed accounts, incident/project identity, date/time, witness statements and evidence; unknown facts remain unknown.
- **Output:** Factual incident DOCX draft, unresolved questions and review receipt.
- **AI role:** Extract, reconcile and draft; independently reopen exact saved paths, not merely trust a successful generator call.
- **Human role:** The responsible safety reviewer and counsel own report disposition, reporting duties and deadlines.
- **Risk:** Safety: consequential output; cannot certify safety or compliance.
- **Checkpoint:** Project-specific output directory with local `checkpoints/` for immutable prior revisions, source/artifact hashes, content expectations, approvals and receipts; outside package inputs.
- **Approval boundary:** Named human approval of exact project/entities/revision, dates, amount/currency where relevant, recipients/use, assumptions/exceptions and semantic-content digest. Material edits or regeneration invalidate approval. Final verified is not issued: issuance remains `not_issued`; no transmission, signature or external mutation.
- **Verifier:** `python3 "$GUARD" verify-artifact --artifact "$ARTIFACT" --expectations "$EXPECTATIONS" --receipt "$RECEIPT"`; check approved semantic fields separately from final-file digest. Required domain/visual checks must also pass.
- **Failure:** Missing evidence, stale approval/receipt or unavailable checks become `needs_human`; keep draft/checkpoint, identify owner and next safe action, withhold final status.



Generate a structured jobsite incident report from the super's account — injury, near-miss, property damage, or utility strike. Outputs DOCX through `contractor-docs`. Written same-day while memories are fresh; preserve the factual record without promising legal protection.

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
7. **Root cause review** — record only attributed findings established by the responsible investigator; otherwise mark undetermined and list evidence/questions. Never invent causation or fill a 5-why chain from speculation.
8. **Corrective actions** — each with an owner and a due date; these feed the next toolbox talk
9. **OSHA recordability checklist** (see below)
10. **Signatures** — preparer, superintendent, safety director

## OSHA Recordability Checklist

Use this as a federal OSHA screening aid, not a determination. Mark only evidence-supported candidates; unknowns stay unknown. The safety director/counsel must verify jurisdiction, state-plan rules, reporting triggers, timing and recording responsibility promptly:

- ☐ Death → **report to OSHA within 8 hours**
- ☐ Inpatient hospitalization, amputation, or eye loss → **report within 24 hours**
- ☐ Days away from work / restricted duty / job transfer → potential recordable candidate (OSHA 300 log)
- ☐ Medical treatment beyond first aid → potential recordable candidate
- ☐ Loss of consciousness → potential recordable candidate
- ☐ First aid only, no other criteria → potentially nonrecordable; reviewer must confirm criteria, document anyway
- Sub's employee → responsible reviewer determines recording employer from actual day-to-day supervision and applicable rules; do not assume payroll employer settles responsibility.

## Outputs

- `{company-slug}_incident_INC-{YYYY-NNN}_{project-slug}.docx`
- **Near-misses get the same report.** A near-miss is a free lesson; the report is how it gets banked. Offer a 5-minute toolbox-talk summary of the lesson as a follow-on output.

## Rules

1. **Same-day or note why not.** Late reports read as reconstructed.
2. **Facts, not fault.** No speculation, no blame language, no admissions — separate reported facts from unknowns and attributed investigator findings; preserve material facts, including unfavorable ones.
3. **Never minimize on paper.** "Minor cut" that needs stitches tomorrow makes the report look engineered.
4. **Photos referenced, not embedded judgments** — "Photo 3: edge condition at grid line F" with no commentary.
5. **Serious incident = stop and escalate.** Surface the 8/24-hour OSHA clock immediately, before finishing the report.
