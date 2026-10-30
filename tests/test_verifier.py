"""Tests for the Phase 1 verification interface."""

from symplex.logic import PlaceholderVerifier, VerificationResult
from symplex.models import Plan, PlanStatus, PlanStep
from symplex.parser import MockTaskParser
from symplex.planner import MockPlanner


def test_placeholder_verifier_returns_structured_result() -> None:
    task = MockTaskParser().parse(
        "Migrate the production database to the new server and delete the old replica only after successful failover."
    )
    result = PlaceholderVerifier().verify(MockPlanner().generate_plan(task))
    assert isinstance(result, VerificationResult)
    assert result.accepted is True
    assert result.violations == []


def test_demo_verifier_rejects_delete_before_failover() -> None:
    task = MockTaskParser().parse(
        "Migrate the production database to the new server and delete the old replica only after successful failover."
    )
    plan = Plan(
        task=task,
        status=PlanStatus.CANDIDATE,
        steps=[
            PlanStep(step_number=1, action="delete_old_replica"),
            PlanStep(step_number=2, action="failover"),
        ],
    )
    result = PlaceholderVerifier().verify(plan)
    assert not result.accepted
    assert "old_replica_deleted_before_failover" in result.violations
