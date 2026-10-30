"""Task and action data structures."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Action(BaseModel):
    """An action schema with symbolic parameters, preconditions, and effects."""

    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    parameters: dict[str, str] = Field(default_factory=dict)
    preconditions: list[str] = Field(default_factory=list)
    effects: list[str] = Field(default_factory=list)


class Task(BaseModel):
    """A normalized task representation shared across system modules."""

    model_config = ConfigDict(extra="forbid")

    natural_language_task: str = Field(min_length=1)
    domain: str = Field(min_length=1)
    goals: list[str] = Field(default_factory=list)
    initial_state: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    supported: bool = True
    unsupported_reason: str | None = None

    @field_validator("natural_language_task")
    @classmethod
    def task_must_not_be_blank(cls, value: str) -> str:
        """Reject whitespace-only natural language input."""

        if not value.strip():
            raise ValueError("natural_language_task must not be blank")
        return value
