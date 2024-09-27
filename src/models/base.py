import uuid
from datetime import datetime

from sqlalchemy import func, text, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from core.settings import settings


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.db_naming_convention
    )

    def __repr__(self):
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = ((k, getattr(self, k)) for k in self.__mapper__.columns.keys())
        sattrs = ", ".join(f"{key}={value!r}" for key, value in attrs)
        return f"{package}.{class_}({sattrs})"


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class UUIDMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()")
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
        server_onupdate=func.now()
    )
