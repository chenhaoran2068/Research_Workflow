from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from runtime.errors import RuntimeContractError
from runtime.loader import (
    FlowBundle,
    load_flow_bundle,
    load_host_profile,
    load_task,
    read_json,
    relative_to_root,
    resolve_repo_root,
    validate_instance,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_run_id(flow_id: str, host_backend: str) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{flow_id}.{host_backend}.{timestamp}"


def ensure_host_is_supported(bundle: FlowBundle, host_profile: dict[str, Any]) -> None:
    host_mode = host_profile["interaction_mode"]
    flow_supported = bundle.flow_contract["supported_host_modes"]
    policy_supported = bundle.policy_definition["supported_host_modes"]
    if host_mode not in flow_supported:
        raise RuntimeContractError(
            f"Host interaction mode '{host_mode}' is not supported by flow contract for '{bundle.flow_id}'"
        )
    if host_mode not in policy_supported:
        raise RuntimeContractError(
            f"Host interaction mode '{host_mode}' is not supported by policy for '{bundle.flow_id}'"
        )

    tool_profiles = bundle.policy_definition.get("tool_policy_profiles", {})
    tool_policy_profile = host_profile["tool_policy_profile"]
    if tool_policy_profile not in tool_profiles:
        raise RuntimeContractError(
            f"Host profile requests unknown tool policy profile '{tool_policy_profile}'"
        )

    binding_rule = bundle.policy_definition.get("host_binding_rule")
    if binding_rule != "one_active_host_binding_per_run":
        raise RuntimeContractError(
            f"Unsupported host binding rule for runtime skeleton: {binding_rule!r}"
        )


def ensure_output_path(repo_root: Path, flow_id: str, host_backend: str, output_path: str | Path | None) -> tuple[str, Path]:
    run_id = build_run_id(flow_id, host_backend)
    if output_path is None:
        output = repo_root / "runs" / "generated" / run_id / "run_record.json"
    else:
        output = Path(output_path)
        if not output.is_absolute():
            output = repo_root / output
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    return run_id, output


def write_audit_log(
    repo_root: Path,
    audit_log_path: Path,
    run_id: str,
    bundle: FlowBundle,
    task_path: Path,
    host_profile_path: Path,
    host_profile: dict[str, Any],
) -> None:
    lines = [
        "# Runtime Skeleton Audit",
        "",
        f"- run_id: `{run_id}`",
        f"- flow_id: `{bundle.flow_id}`",
        f"- host_backend: `{host_profile['host_backend']}`",
        f"- host_mode: `{host_profile['interaction_mode']}`",
        f"- flow_contract: `{relative_to_root(bundle.flow_path, repo_root)}`",
        f"- route_definition: `{relative_to_root(bundle.route_path, repo_root)}`",
        f"- policy_definition: `{relative_to_root(bundle.policy_path, repo_root)}`",
        f"- task_input: `{relative_to_root(task_path, repo_root)}`",
        f"- host_profile: `{relative_to_root(host_profile_path, repo_root)}`",
        "",
        "This audit file records a minimal runtime dry run.",
        "It does not claim that full autonomous workflow advancement occurred.",
    ]
    audit_log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_run_record(
    repo_root: Path,
    run_id: str,
    bundle: FlowBundle,
    task: dict[str, Any],
    task_path: Path,
    host_profile: dict[str, Any],
    host_profile_path: Path,
    output_path: Path,
    audit_log_path: Path,
    started_at: str,
    finished_at: str,
) -> dict[str, Any]:
    record = {
        "record_type": "workflow_run_record",
        "run_id": run_id,
        "flow_id": bundle.flow_id,
        "task_id": task["task_id"],
        "status": "succeeded",
        "host_mode": host_profile["interaction_mode"],
        "host_backend": host_profile["host_backend"],
        "model_profile": host_profile["model_profile"],
        "tool_policy_profile": host_profile["tool_policy_profile"],
        "approval_mode": host_profile["approval_mode"],
        "started_at": started_at,
        "finished_at": finished_at,
        "checkpoint_count": 0,
        "audit_log_path": relative_to_root(audit_log_path, repo_root),
        "artifacts": [
            relative_to_root(bundle.flow_path, repo_root),
            relative_to_root(bundle.route_path, repo_root),
            relative_to_root(bundle.policy_path, repo_root),
            relative_to_root(bundle.task_schema_path, repo_root),
            relative_to_root(task_path, repo_root),
            relative_to_root(host_profile_path, repo_root),
            relative_to_root(audit_log_path, repo_root),
            relative_to_root(output_path, repo_root),
        ],
        "disposition": {
            "outcome": "accepted",
            "summary": (
                "Minimal runtime skeleton completed: flow contract loaded, task validated, "
                "host profile bound, run record emitted. No autonomous workflow advancement executed."
            ),
        },
    }
    run_record_schema = read_json(repo_root / "schemas" / "run_record.schema.json")
    validate_instance(record, run_record_schema, "run record")
    return record


def run_skeleton(
    root: str | Path | None,
    flow_id: str,
    task_path: str | Path,
    host_profile_path: str | Path,
    output_path: str | Path | None = None,
) -> dict[str, Any]:
    repo_root = resolve_repo_root(root)
    started_at = utc_now_iso()

    bundle = load_flow_bundle(repo_root, flow_id)
    task_file_path, task = load_task(repo_root, task_path, bundle.task_schema)
    profile_path, host_profile = load_host_profile(repo_root, host_profile_path)
    ensure_host_is_supported(bundle, host_profile)

    run_id, output_file_path = ensure_output_path(
        repo_root,
        flow_id=bundle.flow_id,
        host_backend=host_profile["host_backend"],
        output_path=output_path,
    )
    audit_log_path = output_file_path.parent / "audit_log.md"
    write_audit_log(
        repo_root,
        audit_log_path,
        run_id,
        bundle,
        task_file_path,
        profile_path,
        host_profile,
    )

    finished_at = utc_now_iso()
    record = build_run_record(
        repo_root,
        run_id,
        bundle,
        task,
        task_file_path,
        host_profile,
        profile_path,
        output_file_path,
        audit_log_path,
        started_at,
        finished_at,
    )
    output_file_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

    return {
        "record_type": "runtime_skeleton_run",
        "typed_outcome": "PASS",
        "run_id": run_id,
        "flow_id": bundle.flow_id,
        "host_backend": host_profile["host_backend"],
        "task_id": task["task_id"],
        "output_path": relative_to_root(output_file_path, repo_root),
        "audit_log_path": relative_to_root(audit_log_path, repo_root),
    }
