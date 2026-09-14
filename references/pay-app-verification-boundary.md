# Pay-app verification boundary (bounded v1)

`check-workflow` accepts estimating pricing evidence, not billing evidence.
For `sub-pay-app`, both `approved_for_final` and `final_verified` always fail
with `needs_human` and `not_issued`. Current file hashes, a caller-supplied
`semantic_sha256`, and even complete estimator approvals cannot unlock them.
Contract and incident-report finalization likewise remain adapter-blocked.

The billing adapter is unavailable. The error explicitly names the required
independent checks; it does **not** report that any of them passed or failed:

- `prior_period`: reconcile prior certified amounts and period identity to
  independently read prior-period records for this project.
- `retainage`: recompute applicable retainage from reviewed contract rules and
  eligible earned/stored amounts, including reviewed releases or exceptions.
- `sov`: reconcile line identities and scheduled values against the approved
  schedule of values and approved contract changes; check billing caps.
- `totals`: independently recompute line extensions, cumulative earned amounts,
  retained amounts, previous certificates, and current payment due.

Any future adapter must bind those recomputations to project, revision, exact
source hashes, reviewed contract terms, and independently extracted artifact
semantics (`semantic_sha256`). Merely adding a `checks: passed` field or an
approval purpose must not open the gate. Billing approval is separate from
estimator approval. Human billing review remains pending before a pilot;
no payment approval, submission, or issuance is performed here.

## Executable coverage and its limits

`tests/test_workflow_checks.py` has separate prior-period, retainage, SOV and
current-total mismatch cases with synthetic JSON artifacts. The consistent
control is: prior certificate 200.00, cumulative earned 500.00, retainage
rate 0.10 and amount 50.00, SOV 600.00 + 400.00 = contract 1000.00, current
due 250.00. Each case changes one stated result while refreshing file and
semantic hashes and estimator approvals. Both final statuses are blocked.
The consistent control is also blocked: these are fail-closed boundary tests,
**not tests of a working pay-app arithmetic or artifact parser**.

Additional tests establish wrong-project evidence/source refusal, an internally
consistent changed estimate amount invalidating a prior pricing approval,
reapproval restoring estimate eligibility, and nonestimate refusal despite
complete estimator approvals. Exact execution evidence is in
`tests/workflow-tdd-evidence.md`.

No shared schema changes are required for this bounded behavior. Supporting a
future billing adapter needs a separately reviewed billing evidence/receipt
contract; the current pricing schema must not be relabeled as billing proof.
