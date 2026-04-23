# Agent Host Usage

## Purpose

This file explains how a human user can download this repository and use it
with an agent host such as `Codex CLI` or `Claude Code`.

## Current Supported Meaning

At the current stage, "use it with an agent host" means:

- open the repository in the host
- let the host read the bounded repository entry files
- validate the repository surfaces
- optionally run the minimal runtime skeleton

It does **not** mean:

- the host will automatically complete the full research workflow end to end

## Mode A: Agent-Assisted Reading And Validation

### Step 1

Clone the repository and enter the root directory.

### Step 2

Install the small public runtime dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Step 3

Start your chosen host in the repository root.

Examples of supported host families at the current public stage:

- `Codex CLI`
- `Claude Code`

### Step 4

Tell the host to begin from:

- `AGENT_START.md`

Recommended first instruction for the host:

```text
Read AGENT_START.md and follow its required read order.
Treat this repository as a bounded public workflow pack.
Run the public validation command and the runtime-skeleton validation command.
Do not infer unpublished local runtime materials.
```

### Step 5

Ask the host to run:

```powershell
python scripts/validate_public_bundle.py --json
python scripts/validate_runtime_setup.py --json
```

If both return `PASS`, the public pack surface and the minimal runtime skeleton
surface are both in the expected shape.

## Mode B: Agent-Assisted Minimal Runtime Use

After validation succeeds, you can ask the host to run the minimal skeleton.

Example command:

```powershell
python -m runtime run `
  --flow research `
  --task flows/research/examples/sample_task.json `
  --host-profile configs/host_profiles/codex_cli.json
```

This does:

- load the `research` flow
- validate the sample task
- bind one host profile
- emit one run record

## Suggested Prompt For The Host

If you want the host to handle both validation and the minimal dry run, you can
use a prompt like this:

```text
Read AGENT_START.md first.
Treat the repository as a bounded public workflow pack plus a minimal shared runtime skeleton.
Run:
1. python scripts/validate_public_bundle.py --json
2. python scripts/validate_runtime_setup.py --json
3. python -m runtime run --flow research --task flows/research/examples/sample_task.json --host-profile configs/host_profiles/codex_cli.json
Then summarize what passed, what the run record means, and what this repository still does not claim.
```

## Files The Host Should Use

At minimum, the host should rely on:

- `AGENT_START.md`
- `pack/manifest.json`
- `docs/direct_execution_readiness.md`
- `docs/runtime_quickstart.md`
- `docs/host_modes.md`

## What The Host Should Not Do

Do not ask the host to:

- invent unpublished local coordinates
- claim the repository is a full internal runtime mirror
- claim the minimal runtime skeleton equals a large autonomous research engine

## Practical Conclusion

At the current stage, outside users can:

- download the repository
- open it in `Codex` or `Claude Code`
- follow the provided entry files
- validate the repository
- run the minimal runtime dry-run loop

That is the current supported agent-host usage surface.
