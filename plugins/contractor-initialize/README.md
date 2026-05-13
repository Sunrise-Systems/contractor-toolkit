# contractor-initialize

The setup wizard for the **contractor-toolkit** marketplace. Run this first.

## What it does

Walks you through a short, conversational interview (~9 sections) and then configures every other plugin in the toolkit — branding, voice, logos, contact info, ICP, and estimating defaults — so the rest of the skills (`/estimate`, `/proposal`, `/branded-doc`, etc.) feel like they were built for your company.

## Commands

| Command | Purpose |
|---|---|
| `/initialize` | First-time full setup. Walks all 9 sections, writes local config, substitutes placeholders across all toolkit plugins. |
| `/initialize [section]` | Re-run just one section: `brand`, `voice`, `logos`, `contact`, `icp`, `estimating`. |
| `/update-brand` | Re-run brand colors + typography. |
| `/update-estimating` | Re-run PM/estimating defaults. |
| `/update-company` | Update basic company info (name, address, contact). |
| `/show-config` | Print the current configuration. |

## Where settings live

Everything is written to `.claude/*.local.md` files, which are gitignored. The master file is `.claude/contractor.local.md`.

## After setup

You'll be ready to use any other plugin in the toolkit: `contractor-brand`, `contractor-docs`, `contractor-estimating`, and `contractor-extras`.
