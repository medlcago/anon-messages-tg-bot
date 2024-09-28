from enum import StrEnum
from pathlib import Path

from pydantic import SecretStr, RedisDsn, field_validator, PostgresDsn
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class FSMMode(StrEnum):
    MEMORY = "memory"
    REDIS = "redis"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=BASE_DIR / ".env"
    )

    bot_token: SecretStr
    bot_name: str = "AnonBot"
    fsm_mode: FSMMode

    db_naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
    db_url: PostgresDsn
    redis_url: RedisDsn | None = None

    @field_validator("redis_url", mode="after")
    @classmethod
    def skip_validating_redis(cls, v: RedisDsn | None, info: ValidationInfo):
        if info.data.get("fsm_mode") == FSMMode.REDIS and v is None:
            err = 'FSM Mode is set to "Redis", but Redis URL is missing!'
            raise ValueError(err)
        return v


settings = Settings()
