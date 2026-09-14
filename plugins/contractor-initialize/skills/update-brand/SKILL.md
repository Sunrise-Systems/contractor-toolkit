---
name: update-brand
description: Re-run just the brand section of the contractor-toolkit setup — primary color, accent, typography. Updates .claude/contractor-brand.local.md and re-substitutes brand placeholders across sibling plugins.
argument-hint: ""
allowed-tools:
  - Bash(python3 *toolkit_guard.py *)
  - Read
  - Write
  - Edit
  - AskUserQuestion
  - Glob
---

# /update-brand — Refresh Brand Settings

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



Quick way to change colors and typography without re-running the full `/initialize` wizard.

## Behavior

1. Read `.claude/contractor.local.md` and `.claude/contractor-brand.local.md`. If neither exists, tell the user to run `/initialize` first.

2. Show current brand:
   ```
   Current brand:
   • Primary: #0A0A0A
   • Accent: (none)
   • Typography: Helvetica Neue, Arial, sans-serif
   ```

3. Ask conversationally:
   - **Primary color** — hex code. Default: keep current.
   - **Accent color** — hex, or "none". Default: keep current.
   - **Typography** — Helvetica Neue / Inter / Monument Grotesk / custom. Default: keep current.

4. Stage selected fields in the master config and affected per-plugin configs; leave all other fields unchanged. Include docs header/contact mirrors where relevant.

5. Inventory only these relevant token families and propose per-file/context patches (not broad old-value replacement):
   - `{{PRIMARY_COLOR}}`
   - `{{ACCENT_COLOR}}`
   - `{{TYPOGRAPHY_PRIMARY}}`
   For previously configured files, require trustworthy occurrence history or human-reviewed exact contexts. Complete the safety contract approval/snapshot/edit/readback sequence before success.

6. Report changed paths, selected fields, checkpoint and verified readback; unresolved conflicts remain `needs_human`.
