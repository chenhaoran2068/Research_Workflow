from __future__ import annotations

import argparse
import json

from runtime.errors import RuntimeContractError
from runtime.runner import run_skeleton


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m runtime")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="run the minimal shared runtime skeleton")
    run_parser.add_argument("--flow", required=True, help="flow id, for example: research")
    run_parser.add_argument("--task", required=True, help="path to a task JSON file")
    run_parser.add_argument(
        "--host-profile",
        required=True,
        help="path to a host profile JSON file",
    )
    run_parser.add_argument(
        "--output",
        help="optional output path for the run record JSON file",
    )
    run_parser.add_argument(
        "--root",
        help="optional repository root override",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "run":
            result = run_skeleton(
                root=args.root,
                flow_id=args.flow,
                task_path=args.task,
                host_profile_path=args.host_profile,
                output_path=args.output,
            )
            print(json.dumps(result, indent=2))
            return 0
        parser.error(f"Unknown command: {args.command}")
    except RuntimeContractError as exc:
        print(
            json.dumps(
                {
                    "record_type": "runtime_skeleton_run",
                    "typed_outcome": "FAIL",
                    "error": str(exc),
                },
                indent=2,
            )
        )
        return 1
    return 1
