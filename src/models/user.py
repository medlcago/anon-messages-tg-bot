from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import (
    Base,
    UUIDMixin,
    TableNameMixin,
    TimestampMixin
)


class User(UUIDMixin, TableNameMixin, TimestampMixin, Base):
    telegram_id: Mapped[str] = mapped_column(String(20), unique=True)
    username: Mapped[str | None] = mapped_column(String(32))
    full_name: Mapped[str | None] = mapped_column(String(64))
    is_active: Mapped[bool] = mapped_column(default=True, server_default="1")
    is_admin: Mapped[bool] = mapped_column(default=False, server_default="0")
