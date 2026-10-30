"""Environment-backed application configuration."""

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Optional local settings; no external service is required."""

    openai_api_key: str | None
    log_level: str


@lru_cache
def get_settings() -> Settings:
    """Return the cached settings loaded from the environment and `.env`."""

    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY") or None,
        log_level=os.getenv("SYMPLEX_LOG_LEVEL", "INFO"),
    )
