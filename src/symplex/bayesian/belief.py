"""Simple probability belief state for later Bayesian implementations."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SimpleBeliefState(BaseModel):
    """Named probabilities without Bayesian-network inference."""

    model_config = ConfigDict(extra="forbid")

    probabilities: dict[str, float] = Field(default_factory=dict)

    @field_validator("probabilities")
    @classmethod
    def probabilities_must_be_valid(cls, values: dict[str, float]) -> dict[str, float]:
        """Require every stored value to be a probability in [0, 1]."""

        if any(not 0.0 <= probability <= 1.0 for probability in values.values()):
            raise ValueError("belief probabilities must be between 0 and 1")
        return values
