---
name: formal-bid
description: Generate a Stage 3 Formal Bid — the construction proposal sent to the client after sub bids are collected. Outputs a text-dense DOCX matching your company's gold standard examples, plus sub bid packages per trade.
argument-hint: "[project description with sub bid data, or leave blank to start interactively]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Edit
---

# /formal-bid — Stage 3 Formal Construction Proposal

## Safety contract

Read `references/toolkit-safety.md` from the toolkit root (repository) or this skill root (standalone); resolve `GUARD` there as described in that guide. Missing helpers or companion resources block the gate.

- **Input:** Exact project/revision, indexed drawing/source hashes, scope, takeoff, quotes, and estimator-reviewed assumptions.
- **Output:** Stage-appropriate estimate drafts, evidence/state files, and artifact receipts; issuance remains `not_issued`.
- **AI role:** Extract, reconcile, recompute, draft, and checkpoint; never invent rates, source facts, or consent.
- **Human role:** Named estimator owns scope and pricing judgment; designated commercial reviewer approves final content/purpose.
- **Risk:** Consequential financial output, including draft estimates.
- **Checkpoint:** `workflow-state.json` and `pricing-evidence.json` beside project outputs; immutable prior revisions in local `checkpoints/`, outside package inputs.
- **Approval boundary:** Scope approval precedes takeoff/pricing; pricing review precedes final content-digest approval. Changed source/scope/amount invalidates affected approvals; do not infer approval from a prior conversation.
- **Verifier:** `python3 "$GUARD" check-workflow --state "$STATE" --evidence "$EVIDENCE"`, then independently reopen each saved artifact via `python3 "$GUARD" verify-artifact --artifact "$ARTIFACT" --expectations "$EXPECTATIONS" --receipt "$RECEIPT"`.
- **Failure:** Record `needs_human`, exception owner and next safe action; preserve drafts/checkpoints, stop finalization, and resume only after source/artifact hash checks.



Prepare a formal construction proposal draft for scoped human review; it is not signed or issued. This is after the conceptual budget is approved, after sub bids are collected, and before the contract is signed.

The canonical use case: *"Once the client agrees to the conceptual budget, go out to subs, collect pricing, and produce the actual bid/proposal. Pull structured data: scope per division, matched exclusions/inclusions per CSI code, clarifications, terms, and contract language."*

## When to Use This

- Conceptual budget approved
- Subcontractor pricing collected for major trades
- Plans are CD-level or GMP-ready
- Preparing a binding proposal for commercial review

## What This Produces

1. **Formal Bid Proposal DOCX (primary)** — Text-dense, editable, matches your company's gold standard example. Clients mark this up and return edits. Save as `{{COMPANY_NAME}}_Proposal_[ProjectName]_[YYYY-MM-DD].docx`.
2. **Formal Bid Proposal HTML (secondary, presentation)** — Same clean design language as ROM/Conceptual Budget. Save as `contractor_formal_bid_[project-slug]_[YYYY-MM].html`.
3. **Sub Bid Invitation Packages** — One set per trade. See `/sub-bid-package` skill.
4. **Internal Cost Breakdown** (optional) — DOCX for PM negotiation notes.

The formal bid is the one document type where DOCX is the primary output — clients must be able to mark it up.

## Document Style — Match Your Gold Standard

Reference your company's example proposals via `contractor-brand`. Typical visual rules:

- Pure black on white, Arial 10pt body, Arial 11pt bold for division headings
- No color, no accent, no decorative elements
- Hairline rules only between sections
- Text-dense — meant to be read and marked up by client and estimator, not presented as a visual artifact
- HTML version is the visual presentation; DOCX is Word-native and text-first

## Structure

Follow your gold-standard structure. A common pattern:

