# Finding 6 workflow coverage

Bounded fail-closed adapter, not pay-app arithmetic certification.

## RED — named missing verification contract

```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest discover -s tests -p test_workflow_checks.py -k test_pay_app_finalization_names_unavailable_checks -v
```

```text
test_pay_app_finalization_names_unavailable_checks (test_workflow_checks.WorkflowTests.test_pay_app_finalization_names_unavailable_checks) ... FAIL

======================================================================
FAIL: test_pay_app_finalization_names_unavailable_checks (test_workflow_checks.WorkflowTests.test_pay_app_finalization_names_unavailable_checks)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/naram/projects/systems/contractor-toolkit/tests/test_workflow_checks.py", line 95, in test_pay_app_finalization_names_unavailable_checks
    self.assertIn(check, result.stderr)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'prior_period' not found in '{"status": "needs_human", "error": "domain-specific legal/safety/billing review adapter unavailable; needs_human", "issuance": "not_issued"}\n'

----------------------------------------------------------------------
Ran 1 test in 0.315s

FAILED (failures=1)
exit_code: 1
```

## GREEN — minimal diagnostic contract

```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest discover -s tests -p test_workflow_checks.py -k test_pay_app_finalization_names_unavailable_checks -v
```

```text
test_pay_app_finalization_names_unavailable_checks (test_workflow_checks.WorkflowTests.test_pay_app_finalization_names_unavailable_checks) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.173s

OK
exit_code: 0
```

## Existing-behavior regression coverage plus GREEN diagnostic

Pay-app mismatch artifacts and the consistent control are all refused by the unavailable adapter. These tests do not claim arithmetic was recomputed.

```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest discover -s tests -p test_workflow_checks.py -v
```

```text
test_changed_approved_amount_invalidates_old_pricing_approval (test_workflow_checks.WorkflowTests.test_changed_approved_amount_invalidates_old_pricing_approval) ... ok
test_consequential_status_cannot_bypass_review (test_workflow_checks.WorkflowTests.test_consequential_status_cannot_bypass_review) ... ok
test_decimal_and_separate_provenance_fail_closed (test_workflow_checks.WorkflowTests.test_decimal_and_separate_provenance_fail_closed) ... ok
test_formal_allowance_approval_bound_to_exact_content (test_workflow_checks.WorkflowTests.test_formal_allowance_approval_bound_to_exact_content) ... ok
test_nonestimate_cannot_reuse_complete_estimator_approvals (test_workflow_checks.WorkflowTests.test_nonestimate_cannot_reuse_complete_estimator_approvals) ... ok
test_pay_app_consistent_control_still_requires_unavailable_adapter (test_workflow_checks.WorkflowTests.test_pay_app_consistent_control_still_requires_unavailable_adapter) ... ok
test_pay_app_finalization_names_unavailable_checks (test_workflow_checks.WorkflowTests.test_pay_app_finalization_names_unavailable_checks) ... ok
test_pay_app_prior_period_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_prior_period_mismatch_cannot_finalize) ... ok
test_pay_app_retainage_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_retainage_mismatch_cannot_finalize) ... ok
test_pay_app_sov_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_sov_mismatch_cannot_finalize) ... ok
test_pay_app_totals_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_totals_mismatch_cannot_finalize) ... ok
test_reindexed_source_still_invalidates_old_approval (test_workflow_checks.WorkflowTests.test_reindexed_source_still_invalidates_old_approval) ... ok
test_resume_after_takeoff_preserves_scope_approval (test_workflow_checks.WorkflowTests.test_resume_after_takeoff_preserves_scope_approval) ... ok
test_resume_before_pricing_requires_no_invented_rates (test_workflow_checks.WorkflowTests.test_resume_before_pricing_requires_no_invented_rates) ... ok
test_unknown_nested_scope_and_missing_scope_approval_block (test_workflow_checks.WorkflowTests.test_unknown_nested_scope_and_missing_scope_approval_block) ... ok
test_wrong_project_evidence_rejected_even_with_fresh_digest (test_workflow_checks.WorkflowTests.test_wrong_project_evidence_rejected_even_with_fresh_digest) ... ok
test_wrong_project_source_rejected_even_with_fresh_approval (test_workflow_checks.WorkflowTests.test_wrong_project_source_rejected_even_with_fresh_approval) ... ok

----------------------------------------------------------------------
Ran 17 tests in 8.735s

OK
exit_code: 0
```

