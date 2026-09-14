# HTML findings 3/4 follow-up evidence

Scope: `scripts/artifact_checks.py` HTML hidden-content and submission checks only, with related regression tests. Branch verified before and after: `feat/youtube-informed-toolkit`. Existing uncommitted fixes were preserved; no reset, checkout, commit, push, or PR. This follow-up changed one production condition and added one test; earlier HTML fixes/tests remain intact.

## Environment and baseline

Working directory for every command: `/home/naram/projects/systems/contractor-toolkit`.

Initial `python3 -m pytest tests/test_artifact_checks.py -q` exited 1: `/usr/bin/python3: No module named pytest`.

Existing temporary interpreter was discovered from repository evidence. Running `/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks -q` without PYTHONPATH exited 1 (`Ran 22 tests in 0.460s`, `FAILED (failures=94, errors=1)`), caused by `ModuleNotFoundError: No module named 'secure_io'` and the helper's resulting `AssertionError: artifact verification API is missing`. This was an invocation/import-path problem, not a valid behavior RED. No dependencies were installed and no unrelated imports were changed.

Corrected baseline command:

```sh
PYTHONPATH=scripts /tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks -q
```

Actual result: exit 0, `Ran 22 tests in 0.635s`, `OK`.

## Vertical slice: hidden popover revision

Inspection found the existing closed-dialog, template, closed-details, hidden/inert/aria-hidden and submission checks already implemented. Remaining gap: HTML `popover` content starts hidden, but the parser still extracted its approved revision and issued a receipt even when a visible paragraph said `revision: R2`.

Added `test_closed_popover_cannot_certify_a_visible_revision_mismatch` before editing production code. It replaces the approved revision paragraph with:

```html
<div popover><p data-field="revision">R1</p></div><p>revision: R2</p>
```

The same behavior is tested with `popover="auto"` and `popover="manual"`. All other required content and canonical print CSS remain valid.

### RED

```sh
PYTHONPATH=scripts /tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_closed_popover_cannot_certify_a_visible_revision_mismatch -v
```

Actual result: exit 1, `Ran 1 test in 0.091s`, `FAILED (failures=3)`. Each subtest (`popover`, `popover="auto"`, `popover="manual"`) failed at the expected rejection assertion with `AssertionError: ValueError not raised`. No working code was removed to produce RED.

### Minimal fix and GREEN

Added `or 'popover' in node.attrs` to the existing hidden/inert attribute rejection condition. This is deliberately conservative: popovers are rejected rather than treated as proof of visible text. No renderer or popover state evaluator was added.

Re-ran the exact RED command. Actual result: exit 0, `Ran 1 test in 0.078s`, `OK`.

## Exact requested existing regressions

```sh
PYTHONPATH=scripts /tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_closed_dialog_cannot_certify_a_visible_revision_mismatch tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes -v
```

Actual result: all three named tests `ok`; exit 0, `Ran 3 tests in 0.107s`, `OK`.

The exact closed-dialog fixture remains `<dialog><p data-field="revision">R1</p></dialog><p>revision: R2</p>` and must raise a hidden-content ValueError. Submission rejection covers `form`, `input`, `button`, `select`, `textarea`, plus `action` and `formaction` attributes with HTTPS, relative, empty, fragment and mailto values. Existing active-scheme tests are also retained.

## Broader verification

```sh
PYTHONPATH=scripts /tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_artifact_checks.py -q
```

Actual result: exit 0, `23 passed, 97 subtests passed in 0.72s`.

```sh
PYTHONPATH=scripts /tmp/contractor-toolkit-venv/bin/python -m pytest tests -q
```

Actual result: exit 0, `131 passed, 183 subtests passed in 37.04s`.

## Files and remaining limits

- Modified `scripts/artifact_checks.py`: one hidden-content condition.
- Modified `tests/test_artifact_checks.py`: one focused popover regression with three variants.
- Created `tests/html-followup-evidence.md`: this evidence.
- The first two files were already untracked on entry; ordinary `git diff --stat` does not show their changes. Existing unrelated working-tree changes were not edited.
- No new form-related production change was needed: baseline and explicit follow-up regressions pass.
- This is static readback validation, not browser rendering or exhaustive HTML/CSS sanitization. Existing `visual_layout_not_inspected` / `not_issued` receipt limits remain. No browser/PDF layout proof was performed.
- Standalone artifact unit-test invocation currently needs `PYTHONPATH=scripts`; this follow-up did not broaden scope to fix import packaging.
