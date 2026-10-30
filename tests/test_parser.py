"""Tests for the deterministic Phase 1 task parser."""

from symplex.parser import MockTaskParser


EXAMPLE = "Migrate the production database to the new server and delete the old replica only after successful failover."


def test_database_migration_example_is_parsed() -> None:
    task = MockTaskParser().parse(EXAMPLE)
    assert task.supported is True
    assert task.domain == "database_migration"
    assert task.goals == ["migration_completed", "old_replica_deleted"]


def test_safety_constraint_is_present() -> None:
    task = MockTaskParser().parse(EXAMPLE)
    assert "old_replica_must_not_be_deleted_before_failover" in task.constraints


def test_unsupported_input_returns_structured_fallback() -> None:
    task = MockTaskParser().parse("Plan a picnic in the park")
    assert task.supported is False
    assert task.domain == "unsupported"
    assert task.unsupported_reason


def test_blank_input_returns_structured_fallback() -> None:
    task = MockTaskParser().parse(" ")
    assert task.supported is False
