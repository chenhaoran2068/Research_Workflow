# Public Mechanism Map

## Purpose

This file gives a public-safe summary of how current mechanism identity is
carried in the sealed `Research` stack.

It is not a full export of the local mechanism manifest.

Its job is to show:

- that coordinates are not left as prose-only promises
- that shared compiled mechanisms are allowed
- that shared mechanisms do not erase coordinate-level attribution

## Compile-Accounting Summary

Current public-safe compile-accounting summary:

| Compile state | Count |
| --- | --- |
| `compiled_direct_plus_assembled` | `11` |
| `compiled_assembled_only` | `166` |
| `oced_drafted_not_yet_compiled` | `0` |
| `upstream_normative_anchor_only` | `0` |
| total real coordinates | `177` |

Operational reading:

- every current real coordinate has explicit current-scope compile accounting
- most coordinates are carried through shared assembled mechanisms
- a smaller set also has direct anchor mechanisms
- the stack does **not** claim one separately deployed executable unit per
  coordinate

## Layer-Level Mechanism Reading

### Law

Current public-safe law reading:

- `Law` is machine-carried through a shared current law surface
- the live carried surface is the promoted current surface
- coordinate-level addressability remains explicit even though the carry is
  shared

Representative mechanism identities:

- `mwl.sc05.active_law_policy_bundle_v2`
- `mwl.sc05.law_coordinate_policy_registry_v2`
- `mwl.sc05.law_tail_surface_resolver`

### Object

Current public-safe object reading:

- object support is organized as named current surfaces
- some surfaces are fully schema-frozen
- some remain bridge-backed or have a shared dependency

Representative object support statuses:

- `research_surface_schema_frozen`
- `bridge_backed_surface`
- `surface_with_shared_dependency`

### Runtime

Current public-safe runtime reading:

- runtime identity is carried through controllers, corridors, projectors,
  guards, validators, routers, and wait or hosting surfaces

Representative runtime mechanism identities:

- `mwl.w203.intake_grounding_projector`
- `mwl.w202.pilot_route_disposition_projector`
- `mwl.w304.result_claim_submission_corridor_projector`
- `mwl.w305.external_review_transition_corridor`
- `mwl.w3c4.wait_resume_projector`

### Audit

Current public-safe audit reading:

- audit identity is carried through contracts, lineage guards, projectors,
  compatibility registries, replay registries, and hosting-readiness surfaces

Representative audit mechanism identities:

- `mwl.w204.release_attempt_lineage_guard`
- `mwl.p1s1.review_adjudication_projector`
- `mwl.p1s2.stop_successor_archive_projector`
- `mwl.sc03.intake_family_projector`
- `mwl.sc04.hosting_capability_manifest`

## Representative Mechanism Families

The current stack is easiest to read through mechanism families rather than
through all `177` coordinate rows.

| Mechanism family | Public-safe role |
| --- | --- |
| `w203` family | intake grounding, question binding, readiness binding |
| `w202` family | pilot evidence, route disposition, continuation or redesign classification |
| `w201` family | results, claims, submission package, semantic-license boundaries |
| `p1s1` family | internal review, human adjudication, release-gate handling |
| `p1s2` family | stop, successor, archive, and terminal disposition handling |
| `sc03` family | replay-family widening and compatibility carry |
| `sc04` family | hosting capability and hosting readiness surfaces |
| `sc05` family | live machine-carried law surface |

## Interpretation Rule

This repository should be read as supporting the following claim shape:

- coordinates remain explicit
- mechanism identity is explicit
- shared mechanisms are allowed
- coordinate-level attribution is preserved even when many coordinates land on
  shared mechanisms

This repository should **not** be read as claiming:

- one standalone executable per coordinate
- a full public export of the local mechanism manifest
- a stronger implementation boundary than the current public repository has
  actually published
