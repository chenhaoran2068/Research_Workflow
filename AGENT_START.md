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
11. `docs/frozen_results_summary.md`
12. `docs/evidence_claim_map.md`

## Validation Command

The public validation command is:

```powershell
python scripts/validate_public_bundle.py --json
```

Run that command before making stronger repository-shape claims.

## Agent Boundaries

Do:

- summarize this repository as a bounded public workflow pack
- use repository-provided files as the source of truth
- treat missing local-only materials as intentionally out of public scope unless
  the repository says otherwise

Do not:

- do not claim this repository is a full public runtime mirror
- do not invent hidden validation commands
- do not infer unpublished local runtime structure from omissions
- do not claim one separately deployed executable unit per coordinate
- do not collapse this repository and the framework repository into one claim

## Relationship Rule

When explaining repository roles:

- `Four-Layer-OCED-M-Framework` explains the framework
- `Research_Workflow` is the workflow-facing companion repository

## Manifest

Machine-oriented pack metadata lives in:

- `pack/manifest.json`
