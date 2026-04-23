# Validation

## Purpose

This repository provides a public-safe validation command so that a new user
does not need to guess what to run.

The goal of this validation surface is modest and explicit:

- confirm that the public workflow pack has the expected entry, boundary,
  workflow, agent-entry, and evidence files
- confirm that key claim-safety markers are present
- confirm that the pack manifest is shaped correctly

It is **not** a claim that the full local research runtime is being executed
publicly here.

## Public Validation Command

Run:

```powershell
python scripts/validate_public_bundle.py --json
```

## Expected Result Shape

Expected successful outcome:

- process exit code: `0`
- JSON field `typed_outcome = "PASS"`
- no failed checks

The validator checks:

- required public files exist
- key claim-safety phrases exist in critical files
- `pack/manifest.json` is valid JSON with the expected public-pack keys

## What This Validation Does Not Do

This command does **not**:

- execute the full local workflow runtime
- rerun the full local experiment archive
- prove industrial deployment completeness
- validate unpublished local artifacts

That boundary is intentional.
