from pathlib import Path

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=BASE_DIR / ".env"
    )

    bot_token: SecretStr = Field(alias="BOT_TOKEN")
