# HTML findings 3/4 — executed vertical TDD

Working directory: `/home/naram/projects/systems/contractor-toolkit`. Output strings are JSON-escaped losslessly to keep this evidence under 300 lines.

## Submission elements RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements
```
```json
{"output": "FFFFF\n======================================================================\nFAIL: test_html_rejects_submission_elements (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements) (tag='form')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 37, in test_html_rejects_submission_elements\n    with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, 'submission'):\n                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_elements (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements) (tag='input')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 37, in test_html_rejects_submission_elements\n    with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, 'submission'):\n                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_elements (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements) (tag='button')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 37, in test_html_rejects_submission_elements\n    with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, 'submission'):\n                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_elements (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements) (tag='select')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 37, in test_html_rejects_submission_elements\n    with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, 'submission'):\n                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_elements (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements) (tag='textarea')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 37, in test_html_rejects_submission_elements\n    with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, 'submission'):\n                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n----------------------------------------------------------------------\nRan 1 test in 0.091s\n\nFAILED (failures=5)", "exit_code": 1}
```

## Submission elements GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements
```
```json
{"output": ".\n----------------------------------------------------------------------\nRan 1 test in 0.078s\n\nOK", "exit_code": 0}
```

## Submission elements regression GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks
```
```json
{"output": ".................\n----------------------------------------------------------------------\nRan 17 tests in 0.587s\n\nOK", "exit_code": 0}
```

## Submission attributes RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes
```
```json
{"output": "FFFFFFFFFF\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='action', value='https://invalid.test/submit')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='action', value='/submit')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='action', value='')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='action', value='#scope')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='action', value='mailto:a@invalid.test')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='formaction', value='https://invalid.test/submit')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='formaction', value='/submit')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='formaction', value='')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='formaction', value='#scope')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_rejects_submission_attributes (tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) (attr='formaction', value='mailto:a@invalid.test')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 43, in test_html_rejects_submission_attributes\n    with self.subTest(attr=attr, value=value), self.assertRaisesRegex(ValueError, 'submission'):\n                                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n----------------------------------------------------------------------\nRan 1 test in 0.117s\n\nFAILED (failures=10)", "exit_code": 1}
```

## Submission attributes GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes
```
```json
{"output": ".\n----------------------------------------------------------------------\nRan 1 test in 0.105s\n\nOK", "exit_code": 0}
```

## Submission attributes regression GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks
```
```json
{"output": "..................\n----------------------------------------------------------------------\nRan 18 tests in 0.571s\n\nOK", "exit_code": 0}
```

## Closed dialog semantic mismatch RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_closed_dialog_cannot_certify_a_visible_revision_mismatch
```
```json
{"output": "F\n======================================================================\nFAIL: test_closed_dialog_cannot_certify_a_visible_revision_mismatch (tests.test_artifact_checks.ArtifactTests.test_closed_dialog_cannot_certify_a_visible_revision_mismatch)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 50, in test_closed_dialog_cannot_certify_a_visible_revision_mismatch\n    with self.assertRaisesRegex(ValueError, 'hidden'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n----------------------------------------------------------------------\nRan 1 test in 0.092s\n\nFAILED (failures=1)", "exit_code": 1}
```

## Closed dialog semantic mismatch GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_closed_dialog_cannot_certify_a_visible_revision_mismatch
```
```json
{"output": ".\n----------------------------------------------------------------------\nRan 1 test in 0.078s\n\nOK", "exit_code": 0}
```

## Closed dialog regression GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks
```
```json
{"output": "...................\n----------------------------------------------------------------------\nRan 19 tests in 0.601s\n\nOK", "exit_code": 0}
```

## Invisible subtrees RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text
```
```json
{"output": "FFFF\n======================================================================\nFAIL: test_html_invisible_subtrees_cannot_supply_required_text (tests.test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text) (wrapper='<div inert>{}</div>')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 60, in test_html_invisible_subtrees_cannot_supply_required_text\n    with self.subTest(wrapper=wrapper), self.assertRaises(ValueError):\n                                        ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_invisible_subtrees_cannot_supply_required_text (tests.test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text) (wrapper='<div aria-hidden=\"TRUE\">{}</div>')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 60, in test_html_invisible_subtrees_cannot_supply_required_text\n    with self.subTest(wrapper=wrapper), self.assertRaises(ValueError):\n                                        ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_invisible_subtrees_cannot_supply_required_text (tests.test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text) (wrapper='<details><summary>Heading</summary>{}</details>')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 60, in test_html_invisible_subtrees_cannot_supply_required_text\n    with self.subTest(wrapper=wrapper), self.assertRaises(ValueError):\n                                        ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_html_invisible_subtrees_cannot_supply_required_text (tests.test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text) (wrapper='<details><summary>Heading</summary><summary>{}</summary></details>')\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 60, in test_html_invisible_subtrees_cannot_supply_required_text\n    with self.subTest(wrapper=wrapper), self.assertRaises(ValueError):\n                                        ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n----------------------------------------------------------------------\nRan 1 test in 0.114s\n\nFAILED (failures=4)", "exit_code": 1}
```

