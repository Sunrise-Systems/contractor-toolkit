---
name: update-company
description: Update basic company info in the contractor-toolkit setup — display name, legal name, tagline, founded year, addresses, phone, email, domain. Updates .claude/contractor.local.md.
argument-hint: ""
allowed-tools:
  - Bash(python3 *toolkit_guard.py *)
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# /update-company — Refresh Company Info

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



Use this when something basic changes — you renamed, moved, changed phone numbers, registered a new entity, picked up a new domain.

## Behavior

1. Read `.claude/contractor.local.md`. If missing, route the user to `/initialize`.

2. Show current values:
   ```
   Current company info:
   • Display name: Apex Construction
   • Legal name: Apex Construction Group, LLC
   • Tagline: Built right. On time.
   • Founded: 2014
   • Registered address: 123 Main St, Phoenix, AZ 85001
   • Operating address: same
   • Phone: (602) 555-0100
   • Email: hello@apexbuilds.com
   • Domain: apexbuilds.com
   ```

3. Ask conversationally which fields they want to change. For each, accept "skip" / "default" to keep current.

4. Stage selected fields in the master config and affected per-plugin configs; leave all other fields unchanged. Include docs header/contact mirrors where relevant.

5. Inventory only these relevant token families and propose per-file/context patches (not broad old-value replacement):
   - `{{COMPANY_NAME}}`, `{{COMPANY_LEGAL_NAME}}`, `{{TAGLINE}}`, `{{FOUNDED_YEAR}}`
   - `{{REGISTERED_ADDRESS}}`, `{{OPERATING_ADDRESS}}`
   - `{{PHONE}}`, `{{EMAIL}}`, `{{DOMAIN}}`
   For previously configured files, require trustworthy occurrence history or human-reviewed exact contexts. Complete the safety contract approval/snapshot/edit/readback sequence before success.

6. Report changed paths, selected fields, checkpoint and verified readback; unresolved conflicts remain `needs_human`.
