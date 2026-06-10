---
name: capabilities-statement
description: Generate a branded capabilities one-pager or project sheet — services, differentiators, notable projects, certifications, bonding, key contacts. Use when the user says "capabilities statement", "cap statement", "project sheet", "case study", or "/capabilities-statement".
argument-hint: [audience or pursuit, e.g. "school district RFQ"]
---

# Capabilities Statement

Generate the marketing document that goes out with prequalification packages, RFQ responses, and first-meeting follow-ups. Three formats, all branded through `contractor-docs`, all HTML-primary:

1. **Capabilities one-pager** — the standard cap statement: who we are, what we do, why us
2. **Project sheet** — one notable project, told properly: challenge, approach, outcome, numbers
3. **Case study** — a 2–3 page deep dive on one project for a specific pursuit

## Data Source

Pull from `.claude/contractor.local.md` — the `# Capabilities` section written by `/initialize` (differentiators, notable projects, certifications, bonding capacity, key personnel, safety record) plus company basics, ICP, and contact blocks.

If the Capabilities section is missing or thin, say so and offer to collect it now (`/initialize capabilities`) — don't pad with generic filler. A cap statement full of "committed to excellence" loses to one with real numbers.

## Capabilities One-Pager Structure

- **Header** — wordmark, tagline, the one-sentence company description
- **Core competencies** — service lines as short, concrete phrases
- **Differentiators** — 3–5, each one specific ("in-house A&E — permits in 6 weeks, not 16", not "quality-focused")
- **Notable projects** — 3–5 lines: name, type, SF/$, location
- **Company data block** — founded year, license number(s), bonding capacity, certifications (DBE/MBE/etc.), EMR if strong
- **Contact** — one person, direct line

Government/agency pursuits: include UEI/CAGE codes and NAICS codes if the user provides them — agencies filter on the data block first.

## Project Sheet Structure

One project per page: hero header (project name, type, size, location, delivery method), **Challenge / Approach / Outcome** in three tight paragraphs, a stats strip (contract value, duration, change-order rate if favorable, schedule performance), and the project team. Numbers beat adjectives — "delivered 11 days early with 1.8% change orders" is the whole pitch.

## Tailoring

Always ask (or infer from the argument) who this is for. Then:
- Lead with the differentiators that match the pursuit (healthcare pursuit → healthcare projects first)
- Match notable projects to the audience's project type
- Cut anything irrelevant — a tailored one-pager beats a complete two-pager

## Outputs

- `{company-slug}_capabilities_{audience-slug}_{YYYY-MM}.html` (+ PDF via the standard print path)
- `{company-slug}_project-sheet_{project-slug}_{YYYY-MM}.html`

## Rules

1. **Real numbers only.** Never invent project stats, EMR values, or bonding capacity — if it's not in the config or provided by the user, leave it out.
2. **The voice is the configured archetype** — a cap statement in the wrong voice reads like a template, which is the one thing it must never do.
3. **One page means one page** for the one-pager. Cutting is the skill.
