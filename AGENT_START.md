# Agent Start

## Purpose

This file is the bounded entry point for agent hosts such as `Codex CLI` or
`Claude Code`.

Use this file instead of guessing the repository structure.

## Required Read Order

Read in this order:

1. `README.md`
2. `START_HERE.md`
3. `REPOSITORY_SCOPE.md`
4. `PUBLIC_STATUS.md`
5. `PUBLIC_BOUNDARY.md`
6. `RELATIONSHIP_TO_FRAMEWORK.md`
7. `docs/workflow_overview.md`
8. `docs/workflow_map.md`
9. `docs/public_registry_slice.md`
10. `docs/public_mechanism_map.md`
11. `docs/direct_execution_readiness.md`
12. `docs/frozen_results_summary.md`
13. `docs/evidence_claim_map.md`

## Validation Command

The public validation command is:

```powershell
python scripts/validate_public_bundle.py --json
```

Run that command before making stronger repository-shape claims.

The runtime-skeleton validation command is:

```powershell
python scripts/validate_runtime_setup.py --json
```

## Agent Boundaries

Do:

- summarize this repository as a bounded public workflow pack
- use repository-provided files as the source of truth
- treat missing local-only materials as intentionally out of public scope unless
  the repository says otherwise
- use `docs/direct_execution_readiness.md` when asked whether this repository is
  already a direct-execution system
- use `docs/runtime_quickstart.md` when asked how the minimal runtime skeleton
  currently works

Do not:

- do not claim this repository is a full public runtime mirror
- do not invent hidden validation commands
- do not infer unpublished local runtime structure from omissions
- do not claim one separately deployed executable unit per coordinate
- do not collapse this repository and the framework repository into one claim
- do not describe this repository as a standalone workflow engine unless a real
  execution runtime has been added
- do not confuse the minimal runtime skeleton with a large autonomous engine

## Relationship Rule

When explaining repository roles:

- `Four-Layer-OCED-M-Framework` explains the framework
- `Research_Workflow` is the workflow-facing companion repository

## Manifest

Machine-oriented pack metadata lives in:

- `pack/manifest.json`
