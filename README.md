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

Then upload release zips from `dist/zips/` only after human review. Unconfigured templates now fail release validation; there is no token-ignore switch. Install validation dependencies first, as below. See `dist/README.md` for safe preview/build commands and companion requirements.

---

## Make it yours

Every skill is a Markdown file under `plugins/<plugin>/skills/<skill>/SKILL.md`. Common customizations:

- Swap the cost benchmarks in `contractor-estimating/skills/estimating-workflow/references/cost-reference.md` for your historical numbers
- Replace the California license classifications in `sub-trade-mapping.md` with your state's
- Add your standard exclusions and clarifications to the master libraries
- Drop your licensed AIA boilerplate into `contractor-brand/skills/brand/resources/` and `/contract` uses it automatically

Improvements that would help any contractor? PRs welcome.

## Validation and safety baseline

Use an isolated Python 3.13 environment (no system-package installation):

```sh
python3 -m venv /tmp/toolkit-venv
. /tmp/toolkit-venv/bin/activate
pip install -r scripts/requirements-validation.txt
python3 scripts/validate-toolkit.py --mode source
python3 -m unittest discover -s tests -v
bash -n scripts/build-dist.sh
bash -n plugins/contractor-docs/hooks/check-unresolved-tokens.sh
bash scripts/build-dist.sh --mode template-preview --output-dir /tmp/toolkit-preview
python3 scripts/validate-toolkit.py --mode template-preview --package-dir /tmp/toolkit-preview
```

Source checks cover **six plugins / 38 skills**: real duplicate-key-rejecting YAML/JSON,
exact inventory/manifests, safe resource paths, deterministic package identities, and
exact-context registered template tokens. Policy is `scripts/toolkit-policy.json`;
`template-tokens.json` records literal lines/counts and explanatory versus required use.
Review policy edits like code. It is not an authenticated whitelist.

Release is the default build mode and rejects required unresolved tokens, including logos.
A source checkout is intentionally not release-configured. Tests configure temporary
synthetic trees only and prove 38 archives plus normalized source/package parity.
Preview emits unpacked inspection files, never uploadable zips. Existing output must be
build-owned; staging failure preserves prior output. See the distribution recovery notes.

Read `references/toolkit-safety.md` and `references/guard-interface.md` before using
`python3 scripts/toolkit_guard.py --help`. The helper checks digest-bound change plans,
snapshots exact before-images, classifies readback, checks project-bound estimating
state/provenance with Decimal arithmetic, and emits HTML/DOCX/XLSX readback receipts.
It does not mutate planned files, authenticate consent, or persist workflow state for you.
Confidential plans/checkpoints stay local outside package inputs.

Only initialize, the three update skills, estimate, estimating-workflow, formal-bid,
contract, incident-report, sub-pay-app and document-generator have integration guidance
and static coverage. The shared policy is guidance for other skills, not equivalent
integration coverage or proof of agent obedience. Supervised/domain review is pending;
use `tests/manual-safety-evals.md` before pilot claims.

Draft, review, approval and final verification are distinct. External issuance stays
`not_issued`: no sending, signing, submission, payment approval or Matter mutation.
The bounded checker never grants `final_verified`; professional and visual review are
not automated. PDF verification is blocked until text/layout proof support exists;
all XLSX formulas block (use reviewed values with independent covered calculations).
The existing HTML Write hook is only defense in depth, not artifact verification.

## Credits & license

Built by [Formwork](https://github.com/Sunrise-Systems), derived from plugin suites built for real contractors. MIT licensed — see `LICENSE`.