## Full-suite verification (concurrent working tree)

```sh
/tmp/contractor-toolkit-venv/bin/python -m unittest discover -s tests -v
```

```text
test_changed_during_inspection_has_no_receipt (test_artifact_checks.ArtifactTests.test_changed_during_inspection_has_no_receipt) ... ok
test_closed_dialog_cannot_certify_a_visible_revision_mismatch (test_artifact_checks.ArtifactTests.test_closed_dialog_cannot_certify_a_visible_revision_mismatch) ... ok
test_docx_reads_tables_headers_footers_and_split_tokens (test_artifact_checks.ArtifactTests.test_docx_reads_tables_headers_footers_and_split_tokens) ... ok
test_duplicate_attributes_cannot_hide_active_content (test_artifact_checks.ArtifactTests.test_duplicate_attributes_cannot_hide_active_content) ... ok
test_expectation_types_and_nonbody_sections_fail_closed (test_artifact_checks.ArtifactTests.test_expectation_types_and_nonbody_sections_fail_closed) ... ok
test_financial_crossfoot_recomputed_with_explicit_decimal_rounding (test_artifact_checks.ArtifactTests.test_financial_crossfoot_recomputed_with_explicit_decimal_rounding) ... ok
test_html_financial_checks_cannot_be_self_asserted (test_artifact_checks.ArtifactTests.test_html_financial_checks_cannot_be_self_asserted) ... ok
test_html_hidden_fields_and_active_resources_do_not_verify (test_artifact_checks.ArtifactTests.test_html_hidden_fields_and_active_resources_do_not_verify) ... ok
test_html_invisible_subtrees_cannot_supply_required_text (test_artifact_checks.ArtifactTests.test_html_invisible_subtrees_cannot_supply_required_text) ... ok
test_html_receipt_binds_saved_bytes_and_semantics (test_artifact_checks.ArtifactTests.test_html_receipt_binds_saved_bytes_and_semantics) ... ok
test_html_rejects_active_url_attributes (test_artifact_checks.ArtifactTests.test_html_rejects_active_url_attributes) ... ok
test_html_rejects_meta_refresh (test_artifact_checks.ArtifactTests.test_html_rejects_meta_refresh) ... ok
test_html_rejects_submission_attributes (test_artifact_checks.ArtifactTests.test_html_rejects_submission_attributes) ... ok
test_html_rejects_submission_elements (test_artifact_checks.ArtifactTests.test_html_rejects_submission_elements) ... ok
test_html_rejects_unapproved_or_incomplete_content (test_artifact_checks.ArtifactTests.test_html_rejects_unapproved_or_incomplete_content) ... ok
test_pdf_cannot_reuse_source_success_without_text_and_layout_proof (test_artifact_checks.ArtifactTests.test_pdf_cannot_reuse_source_success_without_text_and_layout_proof) ... ok
test_stale_receipt_and_invalid_expectations_fail_closed (test_artifact_checks.ArtifactTests.test_stale_receipt_and_invalid_expectations_fail_closed) ... ok
test_xlsx_cell_scalars_distinguish_booleans_from_numbers (test_artifact_checks.ArtifactTests.test_xlsx_cell_scalars_distinguish_booleans_from_numbers) ... ok
test_xlsx_exact_cells_identity_tokens_and_prior_link (test_artifact_checks.ArtifactTests.test_xlsx_exact_cells_identity_tokens_and_prior_link) ... ok
test_xlsx_formula_text_or_cache_never_proves_financial_result (test_artifact_checks.ArtifactTests.test_xlsx_formula_text_or_cache_never_proves_financial_result) ... ok
test_archive_tampering_is_rejected (test_build_dist.BuildTests.test_archive_tampering_is_rejected) ... ok
test_interrupted_promotion_restores_prior_release (test_build_dist.BuildTests.test_interrupted_promotion_restores_prior_release) ... ok
test_packaged_dependency_closure (test_build_dist.BuildTests.test_packaged_dependency_closure) ... ok
test_preview_is_unpacked_and_release_rejects_tokens (test_build_dist.BuildTests.test_preview_is_unpacked_and_release_rejects_tokens) ... ok
test_release_archives_match_sources_and_generated_helpers (test_build_dist.BuildTests.test_release_archives_match_sources_and_generated_helpers) ... ok
test_release_logo_assets_cannot_be_arbitrary_repository_files (test_build_dist.BuildTests.test_release_logo_assets_cannot_be_arbitrary_repository_files) ... ok
test_staging_preserves_previous_and_rejects_unsafe_destinations (test_build_dist.BuildTests.test_staging_preserves_previous_and_rejects_unsafe_destinations) ... ok
test_json_rejects_hardlink (test_secure_io.SecureIOTests.test_json_rejects_hardlink) ... ok
test_json_rejects_mutation_during_read (test_secure_io.SecureIOTests.test_json_rejects_mutation_during_read) ... ok
test_json_rejects_same_content_inode_swap_at_open (test_secure_io.SecureIOTests.test_json_rejects_same_content_inode_swap_at_open) ... ok
test_json_rejects_symlink_ancestor (test_secure_io.SecureIOTests.test_json_rejects_symlink_ancestor) ... ok
test_compact_guidance_and_honest_manual_gates (test_skill_contracts.GuidanceContracts.test_compact_guidance_and_honest_manual_gates) ... ok
test_consequential_artifact_gates (test_skill_contracts.GuidanceContracts.test_consequential_artifact_gates) ... ok
test_estimating_gates (test_skill_contracts.GuidanceContracts.test_estimating_gates) ... ok
test_factored_resources_preserve_gates (test_skill_contracts.GuidanceContracts.test_factored_resources_preserve_gates) ... ok
test_setup_gates (test_skill_contracts.GuidanceContracts.test_setup_gates) ... ok
test_shared_gates (test_skill_contracts.GuidanceContracts.test_shared_gates) ... ok
test_absent_target_checkpoint_never_creates_target (test_toolkit_guard.GuardTests.test_absent_target_checkpoint_never_creates_target) ... ok
test_approved_exact_change_check_is_read_only (test_toolkit_guard.GuardTests.test_approved_exact_change_check_is_read_only) ... ok
test_artifact_cli_exclusive_receipt (test_toolkit_guard.GuardTests.test_artifact_cli_exclusive_receipt) ... ok
test_markdown_frontmatter_update_preserves_unselected_body (test_toolkit_guard.GuardTests.test_markdown_frontmatter_update_preserves_unselected_body) ... ok
test_nonfinite_selected_config_value_blocks (test_toolkit_guard.GuardTests.test_nonfinite_selected_config_value_blocks) ... ok
test_partial_template_update_preserves_but_never_introduces_tokens (test_toolkit_guard.GuardTests.test_partial_template_update_preserves_but_never_introduces_tokens) ... ok
test_plain_reference_exact_patch_and_receipt_hashes (test_toolkit_guard.GuardTests.test_plain_reference_exact_patch_and_receipt_hashes) ... ok
test_schema_and_adversarial_change_inputs (test_toolkit_guard.GuardTests.test_schema_and_adversarial_change_inputs) ... ok
test_snapshot_and_interrupted_readback (test_toolkit_guard.GuardTests.test_snapshot_and_interrupted_readback) ... ok
test_stale_digest_and_symlink_boundaries (test_toolkit_guard.GuardTests.test_stale_digest_and_symlink_boundaries) ... ok
test_unrequested_boolean_to_integer_change_is_not_equal (test_toolkit_guard.GuardTests.test_unrequested_boolean_to_integer_change_is_not_equal) ... ok
test_yaml_exact_images_and_duplicate_keys (test_toolkit_guard.GuardTests.test_yaml_exact_images_and_duplicate_keys) ... ok
test_validation_cli_and_ci_documented (test_validate_toolkit.DeliveryTests.test_validation_cli_and_ci_documented) ... ok
test_brand_entry_point_is_compact (test_validate_toolkit.MetadataTests.test_brand_entry_point_is_compact) ... ok
test_brand_metadata_is_valid (test_validate_toolkit.MetadataTests.test_brand_metadata_is_valid) ... ok
test_all_inventory_and_strict_frontmatter (test_validate_toolkit.SourceTests.test_all_inventory_and_strict_frontmatter) ... ok
test_asset_logo_must_be_bundled_image_and_dependency_closure_is_source_gate (test_validate_toolkit.SourceTests.test_asset_logo_must_be_bundled_image_and_dependency_closure_is_source_gate) ... ok
test_explanatory_token_literals_have_exact_context_exemptions (test_validate_toolkit.SourceTests.test_explanatory_token_literals_have_exact_context_exemptions) ... ok
test_manifest_consistency_and_names (test_validate_toolkit.SourceTests.test_manifest_consistency_and_names) ... ok
test_markdown_links_and_malformed_tokens_are_not_exempt (test_validate_toolkit.SourceTests.test_markdown_links_and_malformed_tokens_are_not_exempt) ... ok
test_new_reference_and_logo_policy (test_validate_toolkit.SourceTests.test_new_reference_and_logo_policy) ... ok
test_private_runtime_files_and_unknown_frontmatter_block (test_validate_toolkit.SourceTests.test_private_runtime_files_and_unknown_frontmatter_block) ... ok
test_resources_paths_tokens_fail_closed (test_validate_toolkit.SourceTests.test_resources_paths_tokens_fail_closed) ... ok
test_changed_approved_amount_invalidates_old_pricing_approval (test_workflow_checks.WorkflowTests.test_changed_approved_amount_invalidates_old_pricing_approval) ... ok
test_consequential_status_cannot_bypass_review (test_workflow_checks.WorkflowTests.test_consequential_status_cannot_bypass_review) ... ok
test_decimal_and_separate_provenance_fail_closed (test_workflow_checks.WorkflowTests.test_decimal_and_separate_provenance_fail_closed) ... ok
test_formal_allowance_approval_bound_to_exact_content (test_workflow_checks.WorkflowTests.test_formal_allowance_approval_bound_to_exact_content) ... ok
test_nonestimate_cannot_reuse_complete_estimator_approvals (test_workflow_checks.WorkflowTests.test_nonestimate_cannot_reuse_complete_estimator_approvals) ... ok
test_pay_app_consistent_control_still_requires_unavailable_adapter (test_workflow_checks.WorkflowTests.test_pay_app_consistent_control_still_requires_unavailable_adapter) ... ok
test_pay_app_finalization_names_unavailable_checks (test_workflow_checks.WorkflowTests.test_pay_app_finalization_names_unavailable_checks) ... ok
test_pay_app_prior_period_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_prior_period_mismatch_cannot_finalize) ... ok
test_pay_app_retainage_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_retainage_mismatch_cannot_finalize) ... ok
test_pay_app_sov_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_sov_mismatch_cannot_finalize) ... ok
test_pay_app_totals_mismatch_cannot_finalize (test_workflow_checks.WorkflowTests.test_pay_app_totals_mismatch_cannot_finalize) ... ok
test_reindexed_source_still_invalidates_old_approval (test_workflow_checks.WorkflowTests.test_reindexed_source_still_invalidates_old_approval) ... ok
test_resume_after_takeoff_preserves_scope_approval (test_workflow_checks.WorkflowTests.test_resume_after_takeoff_preserves_scope_approval) ... ok
test_resume_before_pricing_requires_no_invented_rates (test_workflow_checks.WorkflowTests.test_resume_before_pricing_requires_no_invented_rates) ... ok
test_unknown_nested_scope_and_missing_scope_approval_block (test_workflow_checks.WorkflowTests.test_unknown_nested_scope_and_missing_scope_approval_block) ... ok
test_wrong_project_evidence_rejected_even_with_fresh_digest (test_workflow_checks.WorkflowTests.test_wrong_project_evidence_rejected_even_with_fresh_digest) ... ok
test_wrong_project_source_rejected_even_with_fresh_approval (test_workflow_checks.WorkflowTests.test_wrong_project_source_rejected_even_with_fresh_approval) ... ok

----------------------------------------------------------------------
Ran 77 tests in 26.706s

OK
exit_code: 0
```
