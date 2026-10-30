"""Placeholder interface for future FOL and resolution verification."""

from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field

from symplex.models import Plan, PlanStatus


class VerificationResult(BaseModel):
    """Structured result returned by plan verifiers."""

    model_config = ConfigDict(extra="forbid")

    accepted: bool
    reason: str
    violations: list[str] = Field(default_factory=list)


class Verifier(Protocol):
    """Substitution point for simple or future formal logic verifiers."""

    def verify(self, plan: Plan) -> VerificationResult:
        """Check a candidate plan and explain the outcome."""


class PlaceholderVerifier:
    """Check the demo ordering rule; this is not an FOL resolution engine."""

    def verify(self, plan: Plan) -> VerificationResult:
        """Check that old replica deletion follows failover in the demo plan."""

        if plan.status is not PlanStatus.CANDIDATE:
            return VerificationResult(
                accepted=False,
                reason="No supported candidate plan was provided.",
                violations=["plan_is_not_a_candidate"],
            )
        actions = [step.action for step in plan.steps]
        if "old_replica_must_not_be_deleted_before_failover" in plan.task.constraints:
            if "delete_old_replica" in actions and (
                "failover" not in actions
                or actions.index("delete_old_replica") < actions.index("failover")
            ):
                return VerificationResult(
                    accepted=False,
                    reason="The demo ordering constraint is violated.",
                    violations=["old_replica_deleted_before_failover"],
                )
        return VerificationResult(
            accepted=True,
            reason="Accepted by the Phase 1 demo ordering check; formal FOL verification is not implemented.",
        )
