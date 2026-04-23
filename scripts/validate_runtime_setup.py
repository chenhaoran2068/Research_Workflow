from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from jsonschema import Draft202012Validator

from runtime.errors import RuntimeContractError
from runtime.loader import (
    load_flow_bundle,
    load_host_profile,
    load_task,
    read_json,
    resolve_repo_root,
)
from runtime.runner import run_skeleton

ROOT = resolve_repo_root()


def add_check(results: list[dict[str, object]], check_id: str, status: str, detail: str) -> None:
    results.append(
        {
            "check_id": check_id,
            "status": status,
            "detail": detail,
        }
    )


def validate_run_record(path: Path, schema_path: Path) -> None:
    schema = read_json(schema_path)
    instance = read_json(path)
    validator = Draft202012Validator(
        schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = sorted(validator.iter_errors(instance), key=lambda error: error.json_path)
    if errors:
        first = errors[0]
        raise RuntimeContractError(f"run record validation failed at {first.json_path}: {first.message}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON summary")
    args = parser.parse_args()

    results: list[dict[str, object]] = []

    required_files = [
        "requirements.txt",
        "runtime/__main__.py",
        "runtime/cli.py",
        "runtime/loader.py",
        "runtime/runner.py",
        "configs/host_profiles/codex_cli.json",
        "configs/host_profiles/claude_code.json",
        "docs/runtime_quickstart.md",
        "docs/host_modes.md",
        "runs/README.md",
    ]
    for rel_path in required_files:
        path = ROOT / rel_path
        if path.is_file():
            add_check(results, f"exists:{rel_path}", "PASS", "required file present")
        else:
            add_check(results, f"exists:{rel_path}", "FAIL", "required file missing")

    try:
        load_flow_bundle(ROOT, "research")
        add_check(results, "runtime:load_flow_bundle", "PASS", "research flow bundle loaded")
    except RuntimeContractError as exc:
        add_check(results, "runtime:load_flow_bundle", "FAIL", str(exc))

    try:
        bundle = load_flow_bundle(ROOT, "research")
        load_task(ROOT, "flows/research/examples/sample_task.json", bundle.task_schema)
        add_check(results, "runtime:validate_sample_task", "PASS", "sample task validated")
    except RuntimeContractError as exc:
        add_check(results, "runtime:validate_sample_task", "FAIL", str(exc))

    try:
        load_host_profile(ROOT, "configs/host_profiles/codex_cli.json")
        add_check(results, "runtime:validate_host_profile", "PASS", "host profile validated")
    except RuntimeContractError as exc:
        add_check(results, "runtime:validate_host_profile", "FAIL", str(exc))

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "run_record.json"
            result = run_skeleton(
                root=ROOT,
                flow_id="research",
                task_path="flows/research/examples/sample_task.json",
                host_profile_path="configs/host_profiles/codex_cli.json",
                output_path=output_path,
            )
            if result["typed_outcome"] != "PASS":
                raise RuntimeContractError("runtime skeleton returned a non-PASS outcome")
            validate_run_record(output_path, ROOT / "schemas" / "run_record.schema.json")
            add_check(
                results,
                "runtime:dry_run_and_run_record",
                "PASS",
                "dry run succeeded and emitted a valid run record",
            )
    except RuntimeContractError as exc:
        add_check(results, "runtime:dry_run_and_run_record", "FAIL", str(exc))

    pass_count = sum(1 for result in results if result["status"] == "PASS")
    fail_count = sum(1 for result in results if result["status"] == "FAIL")
    typed_outcome = "PASS" if fail_count == 0 else "FAIL"

    summary = {
        "record_type": "research_workflow_runtime_setup_validation",
        "typed_outcome": typed_outcome,
        "workspace_root": str(ROOT),
        "check_count": len(results),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "checks": results,
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print("# Research_Workflow Runtime Setup Validation")
        print()
        print(f"- typed_outcome: `{typed_outcome}`")
        print(f"- pass_count: `{pass_count}`")
        print(f"- fail_count: `{fail_count}`")
        print()
        print("## Checks")
        print()
        for result in results:
            print(f"- `{result['check_id']}`: {result['status']} - {result['detail']}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
