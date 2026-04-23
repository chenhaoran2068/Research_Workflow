from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from runtime.errors import RuntimeContractError


def resolve_repo_root(root: str | Path | None = None) -> Path:
    if root is None:
        return Path(__file__).resolve().parents[1]
    return Path(root).resolve()


def relative_to_root(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path.resolve())


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeContractError(f"JSON decode failed for {path}: {exc}") from exc


def read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise RuntimeContractError(f"YAML parse failed for {path}: {exc}") from exc


def validate_instance(instance: Any, schema: dict[str, Any], label: str) -> None:
    validator = Draft202012Validator(
        schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = sorted(validator.iter_errors(instance), key=lambda error: error.json_path)
    if not errors:
        return

    first = errors[0]
    location = first.json_path if first.json_path != "$" else label
    raise RuntimeContractError(f"{label} failed schema validation at {location}: {first.message}")


@dataclass
class FlowBundle:
    repo_root: Path
    flow_id: str
    flow_path: Path
    route_path: Path
    policy_path: Path
    task_schema_path: Path
    flow_contract: dict[str, Any]
    route_definition: dict[str, Any]
    policy_definition: dict[str, Any]
    task_schema: dict[str, Any]


def load_flow_bundle(repo_root: Path, flow_id: str) -> FlowBundle:
    schemas_root = repo_root / "schemas"
    flow_schema_path = schemas_root / "flow_pack_contract.schema.json"
    flow_contract_schema = read_json(flow_schema_path)

    flow_path = repo_root / "flows" / flow_id / "flow.yaml"
    if not flow_path.is_file():
        raise RuntimeContractError(f"Flow definition file is missing: {flow_path}")

    flow_contract = read_yaml(flow_path)
    validate_instance(flow_contract, flow_contract_schema, "flow contract")

    if flow_contract["flow_id"] != flow_id:
        raise RuntimeContractError(
            f"Flow id mismatch: requested '{flow_id}' but flow file declares '{flow_contract['flow_id']}'"
        )

    route_path = repo_root / flow_contract["route_definition_path"]
    policy_path = repo_root / flow_contract["policy_definition_path"]
    task_schema_path = repo_root / flow_contract["task_schema_path"]

    for path in (route_path, policy_path, task_schema_path):
        if not path.is_file():
            raise RuntimeContractError(f"Flow contract references a missing file: {path}")

    route_definition = read_yaml(route_path)
    policy_definition = read_yaml(policy_path)
    task_schema = read_json(task_schema_path)

    if route_definition.get("flow_id") != flow_id:
        raise RuntimeContractError(
            f"Route definition flow_id mismatch in {route_path}: expected '{flow_id}'"
        )
    if policy_definition.get("flow_id") != flow_id:
        raise RuntimeContractError(
            f"Policy definition flow_id mismatch in {policy_path}: expected '{flow_id}'"
        )

    return FlowBundle(
        repo_root=repo_root,
        flow_id=flow_id,
        flow_path=flow_path,
        route_path=route_path,
        policy_path=policy_path,
        task_schema_path=task_schema_path,
        flow_contract=flow_contract,
        route_definition=route_definition,
        policy_definition=policy_definition,
        task_schema=task_schema,
    )


def load_host_profile(repo_root: Path, host_profile_path: str | Path) -> tuple[Path, dict[str, Any]]:
    profile_path = Path(host_profile_path)
    if not profile_path.is_absolute():
        profile_path = repo_root / profile_path
    profile_path = profile_path.resolve()

    if not profile_path.is_file():
        raise RuntimeContractError(f"Host profile file is missing: {profile_path}")

    host_schema = read_json(repo_root / "schemas" / "host_profile.schema.json")
    host_profile = read_json(profile_path)
    validate_instance(host_profile, host_schema, "host profile")
    return profile_path, host_profile


def load_task(repo_root: Path, task_path: str | Path, task_schema: dict[str, Any]) -> tuple[Path, dict[str, Any]]:
    candidate = Path(task_path)
    if not candidate.is_absolute():
        candidate = repo_root / candidate
    candidate = candidate.resolve()

    if not candidate.is_file():
        raise RuntimeContractError(f"Task file is missing: {candidate}")

    task = read_json(candidate)
    validate_instance(task, task_schema, "task input")
    return candidate, task
