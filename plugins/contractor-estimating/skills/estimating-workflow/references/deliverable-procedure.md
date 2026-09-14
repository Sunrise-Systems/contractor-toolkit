# Phase procedure

Load from the parent SKILL.md after its safety/state gate. Examples are illustrative, not verified project quantities/rates. Reference paths below are relative to the skill root. All outputs remain drafts until the shared gates pass.

## Phase 8: Document Generation

**Purpose:** Generate all output documents using the `contractor-docs` plugin styling (or your own document generators).

### Documents to Generate

#### 1. Takeoff Proposal (Client-Facing)

The full estimate document that goes to the client:

- **Cover page** — Company branding, project name, prepared for/by, date, estimate number (EST-YYYY-NNN)
- **Executive summary** — Project description (2-3 sentences), total investment (prominent), key parameters table (SF, building type, location, design phase)
- **Written scope by division** — From Phase 2, clean narrative format
- **Priced estimate summary** — Division totals only (client does NOT see line-by-line unit costs)
- **Clarifications & assumptions** — Key assumptions that drive pricing
- **Exclusions** — Numbered, organized by category
- **Schedule/timeline** — Key milestones, construction duration
- **Terms and conditions** — Payment terms, change order process, validity period
- **Signature block** — Client and company signature lines, date fields, contact info

#### 2. Detailed Cost Breakdown (Internal / Negotiation)

The line-by-line estimate used for sub negotiation and internal review:

- **Full quantity takeoff** with unit costs from Phase 4 and Phase 5
- **Pricing reasoning** per line item and per division — the "why" behind each number
- **Division subtotals and project total**
- **Markup breakdown** — General conditions, overhead, profit, contingency, escalation, bond
- **Comparison notes** — RS Means range vs. applied rate, market conditions

This is the document the PM uses when a sub comes in high. "We estimated drywall at $3.25/SF because RS Means shows $2.80–$3.50 for Level 4 finish in our market. Your number is $4.50 — what are we missing?"

#### 3. Investment Deck (Presentation)

Executive summary format for presentations and PandaDoc-style delivery:

- **Project overview** (1 page) — What, where, why
- **Scope summary** with division breakdown (1-2 pages) — Visual, scannable
- **Investment summary** with visual cost breakdown (1 page) — Pie chart or bar, key numbers prominent
- **Timeline and milestones** (1 page) — Gantt-style or milestone list
- **Team and sub roster** (1 page) — Who is doing the work
- **Next steps and approvals needed** (1 page) — Clear call to action

Branded per `contractor-brand`, clean, presentation-quality.

#### 4. Sub Bid Invitation Packages

Per trade, from Phase 7:

- Project description
- Scope of work for their trade
- Quantities and specifications
- Schedule and coordination requirements
- Bid form / response format
- Company contact and submission deadline

### Brand Standards

Use the patterns from the `contractor-brand` plugin (if installed) or fall back to a clean monochrome default:

- **Typography:** Arial 10pt body, 11pt bold headings (DOCX); a clean sans-serif (HTML) — Helvetica Neue, Inter, system-ui
- **Palette:** Pure black, near-black body text, gray hairlines, white page; or whatever `contractor-brand` specifies
- **Hairline rules** between sections, no decorative borders
- **No accent color** unless `contractor-brand` defines one — restraint reads as premium

### Output Format — HTML First for Visual, DOCX for Editable

Match the design archetype to the deliverable:

| Deliverable | Format | Template |
|---|---|---|
| ROM Budget | **HTML** | Visual, print-to-PDF; clone from your example library |
| Conceptual Budget | **HTML** | Same as ROM, with expanded detail + scope-check findings |
| Investment Deck / Capabilities | **HTML** | Same HTML design language |
| Formal Bid / Proposal | **DOCX** | Text-dense, editable by client |
| Sub Bid Invitation | **DOCX** | Custom, matches formal-bid style |
| Internal Cost Breakdown | **DOCX** | Text-first, for PM use only |
| Letter / Change Order | **DOCX** | Letter archetype |
| Exclusions Workbook | **XLSX** | Generated via openpyxl |

**Do not render ROM, Conceptual Budget, or Investment Deck as DOCX by default.** HTML preserves the typography, hairline rules, and tonal Gantt bars that define a premium aesthetic. DOCX cannot reproduce them faithfully. Generate DOCX siblings only when the client specifically needs to edit the numbers.

### Output Filenames

```
contractor_rom_[project-slug]_[YYYY-MM].html                          — ROM Budget
contractor_conceptual_budget_[project-slug]_[YYYY-MM].html            — Conceptual Budget
contractor_scope_check_[project-slug]_[YYYY-MM].html                  — Scope Check Report
contractor_exclusions_[project-slug]_[YYYY-MM].xlsx                   — Exclusions Workbook
{{COMPANY_NAME}}_Proposal_[ProjectName]_[YYYY-MM-DD].docx              — Formal Bid Proposal
{{COMPANY_NAME}}_CostBreakdown_[ProjectName]_[YYYY-MM-DD].docx         — Internal Cost Breakdown
{{COMPANY_NAME}}_BidInvite_[Trade]_[ProjectName]_[YYYY-MM-DD].docx     — Sub Bid Package (per trade)
{{COMPANY_NAME}}_Contract_[ProjectName]_[YYYY-MM-DD].docx              — AIA A201 curated contract
```

All files save to the working directory unless the user specifies otherwise.

### Pre-delivery validation — mandatory

Run the safety contract's format-aware artifact verifier on the exact saved paths. A token scan of compressed DOCX/XLSX bytes is insufficient. Require parsed identity, required content, approved values, and receipts plus domain/visual review before final status. Missing parsers or unresolved tokens stop delivery as final.
