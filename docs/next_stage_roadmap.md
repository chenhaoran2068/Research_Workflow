# Next Stage Roadmap

## Purpose

This file records the stable post-current-stage roadmap for
`Research_Workflow`.

It is meant to answer:

- what should happen next after the current-stage completion surface
- in what order those steps should happen
- what review standard should be met before moving to a larger system phase

## Current Stage Baseline

The current completed baseline is:

- one public workflow pack
- one first standard flow-pack starter surface under `flows/research/`
- one minimal shared runtime skeleton
- one public validation loop
- one runtime validation loop
- one fresh-clone verification pass

This is the correct current baseline.

The roadmap below is about what should happen **after** that baseline.

## Phase E1: Second-Flow Proof

### Goal

Prove that the runtime is not secretly hard-coded only to `research`.

### Intended Deliverable

Add one very small second flow.

This does **not** need to be a full real production workflow yet.

It can be:

- a small `knowledge` starter flow
- or another clearly bounded dummy-but-real second flow

### Minimum Work

The second flow should include:

- `flows/<flow_id>/flow.yaml`
- `flows/<flow_id>/route.yaml`
- `flows/<flow_id>/task_schema.json`
- `flows/<flow_id>/policy.yaml`
- one sample task

### Review Standard

Phase `E1` is complete only if:

- the runtime can load the second flow
- the runtime can validate the second flow task
- the runtime can emit a run record for the second flow
- no research-only assumptions had to be hard-coded into runtime logic

## Phase E2: Runtime Hardening

### Goal

Make the runtime skeleton safer, clearer, and more failure-aware.

### Intended Deliverables

- stronger negative tests
- clearer error messages
- stronger fail-closed behavior
- fuller run-record surface

### Minimum Work

Add at least:

1. negative task validation test
2. invalid host-profile test
3. missing-flow-file test
4. explicit contract-break error surface
5. richer run record fields where justified

### Review Standard

Phase `E2` is complete only if:

- invalid inputs reliably fail closed
- error messages are specific enough for outside users to debug
- run records remain machine-readable and claim-safe

## Decision Gate

## Purpose

Pause before turning the repository into a much larger system.

The decision gate exists because the jump from:

- bounded public pack plus minimal runtime

to:

- large autonomous multi-stage system

is a real architectural phase change.

### Required Questions

Before moving on, answer these questions explicitly:

1. has the runtime been proven with more than one flow?
2. are fail-closed paths trustworthy enough?
3. is the public-pack surface still clean and readable?
4. do we want to keep runtime inside this repository?
5. or is a separate runtime repository now cleaner?

### Go Condition

Move past the decision gate only if:

- `E1` is complete
- `E2` is complete
- repository roles are still clear
- the team explicitly accepts the complexity increase

## Big-System Phase

### Goal

Only after the decision gate, consider a larger system phase.

This phase would mean moving toward:

- fuller automatic stage advancement
- richer runtime state management
- stronger controller logic
- more explicit loop and return handling
- broader multi-flow execution support

### Important Rule

Do **not** treat this phase as a small extension.

It is a new stage.

It may deserve:

- a separate runtime repository
- its own roadmap
- its own validation strategy
- its own release claims

## Activation Rule For Future Flow Creation

If a new public workflow is created, such as:

- `Knowledge_Workflow`
- `Data_Workflow`

then this roadmap should be revisited immediately.

Recommended activation pattern:

1. open this roadmap
2. identify whether the new work belongs to `E1`, `E2`, or a post-gate phase
3. create one temporary execution plan for that specific round
4. complete the round
5. delete the temporary execution plan after completion

## What This Roadmap Is Not

This file is:

- a stable sequencing guide

This file is **not**:

- a temporary worklist
- an automatic trigger by itself
- a claim that later phases are already implemented

## Practical Summary

The intended order is:

1. `E1`: second-flow proof
2. `E2`: runtime hardening
3. decision gate
4. only then consider the big-system phase

That order is safer than jumping directly into a large autonomous runtime.
