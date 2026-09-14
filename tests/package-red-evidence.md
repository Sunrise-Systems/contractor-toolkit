## Package standalone copy RED

Command: `/tmp/contractor-toolkit-venv/bin/python -m unittest discover -s tests -p test_package_copy_identity.py -v`

Exit: 1

```text
test_generate_rejects_same_content_replacement_after_inventory (test_package_copy_identity.PackageCopyIdentityTests.test_generate_rejects_same_content_replacement_after_inventory) ... FAIL

======================================================================
FAIL: test_generate_rejects_same_content_replacement_after_inventory (test_package_copy_identity.PackageCopyIdentityTests.test_generate_rejects_same_content_replacement_after_inventory)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/naram/projects/systems/contractor-toolkit/tests/test_package_copy_identity.py", line 30, in test_generate_rejects_same_content_replacement_after_inventory
    with self.assertRaisesRegex(ValueError, 'identity/content changed'):
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 1 test in 0.036s

FAILED (failures=1)
```
