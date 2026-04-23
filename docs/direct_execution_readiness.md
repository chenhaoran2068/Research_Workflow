# Direct Execution Readiness

## Purpose

This file answers a practical architecture question:

- what would it mean for `Research_Workflow` to become a system that
  `Claude Code` or `Codex` can directly execute?
- do we already have that?
- do we need that now?

## First Distinction

Two things should not be confused.

### 1. Agent-Usable Public Workflow Pack

Plain meaning:

- a repository that an agent host can read, validate, and use in bounded form
  through repository-provided entry files

This is the current `v1` target.

Canonical phrase:

- `agent-usable public workflow pack`

### 2. Direct-Execution System

Plain meaning:

- a repository or system where a host can start one explicit execution entry,
  load structured tasks, manage workflow state, call tools through defined
  policies, and advance the workflow automatically

This is a stronger target than the current `v1` public pack.

## What A Direct-Execution System Usually Needs

For the stronger direct-execution target, the following are usually required:

1. executable entrypoint
   - CLI, API, `main.py`, or server entry
2. explicit agent runtime
   - loop, state machine, graph executor, or equivalent runtime controller
3. tooling layer
   - search, code execution, file I/O, git operations, and related tool policy
4. task definition format
   - JSON schema, DSL, or structured config for runnable tasks
5. state management
   - memory, context, artifacts, run state, checkpoints, or equivalent
6. automatic execution chain
   - a real execution path that advances the workflow rather than only
     describing it

## Current Assessment

### 1. Executable Entrypoint

Current status:

- `partial`

What we have:

- `AGENT_START.md`
- `VALIDATION.md`
- `scripts/validate_public_bundle.py`

What we do **not** yet have:

- no workflow-run CLI such as `run_research_workflow.py`
- no API server
- no `main.py` that executes workflow tasks

Judgment:

- we have a validation entrypoint
- we do not yet have a workflow-execution entrypoint

### 2. Explicit Agent Runtime

Current status:

- `no`, at pack-owned runtime level

What we have:

- the host runtime is provided by `Codex CLI` or `Claude Code`
- the repository gives bounded entry instructions for that host

What we do **not** yet have:

- no pack-owned loop
- no pack-owned state machine executor
- no pack-owned graph runtime

Judgment:

- current `v1` depends on the host runtime
- it does not ship its own runtime engine

### 3. Tooling Layer

Current status:

- `partial`

What we have:

- the host already provides tools such as file reading, editing, command
  execution, and git operations
- the repository provides one explicit public validator
- the repository now also exposes a starter flow policy surface at
  `flows/research/policy.yaml`

What we do **not** yet have:

- no pack-owned tool abstraction layer
- no declared tool policy module for search, code exec, file I/O, or git ops
- no workflow-step-to-tool contract layer

Judgment:

- host tools exist
- one starter policy surface now exists
- pack-owned execution tooling still does not yet exist

### 4. Task Definition Format

Current status:

- `partial`

What we have:

- `pack/manifest.json`
- structured repository entry and claim-boundary metadata
- `flows/research/flow.yaml`
- `flows/research/route.yaml`
- `flows/research/task_schema.json`

What we do **not** yet have:

- no direct execution DSL
- no runtime loader that consumes those files end to end
- no task-card execution path that is already live in a runtime

Judgment:

- we have pack metadata
- we now also have a starter runtime-facing task-definition surface
- we still do not yet have a live runtime execution path

### 5. State Management

Current status:

- `partial`

What we have:

- repository documents
- frozen evidence summaries
- manifest metadata
- explicit artifact-oriented reading and validation surfaces

What we do **not** yet have:

- no run-state store
- no checkpoint ledger for public workflow execution
- no persistent context manager for direct execution
- no pack-owned memory subsystem

Judgment:

- we have documentation and artifact state
- we do not yet have runtime state management

### 6. Automatic Execution Chain

Current status:

- `no`, except validation

What we have:

- one automatic public validation chain:
  `python scripts/validate_public_bundle.py --json`

What we do **not** yet have:

- no automatic workflow advancement chain
- no task intake to disposition runner
- no end-to-end runtime automation path

Judgment:

- the repository can validate itself
- it cannot yet execute the workflow automatically

## Short Answer

If the question is:

- "Do we already have a public workflow pack that `Claude Code` / `Codex` can
  use in bounded form?"

Then the answer is:

- `yes`

If the question is:

- "Do we already have a full direct-execution system that `Claude Code` /
  `Codex` can run as an explicit workflow engine?"

Then the answer is:

- `no`

## Do We Need All Of That Now?

For the current `v1` goal:

- `download-and-read`
- `download-and-validate`
- bounded `agent-assisted use`

The answer is:

- `no`, we do not need the full direct-execution stack yet

Reason:

- the host layer already exists
- `Codex CLI` and `Claude Code` already provide the agent runtime and tool
  surface
- current `v1` is a workflow pack, not a standalone workflow engine

## What We Do Need Now

For the current public-pack goal, the really necessary pieces are:

1. explicit human entry
2. explicit agent entry
3. explicit validation command
4. explicit pack manifest
5. explicit workflow reading spine
6. explicit governance slice
7. compact frozen evidence
8. explicit claim boundaries

These are already present in the current repository.

## What We Would Need Later If We Choose The Stronger Target

If we later decide that `Research_Workflow` should become a true
direct-execution system, then we should add a new layer such as:

1. workflow runner entrypoint
   - for example `python run_pack.py`
2. task schema
   - runnable task cards or task manifests
3. execution state store
   - run context, checkpoints, artifacts, and replay state
4. tool policy layer
   - explicit tool contracts and allowed operations by workflow segment
5. runtime controller
   - loop, state machine, or graph runner
6. execution audit outputs
   - machine-readable run records for actual public execution

## Practical Conclusion

Current `Research_Workflow` should be described as:

- a host-agnostic public workflow pack
- agent-usable in bounded form
- carrying a first standard flow-pack starter surface under `flows/research/`
- not yet a standalone direct-execution workflow system

That is not a defect.

It is the correct reading for the current release target.
