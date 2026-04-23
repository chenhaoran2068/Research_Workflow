# Start Here

If you are opening this repository for the first time, read in this order:

1. `README.md`
2. `REPOSITORY_SCOPE.md`
3. `PUBLIC_STATUS.md`
4. `PUBLIC_BOUNDARY.md`
5. `RELATIONSHIP_TO_FRAMEWORK.md`
6. `docs/workflow_overview.md`
7. `docs/workflow_map.md`
8. `docs/public_registry_slice.md`
9. `docs/public_mechanism_map.md`
10. `VALIDATION.md`
11. `AGENT_START.md`
12. `docs/direct_execution_readiness.md`
13. `docs/runtime_quickstart.md`
14. `docs/host_modes.md`
15. `docs/agent_host_usage.md`
16. `docs/frozen_results_summary.md`
17. `docs/evidence_claim_map.md`
18. `docs/v1_readiness_review.md`

That first pass should answer:

- what this repository is
- what it is not
- what is already public here
- what is still being prepared
- how this repository relates to the framework repository

## What To Expect Right Now

This repository is `v1 ready` as a first public workflow pack.

That means:

- the identity and boundary layer is present
- the workflow reading spine is present
- the validation, agent-entry, and frozen-evidence surfaces are present

Do **not** assume that the absence of a file means the local workflow has no
such material.
In many cases it means the public-safe derivative has not yet been authored.

## If You Are A Human Reader

Use this repository as:

- a public-facing workflow-pack reading surface
- a bounded, public-safe workflow explanation

Do not use it as:

- a claim that every local implementation surface is already public

## If You Are Using An Agent Host

Agent rule for the current stage:

- begin from the files listed above
- use `AGENT_START.md` and `pack/manifest.json`
- do not infer unpublished local runtime structure from public omissions
- use `docs/direct_execution_readiness.md` if you need the current execution
  boundary

## Next Likely Strengthening Lane

The next likely strengthening lane is:

- adaptation guidance
- richer ablation summaries
- broader public evidence extensions

## If You Are Exploring The Future Runtime-Facing Starter Layer

Read in this order:

1. `docs/multi_flow_runtime_contract.md`
2. `flows/research/README.md`
3. `flows/research/flow.yaml`
4. `flows/research/route.yaml`
5. `flows/research/task_schema.json`
6. `flows/research/policy.yaml`
7. `flows/research/examples/sample_task.json`
8. `docs/runtime_quickstart.md`
9. `docs/host_modes.md`
10. `docs/agent_host_usage.md`

Interpretation rule:

- this is the first standard flow-pack starter layer
- plus a minimal runtime skeleton
- but it is still not proof that a large autonomous runtime has already been implemented
