# Findings 6/7 follow-up audit: executed evidence

Workdir: `/home/naram/projects/systems/contractor-toolkit`
Branch verified: `feat/youtube-informed-toolkit`. No commit, push, or PR.
Interpreter for every command below: `/tmp/contractor-toolkit-venv/bin/python`.

## Audit result and scope

Inspected `scripts/workflow_checks.py`, `scripts/change_checks.py`, the workflow
schema, `references/guard-interface.md`, workflow/section/guidance tests, and
prior TDD evidence. Existing runtime behavior already rejects pay-app finalization
with a named unavailable billing adapter and separates v2 human section labels
from exact field keys. No runtime or schema rewrite was needed or performed.
V1 field-key semantics remain deprecated, unchanged; workflow/pricing/receipt
versions remain v1. Existing section tests cover exact membership, selected-field
isolation, stale approvals/before-images, and JSON/YAML/Markdown/text behavior.

Baseline command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_workflow_checks.py tests/test_change_sections.py tests/test_skill_contracts.py -q
```
Exit 0: `48 passed, 57 subtests passed in 8.52s`.

## Existing-behavior regressions: explicitly not RED

Added four executable CLI regression cases to `tests/test_workflow_checks.py`:
- Domain switch from an accepted estimate to sub-pay-app invalidates the old
  estimate-final approval (`approval digest/purpose stale`).
- Wrong-project pricing evidence blocks even with a fresh digest and complete
  estimator approvals (`wrong project/revision evidence`).
- Internally reconciled changed quantities/amounts with a refreshed pricing digest
  invalidate the old pricing approval (`approval digest/purpose stale`), rather
  than relying on an arithmetic-error rejection.
- Removing approvals cannot promote a pay-app to either `approved_for_final` or
  `final_verified` (`completed scope needs scope approval`).

All four assert CLI failure and `issuance: not_issued`. Existing tests separately
exercise fresh estimator-approval bypass attempts for both final statuses, and
prior-period, retainage, SOV and totals mismatches plus a consistent control.
These are fail-closed adapter tests, NOT billing arithmetic certification or
semantic inspection of the synthetic pay-app payload. Editable records are not
authentication; they cannot prevent a caller from fabricating an entirely new
state and approval history.

```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_workflow_checks.py -q
```
Exit 0: `21 passed, 31 subtests passed in 10.90s`.
These passed on first run against existing code. No manufactured RED or production
change is claimed. The patch tool reported Pyright inferred-union warnings on the
new dictionary fixture mutation (the same dynamic fixture pattern already used
by this test module); Python syntax checking and real execution passed.

## One vertical RED → GREEN: pending human-review boundary

Added only `GuidanceContracts.test_human_reviews_are_pending_pre_pilot_not_pr_gate`
before changing the manual-evaluation document.

RED command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_skill_contracts.py::GuidanceContracts::test_human_reviews_are_pending_pre_pilot_not_pr_gate -q
```
Exit 1: `1 failed in 0.02s`.
Exact assertion prefix: `AssertionError: 'pre-pilot' not found`.
The document lacked the explicit pre-pilot versus PR merge boundary; this was a
real documentation-contract failure, not a runtime safety failure.

Minimal GREEN edit: rename the domain gate heading and add one paragraph in
`tests/manual-safety-evals.md`. Supervised/domain reviews remain **PENDING — not
executed**, are pre-pilot requirements, and are not a PR merge gate. CI/merge does
not authorize pilot/production use, billing approval, issuance, or reliability
claims. No pending case was marked passed.

Identical focused command, exit 0: `1 passed in 0.01s`.

## Full regression verification

```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/ -q
```
Exit 0: `131 passed, 183 subtests passed in 37.73s`.
This is the actual concurrent working-tree suite, including other agents' work;
its count is not represented as tests authored in this follow-up.

Files changed in this follow-up only:
- `tests/test_workflow_checks.py`
- `tests/test_skill_contracts.py`
- `tests/manual-safety-evals.md`
- `tests/workflow-followup-evidence.md` (new)

No secure IO, artifact, build, runtime, or schema implementation files edited.
Human supervised evaluations and professional sign-offs remain pending.
