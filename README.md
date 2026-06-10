# Contractor Toolkit

**An AI plugin marketplace for contractors.**

Tell Claude about your company once, and it writes your estimates, proposals, bid packages, contracts, RFIs, daily logs, and pay apps — in your brand, in your voice, the way a senior PM would.

Built for general contractors, design-builders, and specialty trades. Free, open source, yours to fork.

---

## What you get

| Plugin | What it does |
|--------|--------------|
| **contractor-initialize** | The setup wizard. Answer questions about your company once — name, colors, logo, voice, markets, defaults — and every skill below gets configured automatically. |
| **contractor-brand** | Keeps every document on-brand: your colors, fonts, logos, and how your company sounds. |
| **contractor-docs** | The document engine. Clean, premium HTML and DOCX output — the kind of paperwork that wins work. |
| **contractor-estimating** | The full preconstruction pipeline: ROM → Conceptual Budget → Formal Bid, plus plan takeoff, scope checks, sub bid packages, bid leveling, contracts, and subcontracts. |
| **contractor-extras** | The everyday paperwork: proposals, timelines, change orders, RFIs and RFI logs, submittals, daily logs, look-aheads, punch lists, incident reports, capabilities statements. |
| **contractor-subs** | For subcontractors: quote GC bid invitations, change order requests, T&M tickets, progress pay applications. |

Everything is plain Markdown — read it, edit it, make it yours.

---

## Get started in 3 steps

### 1. Get the code

```bash
gh repo fork Sunrise-Systems/contractor-toolkit --clone
cd contractor-toolkit
```

(Or just clone it. Forking lets you save your company's configured version.)

### 2. Install in Claude Code

```
/plugin marketplace add /absolute/path/to/contractor-toolkit
/plugin install contractor-initialize@contractor-toolkit
/plugin install contractor-brand@contractor-toolkit
/plugin install contractor-docs@contractor-toolkit
/plugin install contractor-estimating@contractor-toolkit
/plugin install contractor-extras@contractor-toolkit
```

Subcontractor? Add `/plugin install contractor-subs@contractor-toolkit`.

### 3. Run the wizard

```
/initialize
```

Claude interviews you — company name, brand colors, logo files, how you talk, who your clients are, your estimating defaults, what makes you win work. Takes about 10 minutes. Every answer flows into every document the toolkit ever produces.

That's it. Try:

```
/rom              → ballpark budget from a project description
/estimate         → full pipeline, idea to formal bid
/proposal         → branded client proposal
/daily-log        → site report from the super's notes
```

---

## A typical project, start to finish

```
/project-intake      Qualify the lead
/rom                 "You're looking at roughly $X–$Y" — before design starts
/plan-takeoff        Quantities from the drawings when plans arrive
/conceptual-budget   CSI-structured budget + scope gap check
/sub-bid-package     Send trades out to bid
/bid-leveling        Bids come back — compare apples to apples
/formal-bid          The proposal that wins the job
/contract            Signable contract from the accepted bid
/subcontract         Agreements for your awarded subs
/lookahead           Run the job week to week
/rfi-log /change-order /daily-log /submittal    The paperwork as it happens
/punch-list          Close it out
/capabilities-statement    Win the next one
```

---

## Share it with your team

After `/initialize`, push your configured fork to a private repo:

```bash
gh repo create my-company-skills --private --source=. --remote=origin --push
```

Teammates clone it, install the marketplace, and get your company's skills with zero setup.

## Use it on claude.ai too

Want these skills in the claude.ai web app or Cowork? **After running `/initialize`**, build standalone packages:

```bash
./scripts/build-dist.sh
```

Then upload zips from `dist/zips/` at **Settings → Skills → New skill**. Order matters: zips built before `/initialize` contain unconfigured templates (the build script warns you). See `dist/README.md` for details and which skills depend on each other.

---

## Make it yours

Every skill is a Markdown file under `plugins/<plugin>/skills/<skill>/SKILL.md`. Common customizations:

- Swap the cost benchmarks in `contractor-estimating/skills/estimating-workflow/references/cost-reference.md` for your historical numbers
- Replace the California license classifications in `sub-trade-mapping.md` with your state's
- Add your standard exclusions and clarifications to the master libraries
- Drop your licensed AIA boilerplate into `contractor-brand/skills/brand/resources/` and `/contract` uses it automatically

Improvements that would help any contractor? PRs welcome.

## Credits & license

Built by [Formwork](https://github.com/Sunrise-Systems), derived from plugin suites built for real contractors. MIT licensed — see `LICENSE`.
