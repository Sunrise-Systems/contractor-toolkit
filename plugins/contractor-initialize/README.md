# contractor-initialize

The setup wizard for the **contractor-toolkit** marketplace. Run this first.

## What it does

Walks you through a short, conversational interview (10 sections) and then previews changes to the installed plugins in the toolkit — branding, voice, logos, contact info, ICP, and estimating defaults — so the rest of the skills (`/estimate`, `/proposal`, `/branded-doc`, etc.) feel like they were built for your company.

## Commands

| Command | Purpose |
|---|---|
| `/initialize` | First-time full setup. Walks all 10 sections, stages config and exact template patches, then applies approved changes. |
| `/initialize [section]` | Re-run just one section: `brand`, `voice`, `logos`, `contact`, `icp`, `estimating`. |
| `/update-brand` | Re-run brand colors + typography. |
| `/update-estimating` | Re-run PM/estimating defaults. |
| `/update-company` | Update basic company info (name, address, contact). |
| `/show-config` | Print the current configuration. |

## Where settings live

Everything is written to `.claude/*.local.md` files, which are gitignored. The master file is `.claude/contractor.local.md`.

## After setup

You'll be ready to use any other plugin in the toolkit: `contractor-brand`, `contractor-docs`, `contractor-estimating`, and `contractor-extras`.

## Safe updates

All four setup/update entry points stage answers before live writes. Review the exact diff, selected fields, target root, and checkpoint directory; approval binds the plan digest. Cancellation leaves targets unchanged. Verified before-image backups precede edits; exact after-image and parsed-field readback precedes success. Unrequested fields and user edits remain unchanged. No global old-value replacement is permitted: ambiguous previously configured templates need explicit per-file/context review. Stale hashes, interrupted runs, missing dependencies, or read-only targets stop as `needs_human`; recovery never silently overwrites concurrent edits.

Read the canonical `references/toolkit-safety.md` at toolkit root (or within a covered standalone skill) for commands. Backups stay local outside package inputs. Setup verification is not document approval, issuance, or permission to publish a configured repository.
