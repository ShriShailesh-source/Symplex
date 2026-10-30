"""Candidate plan models and lifecycle status."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .task import Task


class PlanStatus(StrEnum):
    """Lifecycle status for a generated plan."""

    CANDIDATE = "candidate"
    UNSUPPORTED = "unsupported"


class PlanStep(BaseModel):
    """One ordered action in a candidate plan."""

    model_config = ConfigDict(extra="forbid")

    step_number: int = Field(ge=1)
    action: str = Field(min_length=1)
    parameters: dict[str, str] = Field(default_factory=dict)


class Plan(BaseModel):
    """A candidate plan associated with the task it is intended to solve."""

    model_config = ConfigDict(extra="forbid")

    task: Task
    steps: list[PlanStep] = Field(default_factory=list)
    status: PlanStatus