```
[Page 1 header]
COMPANY wordmark logo, top-left
Hairline rule

Project: [Project Name]
[Address]
Date: [Date]

Client:
[Client Name]
[Client Email]

Architect: [Architect Name]
[Architect Email]

{{COMPANY_NAME}} Contacts
{{PM_NAME}} ({{PM_TITLE}}): {{PM_EMAIL}} {{PM_PHONE}}
[Project Managers: ...]
[Accounts Receivable: ...]
[Senior Estimator: ...]

[1-2 sentence project summary]

[If multi-phase project, include a LEGEND block explaining any inline highlights:]
Legend
Blue: Items already included in previous Demo/Framing/Electrical Contract

Construction Investment
Schedule of Values
01    General Requirements              $XX,XXX
02    Existing Conditions               $XX,XXX
03    Concrete                          $XX,XXX
...

Division 01 - General Requirements: $XX,XXX
[Sub-item heading — bold]
[Scope narrative — "Provide and install..." — body]
[Budgetary Allowance $X,XXX] or [Estimated cost $X,XXX] or flat $X,XXX
[Inline exclusions — "Excludes ..."]
[Alternate Addition / Alternate Deduction lines]

Division 02 - Existing Conditions: $XX,XXX
[...]
```

## Inline Highlights Pattern

For multi-phase projects, use text highlighting (not font color) to flag items already covered under a prior contract:

- `WD_COLOR_INDEX.BLUE` — "already in prior contract"
- `WD_COLOR_INDEX.YELLOW` — owner-decision-pending items
- `WD_COLOR_INDEX.TURQUOISE` — owner-furnished items

Always include a Legend block at the top explaining each color used. Never use more than 2-3 highlight colors per document.

## Inline Inclusions & Exclusions Pattern

Every scope line follows this structure — prose-first, not table-driven:

**Inclusion:**
> Provide and install new storefront material consisting of 2" × 4½" frame, dark bronze anodized, center glaze with ½" safety tempered glass.
> $26,540

**Exclusion (immediately below the inclusion):**
> Excludes dumpsters and hauling
> Excludes hazardous waste removal

**Alternate:**
> Alternate Addition
> Provide and install gas line from fireplace (stub), pool and bbq.
> Budgetary Allowance $11,500
> Option for no fireplace -$2,500

## Inputs Needed

Collect conversationally. If a `/conceptual-budget` was already run for this project, pull from its output.

1. **Project info** — name, address, client, architect
2. **Sub bid data** — trade-by-trade pricing collected from subs
3. **Final scope decisions** — any scope changes from conceptual-budget
4. **Alternates to price** — what's in, what's optional
5. **{{COMPANY_NAME}} contact assignments** — PM, estimator, AR (pull from `.claude/contractor-estimating.local.md`)

## Pipeline

Invoke the `estimating-workflow` skill for **Phases 1-8** (full pipeline):

- Phases 1-2: Reuse scope only after exact project/revision/source-hash and approval checks; stale scope reopens review
- Phases 3-5: Sub roster, takeoff, pricing (update with actual sub bids)
- **Phase 6: Exclusions & Inclusions** — full library filtering
- **Phase 7: Sub Bid Coordination Packages** — one per trade
- **Phase 8: Document Generation** — formal bid DOCX + sub bid DOCX + optional internal breakdown

## Outputs

### 1. Formal Bid Proposal DOCX

`{{COMPANY_NAME}}_Proposal_[ProjectName]_[YYYY-MM-DD].docx`

- Matches your gold-standard structure
- No color, no visual design, text-dense
- Division-by-division scope with pricing
- Inline exclusions and alternates
- Standard contract language appendix (from your boilerplate)

### 2. Sub Bid Invitation Packages

One DOCX per trade: `{{COMPANY_NAME}}_BidInvite_[Trade]_[ProjectName]_[YYYY-MM-DD].docx`

Per Phase 7 of estimating-workflow:
- Project description
- Trade-specific scope of work
- Quantities and specifications
- Schedule & coordination requirements
- Bid form with lump-sum + unit-price alternates
- {{COMPANY_NAME}} contact + submission deadline

### 3. Internal Cost Breakdown (optional)

`{{COMPANY_NAME}}_CostBreakdown_[ProjectName]_[YYYY-MM-DD].docx`

Line-by-line with unit costs and pricing reasoning for internal PM use during sub negotiation. Never sent to client.

## Finalization and handoff

Require approved scope and approved pricing from the named estimator. Reopen DOCX and HTML and verify consistency of project, revision, scope, allowances, exclusions, currency and totals against the approved semantic fields. Changed amounts or regenerated content require new approval. Keep sub packages as drafts; direct `/sub-bid-package` execution is not covered by these gates.

Report exact paths, status, approval purpose/digest, readback receipts, and remaining review gaps. Final verification is not client acceptance or permission to send; issuance remains `not_issued`. `/contract` additionally requires evidence of the accepted bid and authorized legal review.
