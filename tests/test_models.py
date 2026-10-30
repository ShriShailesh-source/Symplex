"""Validation tests for Phase 1 data models."""

import pytest
from pydantic import ValidationError

from symplex.models import Plan, PlanStatus, PlanStep, Task


def make_task() -> Task:
    """Build a valid task for model tests."""

    return Task(
        natural_language_task="Migrate production database",
        domain="database_migration",
        goals=["migration_completed"],
    )


def test_task_can_be_created() -> None:
    task = make_task()
    assert task.domain == "database_migration"
    assert task.goals == ["migration_completed"]


def test_invalid_task_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Task(natural_language_task="", domain="")


def test_plan_and_step_work() -> None:
    task = make_task()
    step = PlanStep(step_number=1, action="deploy_new_database")
    plan = Plan(task=task, steps=[step], status=PlanStatus.CANDIDATE)
    assert plan.steps[0].action == "deploy_new_database"
    assert plan.status is PlanStatus.CANDIDATE


def test_invalid_step_number_is_rejected() -> None:
    with pytest.raises(ValidationError):
        PlanStep(step_number=0, action="deploy")
