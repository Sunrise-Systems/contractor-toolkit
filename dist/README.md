# Standalone packages: validated, staged, not issued

Install `scripts/requirements-validation.txt` in an isolated Python 3.13 environment
as shown in the root README. Build commands run from the repository root:

```sh
python3 scripts/validate-toolkit.py --mode source
bash scripts/build-dist.sh --mode template-preview --output-dir /tmp/toolkit-preview
python3 scripts/validate-toolkit.py --mode template-preview --package-dir /tmp/toolkit-preview
# Only after configuring required tokens and reviewing the company design:
bash scripts/build-dist.sh --mode release --output-dir ./dist
python3 scripts/validate-toolkit.py --mode release --package-dir ./dist
```

`PYTHON=/absolute/path/to/venv/bin/python` selects the builder interpreter when the
virtual environment is not active. Default mode is release; default destination is dist.
Template-preview is inspection-only: unpacked folders and a non-release report, no zips.
An unconfigured checkout fails release on purpose. No token-ignore option exists.

## Contents and companions

Release produces `skills/<deterministic-name>/`, `zips/<name>.zip`, and
`build-report.json`. Each zip has one `SKILL.md` at its root, support resources and
`package-manifest.json`. The latter records source identity, content hashes, companions
and integration coverage. Name collisions namespace every member, not just the later one.
CRC, safe archive paths, exact contents and all shared-resource copies are checked.
Two builds are compared by normalized content hashes, **not timestamp-dependent zip bytes**.

All eleven covered standalone skills receive the canonical safety reference, interface,
schema, pinned dependency list and all guard/artifact modules. Additional required
resource copies are enumerated in policy. Edit canonical sources, never generated copies.

Estimating entry points need estimating-workflow, document-generator and brand installed
alongside them; extras/subcontractor document skills need document-generator and brand.
The branded-doc alias requires document-generator. Consult each package manifest.
Sibling plugin paths, agents, hooks and marketplace metadata are not magically present
in a standalone zip. Claude Code plugin installation remains the full host path;
missing companion skills/assets block the relevant workflow.

Licensed AIA boilerplate and company example libraries are optional user-provided inputs,
not shipped dependencies. Contract falls back to the neutral contract-skeleton draft
with explicit legal review; examples fall back to the canonical templates. Never bundle
client backups, prices or confidential files merely to satisfy a reference.

## Token and logo policy

`toolkit-policy.json` declares exact inventory, required resources, generated destinations,
companions and logo configuration. `template-tokens.json` registers exact path/line/count
occurrences. Only enumerated explanatory setup lines may retain tokens in releases.
A new token or changed unresolved context requires deliberate policy review, not a wildcard.

A configured logo design must use `logo.mode: assets` and enumerate real nonempty bundled
PNG/JPEG asset paths under `plugins/contractor-brand/skills/brand/assets/logos/`,
referenced in the configured brand skill and verified with Pillow. Other image formats
require a reviewed converter before this release gate. Alternatively an explicitly human-approved text-only design uses
`mode: no-logo`, empty files, and `approval: {reviewer, reason, digest}`. The digest is
SHA256 of compact sorted-key JSON mapping every brand-skill relative file path to its
SHA256. It binds the actual configured brand resources; changed design requires review.
This local approval is an audit aid, not authentication. Never invent reviewer consent.
Unresolved required logo tokens still fail even with a no-logo approval: remove or
configure those uses as part of the reviewed exact change plan.

## Promotion and recovery

Output must be a new/empty directory or a builder-owned destination. Existing dist may
contain only its tracked README before first use. Root/home/source directories, traversal,
symlink components and unknown output contents are rejected. There is no early deletion.

All output is generated and verified in a sibling staging directory. Only then is the
old directory renamed to `<output>.previous-<id>` and the complete stage promoted.
The tracked dist README is copied unchanged. Failed promotion restores the old directory
when possible; previous versions are retained for deliberate human cleanup/recovery.
SIGKILL/power loss between renames can leave the target absent, not partly complete:
inspect the sibling previous/staging directories and their reports before manually
restoring the previous directory. Do not blindly delete them. Hostile concurrent
filesystem mutation and crash-durable filesystem transactions are outside this baseline.

## Coverage and finalization limits

Source/package validation covers six plugins and 38 skills. Workflow guidance/static
integration covers only the eleven listed in the root README. It does not prove all
skills obey safety gates or establish professional correctness. Manual scenarios and
estimator/legal/safety/billing review remain pending release gates for pilot claims.

Artifact receipts verify exact saved paths/content; they never imply approval or issuance.
Status boundaries are draft / needs_review / approved_for_final / final_verified /
needs_human, with issuance separately `not_issued`. The helper withholds final_verified
because professional/visual review is not automated. PDF text/layout proof is unavailable;
formula workbooks are blocked. No external sending, signing, submission or Matter mutation.
