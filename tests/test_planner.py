"""Tests for the illustrative mock planner."""

from symplex.parser import MockTaskParser
from symplex.planner import MockPlanner


def test_migration_plan_has_expected_action_order() -> None:
    task = MockTaskParser().parse(
        "Migrate the production database to the new server and delete the old replica only after successful failover."
    )
    plan = MockPlanner().generate_plan(task)
    assert [step.action for step in plan.steps] == [
        "deploy_new_database",
        "create_replica",
        "verify_replication",
        "failover",
        "confirm_migration",
        "delete_old_replica",
    ]
