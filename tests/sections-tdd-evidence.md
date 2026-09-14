# Finding 7: section labels — executed TDD evidence

Workdir: `/home/naram/projects/systems/contractor-toolkit`
Branch: `feat/youtube-informed-toolkit`; no commit/push.
Interpreter: `/tmp/contractor-toolkit-venv/bin/python`.

## Environment prerequisite (not RED)

Initial focused pytest invocation exited 1:
`/tmp/contractor-toolkit-venv/bin/python: No module named pytest`.
Installed pytest into the specified temporary venv with
`/tmp/contractor-toolkit-venv/bin/python -m pip install pytest`.
Resolved pytest 9.1.1 (pluggy 1.6.0, iniconfig 2.3.0,
packaging 26.3, pygments 2.21.0). No repository dependency files changed.
This setup failure is not counted as a behavioral RED.

## Vertical slice 1: explicit v2 label/field separation

Wrote only the fixture and `test_v2_human_label_differs_from_field_key`.
The approved plan binds `Company identity` via target `section` while selecting
actual field `company_name`; validation must succeed without changing the file.

RED command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_change_sections.py::test_v2_human_label_differs_from_field_key -q
```
Exit 1. Exact failure: `jsonschema.exceptions.ValidationError: 1 was expected`
on `schema_version: 2`; summary: `1 failed in 0.13s`.

Then added v2 change-plan/target schema definitions (mandatory target section),
change-plan-only runtime version support, exact target keys by version, and
retained the original field-key subset check specifically for v1.

GREEN: identical command, exit 0, `1 passed in 0.09s`.

## Vertical slice 2: bound label must actually be selected

Only after slice 1 GREEN, added `test_v2_unselected_section_rejected`, with
`Licensing`, ` Company identity`, and whitespace-only labels.
Fresh test approvals ensure stale digests cannot hide a missing membership check.

RED command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_change_sections.py::test_v2_unselected_section_rejected -q
```
Exit 1. Each case: `Failed: DID NOT RAISE ValueError`.
Exact summary: `3 failed in 0.16s`.

Then added nonempty target-section and exact selected-label membership checks
for v2, leaving v1 allowlist semantics and all IO/approval checks unchanged.

GREEN command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_change_sections.py -q
```
Exit 0, `4 passed in 0.10s`.

## Additional regression/contract coverage (not claimed as RED)

Added checks for missing section (schema constraint introduced in slice 1),
exact field selection, unselected edits, stale section/label/field/version
approvals, stale before-images, unchanged v1 behavior, forbidden v1 target
section, non-change kinds staying v1, invalid versions, and YAML/Markdown/text.
These exercised existing mechanisms or the already-green interface; no further
production code was needed and these are not represented as test-first REDs.

Focused command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/test_change_sections.py -q
```
Exit 0: `25 passed in 0.18s`.

Full regression command:
```sh
/tmp/contractor-toolkit-venv/bin/python -m pytest tests/ -q
```
Exit 0: `121 passed, 178 subtests passed in 32.58s`.

Documentation now distinguishes human labels from exact field keys and marks
v1 deprecated without reinterpreting approvals. The retained v1 schema ID is
unchanged; only change-plan definitions admit v2. No generic engine added.
