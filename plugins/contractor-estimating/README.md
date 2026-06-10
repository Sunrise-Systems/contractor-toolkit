# contractor-estimating

Preconstruction estimating pipeline for general contractors. Genericized from a real GC's eight-phase workflow — usable out of the box and easy to customize for your market, division mix, and brand voice.

## What it does

Three delivery stages, eight internal phases:

```
Stage 1 — ROM (Rough Order of Magnitude)        /rom
Stage 2 — Conceptual Budget                      /conceptual-budget
Stage 3 — Formal Bid                             /formal-bid
Post-contract                                    /contract
```

Plus standalone utilities:

| Command | Purpose |
|---|---|
| `/plan-takeoff` | Draft quantity takeoff from an uploaded plan set PDF |
| `/scope-check` | Gap analysis only — plans vs. master checklists |
| `/sub-bid-package` | Single-trade bid invitation |
| `/bid-leveling` | Compare returned sub bids — scope gaps, adjustments, award recommendation |
| `/subcontract` | Subcontract agreement for an awarded trade |
| `/exclusions-excel` | Project-filtered exclusions XLSX workbook |
| `/estimate` | Full end-to-end orchestrator |
| `/setup` | Save PM contact info and project defaults |

## What's inside

- `skills/estimating-workflow/` — the master 8-phase pipeline + universal references (CSI MasterFormat, sub-trade mapping, RS Means workflow, fee bands, exclusions, clarifications)
- `skills/rom/`, `skills/conceptual-budget/`, `skills/formal-bid/` — stage entry points
- `skills/scope-check/`, `skills/sub-bid-package/`, `skills/exclusions-excel/`, `skills/contract/` — standalone utilities
- `skills/estimate/` — orchestrator that runs all three stages
- `skills/setup/` — per-project config
- `agents/scope-writer.md`, `agents/estimate-reviewer.md`, `agents/sub-packager.md` — specialist subagents

## Customize for your shop

1. Run `/setup` once per project to save PM name, default division, market city, and issuing company. Output lands at `.claude/contractor-estimating.local.md`.
2. Edit `skills/estimating-workflow/references/cost-reference.md` — the $/SF benchmarks are templated; replace with your historical data and local market rates.
3. Edit `skills/estimating-workflow/references/sub-trade-mapping.md` — the license classifications default to California (CSLB). If you operate elsewhere, swap in your state's licensing scheme.
4. Edit `skills/estimating-workflow/references/exclusions-master.md` and `clarifications-master.md` — add your standard scope boundary language. Harvest from past proposals.
5. Optional: install the companion `contractor-brand` plugin to inject your company name, divisions, color palette, and voice archetype across all generated documents.

## Companion plugins

- **contractor-brand** — Company identity (name, divisions, palette, voice). Variables defined there are consumed by this plugin's `{{COMPANY_NAME}}`, `{{DEFAULT_DIVISION}}`, `{{VOICE_ARCHETYPE}}` etc.
- **contractor-docs** — DOCX/HTML/XLSX document generators. This plugin produces estimate content; contractor-docs renders the deliverables.

## License

MIT
