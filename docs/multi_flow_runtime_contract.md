# Multi-Flow Runtime Contract

## Purpose

This file defines the next design layer after the current `v1` public
workflow-pack release.

It does **not** claim that the runtime already exists.

It defines:

- how a shared runtime layer should relate to flow packs
- how `Research_Workflow` should evolve into the first standard flow pack
- how future packs such as `Data_Workflow` and `Knowledge_Workflow` should join
  the same contract

## Current Status

Current repository truth:

- `Research_Workflow` is already a public workflow pack
- it is readable
- it is publicly validatable
- it is usable in bounded `agent-assisted` form

Current repository limit:

- it is not yet a standalone multi-flow runtime system
- it does not yet ship a full runtime-owned task engine

This contract is therefore a **forward contract**, not a false present-tense
deployment claim.

## Contract Actors

The future system should be designed around four actors.

### 1. Shared Runtime Layer

This layer is responsible for:

- loading a selected flow pack
- validating the selected task input
- binding one host profile for one run
- enforcing tool policy
- advancing workflow state
- writing audit outputs and artifacts

### 2. Standard Flow Pack

This is the unit a runtime should load.

A standard flow pack is:

- host-agnostic
- flow-specific
- readable by humans
- machine-readable by the runtime

Examples:

- `Research_Workflow`
- future `Data_Workflow`
- future `Knowledge_Workflow`

### 3. Host Profile

This tells the runtime what execution host or backend is bound to the run.

Examples:

- `codex_cli`
- `claude_code`
- `direct_runtime_local_model`

### 4. Run Record

This is the machine-readable record of one execution.

It should preserve:

- which flow ran
- which host/backend was bound
- which model profile and tool policy were active
- what happened
- what was produced

## Core Rules

### Rule 1: One Shared Runtime, Many Flow Packs

The runtime should be generic.

It should not be hard-coded only for `research`.

Instead:

- shared logic belongs in the runtime layer
- flow-specific logic belongs in the flow pack

### Rule 2: Additive Growth Only

The runtime layer must be added **on top of** the current public workflow-pack
surface.

Do not:

- destroy the current reading surface
- destroy the public validation surface
- replace public documents with an opaque engine-only repository

### Rule 3: Host-Agnostic Pack, Explicit Host Binding Per Run

A flow pack should not be written as if it only works with one host vendor.

Instead:

- the pack stays host-agnostic
- the run record declares which host/backend was actually used

### Rule 4: One Active Host Binding Per Run

The system may support more than one host family overall.

For example:

- `Codex`
- `Claude Code`
- direct local runtime

But one live run should bind to one active host/backend profile at a time.

Reason:

- it preserves determinacy
- it preserves auditability
- it makes recovery and replay simpler
- it preserves attribution clarity

## Minimum Contract Surface

The future multi-flow system needs four minimum contract surfaces:

1. standard flow-pack contract
2. host profile contract
3. run record contract
4. runtime loading contract

## Runtime Loading Contract

For one run, the runtime should operate in this order:

1. select one pack
2. select one flow inside that pack
3. validate pack metadata
4. validate flow definition files
5. validate task input against task schema
6. bind one host profile
7. bind one tool policy profile
8. create one run record
9. advance the workflow
10. write outputs, checkpoints, and final disposition

The runtime should not start real execution if contract validation fails.

## Standard Flow Pack: Minimum Required Files

The minimum future standard for a runnable flow pack should be:

### Repository-Level Required Files

- `README.md`
- `START_HERE.md`
- `PUBLIC_BOUNDARY.md`
- `AGENT_START.md`
- `pack/manifest.json`

These preserve:

- human entry
- public boundary
- agent entry
- pack identity

### Flow-Level Required Files

Under a future standard directory such as `flows/<flow_id>/`, the pack should
minimally contain:

- `flow.yaml`
- `route.yaml`
- `task_schema.json`
- `policy.yaml`

Recommended additions:

- `prompts/`
- `templates/`
- `examples/`
- `baselines/`

## Standard Flow Pack: Minimum Required Fields

At minimum, a standard flow pack should declare:

- `pack_id`
- `pack_version`
- `flow_id`
- `flow_version`
- `entry_mode`
- `task_schema_path`
- `route_definition_path`
- `policy_definition_path`
- `supported_host_modes`
- `claim_boundaries`

## Host Profile: Minimum Required Fields

At minimum, a host profile should declare:

- `profile_id`
- `host_family`
- `host_backend`
- `interaction_mode`
- `model_profile`
- `tool_policy_profile`
- `approval_mode`
- `capabilities`

The capabilities surface should at least describe:

- file I/O
- shell execution
- git operations
- search or web access

## Run Record: Minimum Required Fields

At minimum, a run record should declare:

- `record_type`
- `run_id`
- `flow_id`
- `task_id`
- `status`
- `host_mode`
- `host_backend`
- `model_profile`
- `tool_policy_profile`
- `approval_mode`
- `started_at`
- `artifacts`
- `disposition`

Recommended additions:

- `checkpoint_count`
- `audit_log_path`
- `error_summary`
- `replay_reference`

## Acceptance Standard For "Standard Flow Pack"

`Research_Workflow` should only be described as a full standard flow pack for a
shared runtime if all of the following become true:

1. the minimum flow-level files exist
2. the machine-readable schemas are satisfied
3. one host binding is explicit per run
4. one run record is emitted per run
5. runtime validation fails closed when the contract is broken

Until then, the safer truth is:

- `Research_Workflow` is the first public workflow pack preparing for that
  standard

## Recommended Adoption Path

### Phase A: Current State

What already exists:

- public reading surface
- public validation surface
- compact frozen evidence layer
- bounded agent-assisted entry

### Phase B: Contract Definition

What this round adds:

- stable contract explanation
- machine-readable schemas
- repository indexing for the future runtime contract

### Phase C: First Standard Pack Upgrade

What should be added later:

- `flows/research/flow.yaml`
- `flows/research/route.yaml`
- `flows/research/task_schema.json`
- `flows/research/policy.yaml`

### Phase D: Shared Runtime Skeleton

What should be added after that:

- runtime loader
- pack validator
- host profile loader
- run record emitter
- smoke-run entrypoint

### Phase E: Multi-Flow Expansion

What becomes possible then:

- `Data_Workflow`
- `Knowledge_Workflow`
- one runtime loading more than one flow family

## Review Questions

Before implementation begins, the following questions should be answerable from
repository materials alone:

1. what is the contract boundary between runtime and flow pack?
2. what files must a standard flow pack include?
3. what fields must a host profile include?
4. what fields must a run record include?
5. can more than one host be supported overall?
6. can more than one host control the same run at once?

The intended answers are:

- the boundary is explicit
- the files are listed
- the fields are listed
- more than one host can be supported overall
- one active host should control one run at a time

## Practical Conclusion

The next correct build target is:

- define one shared runtime contract
- upgrade `Research_Workflow` toward that standard
- add future packs against the same contract

That is safer than:

- building a large research-only runtime first
- hard-coding runtime assumptions to `research`
- claiming multi-flow support before the contract exists
