# Research Workflow

This repository is being prepared as the public workflow-facing repository for
the `Research` workflow.

Its intended role is:

- the main public workflow instantiation repository for `Research`
- a repository for a cleaned public workflow example
- the public workflow-facing companion repository to
  `Four-Layer-OCED-M-Framework`

This repository is **not** a full public runtime mirror of the local research
system.

Plainly:

- this repository is not a full public runtime mirror

It exists to present the `Research` workflow in public-safe workflow-pack
form:

- readable without private oral context
- bounded by explicit public scope
- eventually validatable through explicit public-safe commands
- later usable with agent hosts through repository-provided entry files

## What This Repository Is

- a public workflow-pack repository
- a workflow-facing repository rather than a framework-only repository
- a place for cleaned public workflow materials, explicit scope statements, and
  later public-safe validation and evidence summaries

## What This Repository Is Not

- not a full mirror of the local `Clinical_Research_System`
- not a dump of raw experiment runs or raw evidence packs
- not the paper itself
- not a claim that the entire local research runtime is already public

## Current Public Status

The repository is now `v1 ready` for a first public workflow-pack release.

Current truth:

- the local `Research` workflow already has a sealed current route
- a frozen baseline experiment bundle already exists locally
- this public repository now exposes a bounded public workflow-pack surface
  over that local source base
- a public validation command, agent entry file, and compact frozen evidence
  summary are present

Current limit:

- this repository is still **not** a full public runtime mirror
- this repository is still **not** the full raw evidence archive
- later strengthening work remains possible in future versions

For the precise status statement, read `PUBLIC_STATUS.md`.
For the readiness decision, read `docs/v1_readiness_review.md`.

## Relationship To The Framework Repository

The framework repository and this repository do different jobs.

- framework repository:
  `https://github.com/chenhaoran2068/Four-Layer-OCED-M-Framework`
- workflow repository:
  `https://github.com/chenhaoran2068/Research_Workflow`

Short version:

- `Four-Layer-OCED-M-Framework` explains the framework
- `Research_Workflow` presents a workflow-facing public instantiation lane

For the exact wording discipline, read `RELATIONSHIP_TO_FRAMEWORK.md`.

## Reading Start

Start here:

1. `START_HERE.md`
2. `REPOSITORY_SCOPE.md`
3. `PUBLIC_STATUS.md`
4. `PUBLIC_BOUNDARY.md`
5. `RELATIONSHIP_TO_FRAMEWORK.md`
6. `docs/direct_execution_readiness.md`

## v1 Target

`Research_Workflow v1` currently supports:

- `download-and-read`
- `download-and-validate`
- bounded `agent-assisted use`

It is **not** intended to be a first-release full deployment mirror.

It is also **not** yet a standalone direct-execution workflow engine.

For the exact distinction between:

- an agent-usable workflow pack
- and a direct-execution system

read:

- `docs/direct_execution_readiness.md`

For a future architecture sketch beyond the current `v1` target, read:

- `docs/future_download_and_run_blueprint.md`

For the concrete shared-runtime contract that future flow packs should follow,
read:

- `docs/multi_flow_runtime_contract.md`

For machine-readable contract surfaces that later implementation work can
follow, read:

- `schemas/flow_pack_contract.schema.json`
- `schemas/host_profile.schema.json`
- `schemas/run_record.schema.json`

## Phase C Starter Surface

The repository now also contains the first standard flow-pack starter surface
for the `research` flow under:

- `flows/research/README.md`
- `flows/research/flow.yaml`
- `flows/research/route.yaml`
- `flows/research/task_schema.json`
- `flows/research/policy.yaml`

This means:

- the first contract-facing flow definition layer is now present

It does **not** mean:

- a full shared runtime already exists
- a full direct-execution engine is already implemented
