"""Planner protocol and deterministic demonstration planner."""

from typing import Protocol

from symplex.models import Plan, PlanStatus, PlanStep, Task


class Planner(Protocol):
    """Substitution point for mock or future PDDL planner implementations."""

    def generate_plan(self, task: Task) -> Plan:
        """Generate a candidate plan for a task."""


class MockPlanner:
    """Produce a fixed demonstration plan for the migration domain."""

    _actions = (
        "deploy_new_database",
        "create_replica",
        "verify_replication",
        "failover",
        "confirm_migration",
        "delete_old_replica",
    )

    def generate_plan(self, task: Task) -> Plan:
        """Return an illustrative plan; this is not a PDDL solver."""

        if not task.supported or task.domain != "database_migration":
            return Plan(task=task, steps=[], status=PlanStatus.UNSUPPORTED)
        steps = [
            PlanStep(step_number=index, action=action)
            for index, action in enumerate(self._actions, start=1)
        ]
        return Plan(task=task, steps=steps, status=PlanStatus.CANDIDATE)
