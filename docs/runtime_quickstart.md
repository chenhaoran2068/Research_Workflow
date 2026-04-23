# Runtime Quickstart

## Purpose

This file explains the current minimal shared runtime skeleton.

It does **not** describe a large autonomous workflow engine.

It describes a small bounded runtime loop that can:

- load one flow definition
- validate one task
- bind one host profile
- emit one run record

## Install

From the repository root, install the small runtime dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Validate Public Pack Surface

First validate the public workflow-pack surface:

```powershell
python scripts/validate_public_bundle.py --json
```

## Validate Runtime Skeleton Surface

Then validate the runtime skeleton surface:

```powershell
python scripts/validate_runtime_setup.py --json
```

Expected successful outcome:

- process exit code: `0`
- JSON field `typed_outcome = "PASS"`

## Run The Minimal Skeleton

Example command:

```powershell
python -m runtime run `
  --flow research `
  --task flows/research/examples/sample_task.json `
  --host-profile configs/host_profiles/codex_cli.json
```

Expected result:

- one run record JSON is emitted under `runs/generated/.../run_record.json`
- one audit note is emitted under `runs/generated/.../audit_log.md`
- the printed JSON summary reports `typed_outcome = "PASS"`

## What This Skeleton Does

The current skeleton does:

1. load `flows/research/flow.yaml`
2. load `route.yaml`, `policy.yaml`, and `task_schema.json`
3. validate one task file
4. validate one host profile
5. check host-mode and tool-policy compatibility
6. emit one run record

## What This Skeleton Does Not Yet Do

The current skeleton does **not** yet:

- advance the full research workflow automatically
- run a graph executor
- orchestrate a full tool chain across many workflow stages
- replace the full local internal research runtime

## Output Interpretation Rule

The emitted run record should be read as:

- proof that the minimal runtime contract loop works

It should not be read as:

- proof that a large autonomous research engine is already public
