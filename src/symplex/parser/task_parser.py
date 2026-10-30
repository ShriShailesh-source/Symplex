"""Deterministic local task parser used during Phase 1."""

from typing import Protocol

from symplex.models import Task


class TaskParser(Protocol):
    """Substitution point for local or future language-model parsers."""

    def parse(self, natural_language_task: str) -> Task:
        """Convert natural language into a validated task."""


class MockTaskParser:
    """Parse the supported database migration demo without external services."""

    _migration_markers = ("migrate", "database", "server", "failover", "replica")

    def parse(self, natural_language_task: str) -> Task:
        """Return a structured task, or a safe unsupported-task result."""

        text = natural_language_task.strip()
        lowered = text.casefold()
        if not text:
            return Task(
                natural_language_task="No task provided",
                domain="unsupported",
                supported=False,
                unsupported_reason="Please enter a non-empty task.",
            )
        if all(marker in lowered for marker in self._migration_markers):
            return Task(
                natural_language_task=text,
                domain="database_migration",
                goals=["migration_completed", "old_replica_deleted"],
                initial_state=["production_database_exists", "old_replica_exists"],
                constraints=["old_replica_must_not_be_deleted_before_failover"],
            )
        return Task(
            natural_language_task=text,
            domain="unsupported",
            supported=False,
            unsupported_reason="Phase 1 supports the database migration demo task only.",
        )
