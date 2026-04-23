# Future Download-and-Run Blueprint

## Purpose

This file describes a stronger future target for `Research_Workflow`.

It is **not** the current `v1` public-pack claim.

Current status:

- the repository is an agent-usable public workflow pack
- it supports human reading, public validation, and bounded agent-assisted use

Future stronger target:

- the repository, or a closely related runtime layer, can be downloaded and run
  as a real workflow system

## Core Design Rule

The future runtime layer should be **additive**, not destructive.

That means:

- keep the current public pack readable
- keep public boundaries explicit
- keep frozen evidence readable
- keep agent-assisted use possible
- add runtime and execution layers on top

Do **not** collapse everything into one opaque automation engine.

## What "Download-and-Run" Actually Means

A serious download-and-run system should let a user do something like:

```text
git clone ...
cd Research_Workflow
python -m runtime run --flow research --task examples/tasks/sample_task.json
```

and then the system should:

1. load one declared flow
2. validate task input
3. construct run state
4. select tools under policy
5. advance the workflow through explicit runtime logic
6. record audit outputs and artifacts
7. stop with a reconstructable disposition

## Complete Capability Surface

To reach that stronger target, the full system usually needs all of the
following:

1. install surface
2. runnable entrypoint
3. flow registry
4. task schema
5. runtime controller
6. tool abstraction layer
7. tool policy layer
8. state store and checkpoints
9. artifact store
10. audit ledger
11. run outputs
12. validation and tests
13. examples
14. operator documentation
15. host compatibility rules

## Recommended Top-Level Structure

If this stronger target is implemented inside the same repository, a serious
future structure could look like this:

```text
Research_Workflow/
  README.md
  START_HERE.md
  AGENT_START.md
  REPOSITORY_SCOPE.md
  PUBLIC_STATUS.md
  PUBLIC_BOUNDARY.md
  PUBLIC_CONTENTS.md
  RELATIONSHIP_TO_FRAMEWORK.md
  VALIDATION.md

  pyproject.toml
  requirements.lock

  pack/
    manifest.json

  docs/
    workflow_overview.md
    workflow_map.md
    workflow_reading_order.md
    public_registry_slice.md
    public_mechanism_map.md
    frozen_results_summary.md
    evidence_claim_map.md
    direct_execution_readiness.md
    future_download_and_run_blueprint.md
    runtime_quickstart.md
    host_modes.md
    multi_flow_architecture.md

  runtime/
    __main__.py
    cli.py
    runner.py
    graph.py
    scheduler.py
    approvals.py
    policy.py
    audit.py
    checkpoints.py
    errors.py

  flows/
    research/
      flow.yaml
      route.yaml
      task_schema.json
      policy.yaml
      prompts/
      templates/
      examples/
      baselines/
    data/
      flow.yaml
      route.yaml
      task_schema.json
      policy.yaml
      prompts/
      templates/
      examples/
    knowledge/
      flow.yaml
      route.yaml
      task_schema.json
      policy.yaml
      prompts/
      templates/
      examples/

  tools/
    registry.py
    model_client.py
    search.py
    file_io.py
    git_ops.py
    shell_exec.py
    sandbox.py

  schemas/
    flow.schema.json
    route.schema.json
    task.schema.json
    run_record.schema.json
    artifact_manifest.schema.json

  state/
    store.py
    context.py
    artifacts.py
    replay.py
    quarantine.py

  configs/
    default.yaml
    claude_code.yaml
    codex.yaml
    local_model.yaml

  examples/
    tasks/
      sample_research_task.json
      sample_data_task.json
      sample_knowledge_task.json

  tests/
    test_cli.py
    test_flow_loading.py
    test_schema_validation.py
    test_policy_guards.py
    test_replay.py
    integration/
    fixtures/

  scripts/
    validate_public_bundle.py
    validate_runtime_setup.py
    smoke_run.py

  runs/
    .gitkeep
```

## Directory Meaning

### `runtime/`

This is the execution engine.

It should decide:

- what step runs next
- what tool is allowed
- when approval is required
- how failures are handled
- what gets written to audit outputs

### `flows/`

This is where workflow packs become runnable units.

Each flow should define:

- its route
- its task schema
- its policy surface
- its prompts or instruction assets
- its examples and baselines

The current repository is effectively centered on one flow:

- `research`

Later, additional flows could be added, such as:

- `data`
- `knowledge`

## Recommended Multi-Flow Rule

When additional flows are introduced, the safest rule is:

- one shared runtime layer
- many host-agnostic flow packs

In other words:

- do not build one separate runtime per flow
- do not hard-code research-only assumptions into the runtime core

Instead:

- keep runtime generic
- keep flow-specific logic inside each flow directory

## Host Compatibility Rule

The future system should support more than one host mode.

At minimum, the following modes are useful:

1. direct runtime mode
   - user runs the repository through its own CLI
2. agent-assisted mode
   - `Claude Code` or `Codex` reads the pack and helps a user operate it
3. hosted backend mode
   - the runtime calls an external agent host as one backend under policy

## Can Claude Code and Codex "Both Use It"?

Yes, but the exact meaning matters.

### What should be supported

- the same repository can be usable by `Claude Code`
- the same repository can be usable by `Codex`
- the runtime can offer host-specific config profiles
- different runs can choose different hosts

### What should usually **not** happen

- two different hosts should not both control the same live run state at the
  same time

Reason:

- it harms determinacy
- it harms auditability
- it complicates checkpoint recovery
- it makes attribution much weaker

So the better rule is:

- many hosts supported
- one active host binding per run

## Recommended Run Binding Model

Each run record should declare:

- `run_id`
- `flow_id`
- `task_id`
- `host_mode`
- `host_backend`
- `model_profile`
- `tool_policy_profile`
- `approval_mode`

That keeps each execution reconstructable.

## What Should Stay Public-Safe

Even after runtime is added, some public boundary rules should remain:

- no secret keys in the repository
- no hidden local-only dependencies in the public instructions
- no fake claim that every flow is fully autonomous
- no fake claim that public runtime equals the full internal research system

## Better Long-Term Repository Family

Once multiple flows become real, the cleaner long-term architecture is usually:

1. framework repository
   - concepts, structure, boundaries, language
2. runtime repository
   - shared execution engine
3. flow-pack repositories
   - `Research_Workflow`, `Data_Workflow`, `Knowledge_Workflow`, etc.

That structure is cleaner than forcing every future flow into one repository.

## What This Means For `Research_Workflow`

For now, the current repository should remain:

- readable
- validateable
- bounded for agent-assisted use

If a stronger runtime is later built, the safest path is:

1. preserve the current pack surface
2. add runtime as a new layer
3. keep flow definitions explicit
4. keep host bindings explicit per run
5. design for future multi-flow loading from the start

## External Pattern Notes

Observed public projects usually follow one of four patterns:

1. very small host-driven loop
   - compact repo, one editable surface, one metric, agent host does most of
     the work
2. modular research framework
   - reusable modules for theorist, experimentalist, experiment runners, and
     workflow logic
3. template-based runtime
   - one engine plus many templates with standard files
4. full pipeline runtime
   - multi-stage runtime, stronger automation, stronger execution and audit
     machinery

For this repository family, the strongest long-term direction is usually:

- public pack first
- runtime second
- multi-flow loading third
