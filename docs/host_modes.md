# Host Modes

## Purpose

This file explains how host binding is interpreted in the current runtime
skeleton.

## Current Rule

The repository may support more than one host family overall.

Current public samples include:

- `Codex CLI`
- `Claude Code`

But one run should bind to one active host profile at a time.

## Why One Host Per Run

This keeps:

- determinacy stronger
- auditability clearer
- attribution cleaner
- recovery simpler

## Current Sample Host Profiles

Public sample profiles live under:

- `configs/host_profiles/codex_cli.json`
- `configs/host_profiles/claude_code.json`

Each profile declares:

- host family
- host backend
- interaction mode
- model profile
- tool policy profile
- approval mode
- capabilities

## Current Interaction Modes

The current public starter pack supports these interaction modes at contract
level:

- `agent_assisted`
- `direct_runtime`
- `hosted_backend`

Current public sample host profiles use:

- `agent_assisted`

## Boundary Rule

These host profiles are public sample bindings.

They are **not** secret-bearing deployment configurations.
