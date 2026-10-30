"""Interactive Phase 1 demonstration CLI."""

import json
from typing import TextIO

from symplex.logic import PlaceholderVerifier
from symplex.parser import MockTaskParser, TaskParser
from symplex.planner import MockPlanner, Planner


def run_demo(
    parser: TaskParser | None = None,
    planner: Planner | None = None,
    input_stream: TextIO | None = None,
) -> int:
    """Run the parse-plan-verify demonstration and return a process code."""

    import sys

    parser = parser or MockTaskParser()
    planner = planner or MockPlanner()
    input_stream = input_stream or sys.stdin
    print("SYMPLEX\nNeuro-Symbolic Planning and Verification\n")
    print("Enter task:")
    natural_language_task = input_stream.readline().strip()
    task = parser.parse(natural_language_task)
    print("\nParsed Task:")
    print(json.dumps(task.model_dump(), indent=2))
    plan = planner.generate_plan(task)
    if not task.supported:
        print(f"\nUnsupported task: {task.unsupported_reason}")
        print("No plan was generated.")
        return 1
    print("\nGenerated Mock Plan:")
    for step in plan.steps:
        print(f"{step.step_number}. {step.action}")
    result = PlaceholderVerifier().verify(plan)
    print("\nLogical Verification (Phase 1 demo check):")
    print("ACCEPTED" if result.accepted else "REJECTED")
    print(result.reason)
    if result.violations:
        print("Violations: " + ", ".join(result.violations))
    print("\nPhase 1 demo completed successfully." if result.accepted else "\nPhase 1 demo rejected the plan.")
    return 0 if result.accepted else 2


def main() -> None:
    """Run the CLI and exit with its result code."""

    raise SystemExit(run_demo())


if __name__ == "__main__":
    main()