## Invisible subtrees GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text
```
```json
{"output": ".\n----------------------------------------------------------------------\nRan 1 test in 0.139s\n\nOK", "exit_code": 0}
```

## Invisible subtrees regression GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks
```
```json
{"output": "....................\n----------------------------------------------------------------------\nRan 20 tests in 0.600s\n\nOK", "exit_code": 0}
```

## Template semantic mismatch RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_template_cannot_supply_approved_revision
```
```json
{"output": "F\n======================================================================\nFAIL: test_template_cannot_supply_approved_revision (tests.test_artifact_checks.ArtifactTests.test_template_cannot_supply_approved_revision)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/scripts/artifact_checks.py\", line 40, in verify_artifact\n    return _verify(Path(path), expectations)\n  File \"/home/naram/projects/systems/contractor-toolkit/scripts/artifact_checks.py\", line 74, in _verify\n    raise ValueError('approved fields mismatch')\nValueError: approved fields mismatch\n\nThe above exception was the direct cause of the following exception:\n\nValueError: artifact unverified: approved fields mismatch\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 72, in test_template_cannot_supply_approved_revision\n    with self.assertRaisesRegex(ValueError, 'hidden'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: \"hidden\" does not match \"artifact unverified: approved fields mismatch\"\n\n----------------------------------------------------------------------\nRan 1 test in 0.083s\n\nFAILED (failures=1)", "exit_code": 1}
```

Template semantic candidate already failed closed (wrong error, not a bypass); replaced with explicit template rejection behavior before implementation.

## Explicit template rejection RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_template_is_explicitly_rejected
```
```json
{"output": "F\n======================================================================\nFAIL: test_template_is_explicitly_rejected (tests.test_artifact_checks.ArtifactTests.test_template_is_explicitly_rejected)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 69, in test_template_is_explicitly_rejected\n    with self.assertRaisesRegex(ValueError, 'hidden'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n----------------------------------------------------------------------\nRan 1 test in 0.079s\n\nFAILED (failures=1)", "exit_code": 1}
```

## Explicit template rejection GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_template_is_explicitly_rejected
```
```json
{"output": ".\n----------------------------------------------------------------------\nRan 1 test in 0.086s\n\nOK", "exit_code": 0}
```

## Template regression GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks
```
```json
{"output": ".....................\n----------------------------------------------------------------------\nRan 21 tests in 0.659s\n\nOK", "exit_code": 0}
```

## Hidden CSS including canonical CSS RED
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css
```
```json
{"output": "FFFFFFFFF\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='display: none', canonical=True)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='visibility: hidden', canonical=True)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='visibility: collapse', canonical=True)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='visibility: collapse', canonical=False)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='content-visibility: hidden', canonical=True)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='opacity: 0', canonical=True)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='opacity: 0', canonical=False)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='display:/**/none', canonical=True)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n======================================================================\nFAIL: test_hidden_css_is_rejected_even_in_canonical_print_css (tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css) (css='display:/**/none', canonical=False)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/naram/projects/systems/contractor-toolkit/tests/test_artifact_checks.py\", line 74, in test_hidden_css_is_rejected_even_in_canonical_print_css\n    with self.assertRaisesRegex(ValueError, 'hidden.*CSS'):\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError: ValueError not raised\n\n----------------------------------------------------------------------\nRan 1 test in 0.131s\n\nFAILED (failures=9)", "exit_code": 1}
```

## Hidden CSS including canonical CSS GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks.ArtifactTests.test_hidden_css_is_rejected_even_in_canonical_print_css
```
```json
{"output": ".\n----------------------------------------------------------------------\nRan 1 test in 0.083s\n\nOK", "exit_code": 0}
```

## Hidden CSS regression GREEN
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest tests.test_artifact_checks
```
```json
{"output": "......................\n----------------------------------------------------------------------\nRan 22 tests in 0.614s\n\nOK", "exit_code": 0}
```

## Full suite final
```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest discover -s tests
```
```json
{"output": ".................................................................................\n----------------------------------------------------------------------\nRan 81 tests in 28.209s\n\nOK", "exit_code": 0}
```
