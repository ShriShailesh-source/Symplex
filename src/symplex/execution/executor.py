"""Safe simulated execution interface."""

from typing import Protocol

from pydantic import BaseModel, ConfigDict

from symplex.models import Plan, PlanStatus


class ExecutionResult(BaseModel):
    """Summary of simulated plan execution."""

    model_config = ConfigDict(extra="forbid")

    completed: bool
    simulated_actions: list[str]
    message: str


class Executor(Protocol):
    """Substitution point for simulation or future execution adapters."""

    def execute(self, plan: Plan) -> ExecutionResult:
        """Execute or simulate a plan and return a structured result."""


class SimulatedExecutor:
    """Record intended actions without contacting external systems."""

    def execute(self, plan: Plan) -> ExecutionResult:
        """Simulate each action in a supported candidate plan."""

        if plan.status is not PlanStatus.CANDIDATE:
            return ExecutionResult(
                completed=False,
                simulated_actions=[],
                message="No supported candidate plan was available.",
            )
        return ExecutionResult(
            completed=True,
            simulated_actions=[step.action for step in plan.steps],
            message="Simulation only; no external operations were performed.",
        )
