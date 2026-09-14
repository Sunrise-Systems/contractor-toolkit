---
name: update-estimating
description: Re-run just the estimating-defaults section of the contractor-toolkit setup — PM contact, default service line, default city, markups. Updates .claude/contractor-estimating.local.md.
argument-hint: ""
allowed-tools:
  - Bash(python3 *toolkit_guard.py *)
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# /update-estimating — Refresh Estimating Defaults

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** Selected-section answers, all four existing local configs, and exact template occurrence contexts.
- **Output:** Approved exact config/template edits, verified backups, and readback record.
- **AI role:** Stage answers and per-file/context patches; validate and apply only approved edits. Preserve unrequested fields and existing user edits.
- **Human role:** Company administrator reviews the diff, target root, and backup location.
- **Risk:** Reversible local update; no publishing or external writes.
- **Checkpoint:** User-approved local directory outside package inputs; change plan, before-images/absent records, after hashes, and receipt.
- **Approval boundary:** Explicit confirmation bound to the plan digest before any live write. Cancellation changes no targets. Ambiguous legacy replacements stop for per-file/context review.
- **Verifier:** Run `python3 "$GUARD" check-change --plan "$PLAN" --root "$ROOT"`, then `python3 "$GUARD" snapshot --plan "$PLAN" --checkpoint-dir "$CHECKPOINT"`; recheck before hashes immediately before edits. Reopen every changed file and run `python3 "$GUARD" verify-change --plan "$PLAN" --checkpoint-dir "$CHECKPOINT"`.
- **Failure:** Stop as `needs_human`; preserve backups and report conflicts. Resume classifies before/approved-after/conflict; recovery requires preview and approval, never overwrite concurrent edits.



Update the values that pre-fill `/estimate` without touching the rest of the config.

## Behavior

1. Read `.claude/contractor-estimating.local.md`. If missing, tell the user to run `/initialize` first.

2. Show current values:
   ```
   Current estimating defaults:
   • PM: Jordan Reyes — Senior Project Manager
   • Email: jordan@apexbuilds.com
   • Phone: (602) 555-0142
   • Default service line: General Contracting
   • Default city: Phoenix
   • OH&P: 15%
   • Contingency: 10%
   ```

3. Ask conversationally — group naturally:
   - **PM info** — name, title, email, phone (default: keep current)
   - **Default service line** — pick from the company's configured service lines
   - **Default city/market**
   - **Markups** — hourly markup, OH&P %, contingency %

4. Stage selected fields in the master config and affected per-plugin configs; leave all other fields unchanged. Include docs header/contact mirrors where relevant.

5. Inventory only these relevant token families and propose per-file/context patches (not broad old-value replacement):
   - `{{PM_NAME}}`, `{{PM_TITLE}}`, `{{PM_EMAIL}}`, `{{PM_PHONE}}`
   - `{{DEFAULT_DIVISION}}`, `{{DEFAULT_CITY}}`
   - `{{OHP_PERCENT}}`, `{{CONTINGENCY_PERCENT}}`
   For previously configured files, require trustworthy occurrence history or human-reviewed exact contexts. Complete the safety contract approval/snapshot/edit/readback sequence before success.

6. Report changed paths, selected fields, checkpoint and verified readback; unresolved conflicts remain `needs_human`.
