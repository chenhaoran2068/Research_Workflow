# Research Flow Starter Surface

## Purpose

This directory is the `Phase C` starter surface for the `research` flow.

It does **not** mean that the shared runtime already exists.

It does mean that the repository now contains the first standard flow-pack
starter files that a future shared runtime can load against.

## Files

- `flow.yaml`
  - machine-readable flow identity and contract-facing paths
- `route.yaml`
  - public-safe route skeleton for the `research` flow
- `task_schema.json`
  - minimum structured task input contract
- `policy.yaml`
  - minimum policy and host-binding rules

Recommended starter support paths also exist:

- `examples/`
- `prompts/`
- `templates/`
- `baselines/`

## Reading Rule

Read this directory as:

- a first standard flow-pack starter layer
- additive to the existing public workflow-pack surface

Do not read this directory as:

- proof that a complete runtime is already implemented
- proof that every local route detail is public
- proof that public examples equal the full local evidence archive
