from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "START_HERE.md",
    "REPOSITORY_SCOPE.md",
    "PUBLIC_STATUS.md",
    "PUBLIC_BOUNDARY.md",
    "PUBLIC_CONTENTS.md",
    "RELATIONSHIP_TO_FRAMEWORK.md",
    "VALIDATION.md",
    "AGENT_START.md",
    "pack/manifest.json",
    "docs/direct_execution_readiness.md",
    "docs/workflow_overview.md",
    "docs/workflow_map.md",
    "docs/workflow_reading_order.md",
    "docs/public_registry_slice.md",
    "docs/public_mechanism_map.md",
    "docs/frozen_results_summary.md",
    "docs/evidence_claim_map.md",
    "docs/v1_readiness_review.md",
]

TEXT_CHECKS = {
    "README.md": [
        "public workflow-facing repository",
        "not a full public runtime mirror",
        "download-and-validate",
    ],
    "PUBLIC_STATUS.md": [
        "`v1 ready`",
        "sealed current route",
    ],
    "PUBLIC_BOUNDARY.md": [
        "cleaned public workflow pack",
        "not a full public mirror",
    ],
    "RELATIONSHIP_TO_FRAMEWORK.md": [
        "workflow-facing companion repository",
        "Four-Layer-OCED-M-Framework",
    ],
    "VALIDATION.md": [
        "python scripts/validate_public_bundle.py --json",
    ],
    "AGENT_START.md": [
        "python scripts/validate_public_bundle.py --json",
        "do not claim",
    ],
    "docs/direct_execution_readiness.md": [
        "agent-usable public workflow pack",
        "direct-execution system",
    ],
    "docs/frozen_results_summary.md": [
        "exp_base_01_2026-04-22T121910Z",
        "exp_sys_02_2026-04-22T124401Z",
    ],
}


def read_text(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def add_check(results: list[dict[str, object]], check_id: str, status: str, detail: str) -> None:
    results.append(
        {
            "check_id": check_id,
            "status": status,
            "detail": detail,
        }
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON summary")
    args = parser.parse_args()

    results: list[dict[str, object]] = []

    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if path.is_file():
            add_check(results, f"exists:{rel_path}", "PASS", "required file present")
        else:
            add_check(results, f"exists:{rel_path}", "FAIL", "required file missing")

    for rel_path, patterns in TEXT_CHECKS.items():
        path = ROOT / rel_path
        if not path.is_file():
            add_check(
                results,
                f"text:{rel_path}",
                "FAIL",
                "text check skipped because file is missing",
            )
            continue
        text = read_text(rel_path)
        missing = [pattern for pattern in patterns if pattern not in text]
        if missing:
            add_check(
                results,
                f"text:{rel_path}",
                "FAIL",
                f"missing expected text markers: {', '.join(missing)}",
            )
        else:
            add_check(results, f"text:{rel_path}", "PASS", "expected text markers found")

    manifest_path = ROOT / "pack" / "manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            required_keys = {
                "pack_name",
                "pack_kind",
                "version",
                "status",
                "entry_files",
                "workflow_docs",
                "validation",
                "agent_entry",
                "evidence",
                "claim_boundaries",
            }
            missing_keys = sorted(required_keys - set(manifest))
            if missing_keys:
                add_check(
                    results,
                    "manifest:keys",
                    "FAIL",
                    f"manifest missing keys: {', '.join(missing_keys)}",
                )
            elif manifest.get("validation", {}).get("command") != "python scripts/validate_public_bundle.py --json":
                add_check(
                    results,
                    "manifest:validation_command",
                    "FAIL",
                    "manifest validation command does not match expected public command",
                )
            else:
                add_check(results, "manifest:shape", "PASS", "manifest shape is valid")
        except json.JSONDecodeError as exc:
            add_check(results, "manifest:json", "FAIL", f"manifest JSON decode failed: {exc}")
    else:
        add_check(results, "manifest:json", "FAIL", "manifest file missing")

    pass_count = sum(1 for result in results if result["status"] == "PASS")
    fail_count = sum(1 for result in results if result["status"] == "FAIL")
    typed_outcome = "PASS" if fail_count == 0 else "FAIL"

    summary = {
        "record_type": "research_workflow_public_bundle_validation",
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
        print("# Research_Workflow Public Bundle Validation")
        print()
        print(f"- typed_outcome: `{typed_outcome}`")
        print(f"- pass_count: `{pass_count}`")
        print(f"- fail_count: `{fail_count}`")
        print()
        print("## Checks")
        print()
        for result in results:
            print(
                f"- `{result['check_id']}`: {result['status']} - {result['detail']}"
            )

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
