# Frozen Results Summary

## Purpose

This file provides a compact public-safe summary of frozen experiment results
that support the public `Research_Workflow` pack.

It is intentionally smaller than the full local evidence archive.

## Evidence Boundary

This file is meant to support public workflow-pack claims such as:

- the sealed route was run and frozen
- the protected surfaces remained clean in the frozen baseline
- a permissive shadow profile did not match governed behavior

This file is **not** meant to be:

- the full paper
- the full raw run archive
- a claim of universal model or workflow safety

## Frozen Baseline

Experiment:

- `EXP-BASE-01`

Frozen run:

- `exp_base_01_2026-04-22T121910Z`

Compact result summary:

- typed outcome: `PASS`
- protected surface clean: `True`
- total invocations: `54/54 PASS`
- total duration: `845.076s`

Frozen baseline metric bundle summary:

- contributing invocation count: `15`
- anchor harness complete: `True`
- repeatability consistent: `True`
- aggregate baseline cases observed across contributing harnesses:
  `50 + 70 + 55 = 175`

Governed baseline metrics:

- `silent_accept_rate = 0.0`
- `fail_closed_block_rate = 1.0`
- `lawful_disposition_determinacy = 1.0`
- `reconstructability_score = 1.0`
- `replay_quarantine_detection_rate = 1.0`
- `currentness_conflict_detection_rate = 1.0`
- `coordinate_attribution_completeness = 1.0`

## Frozen Shadow Comparison

Experiment:

- `EXP-SYS-02`

Frozen run:

- `exp_sys_02_2026-04-22T124401Z`

Comparison posture:

- shadow profile: `permissive_fallthrough_v1`
- protected surface clean: `True`
- total harness invocations: `9`
- total case count: `105`

Compact governed-versus-shadow comparison:

- `silent_accept_rate`: governed `0.0`, shadow `1.0`
- `fail_closed_block_rate`: governed `1.0`, shadow `0.0`
- `lawful_disposition_determinacy`: governed `1.0`, shadow `0.0`
- `reconstructability_score`: governed `1.0`, shadow `0.05`
- `replay_quarantine_detection_rate`: governed `1.0`, shadow `0.0`
- `currentness_conflict_detection_rate`: governed `1.0`, shadow `0.0`
- `coordinate_attribution_completeness`: governed `1.0`, shadow `0.0`

## Public-Safe Reading

At the public-pack level, these frozen results support a bounded reading:

- the sealed governed route remained clean across repeated frozen baseline
  execution
- the current public workflow pack is not supported only by prose
- weakening the route into permissive fallthrough materially changes the
  observed governance behavior

## What This Summary Does Not Claim

This summary does **not** claim:

- benchmark-complete evaluation
- universal superiority over all other systems
- full publication of the raw evidence archive
- proof that no future reratification or fresh activation is ever needed
