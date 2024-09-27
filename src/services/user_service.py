from __future__ import annotations

from abc import abstractmethod, ABC
from typing import TYPE_CHECKING

from pydantic import BaseModel

from models import User
from repo.unitofwork import UnitOfWork

if TYPE_CHECKING:
    from aiogram.types import User as TgUser


class IUserService(ABC):
    @abstractmethod
    async def register_user(self, tg_user: TgUser) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, telegram_id: str) -> User | None:
        raise NotImplementedError


class UserService(IUserService, BaseModel):
    uow: UnitOfWork

    async def register_user(self, tg_user: TgUser) -> User:
        async with self.uow as session:
            user = User(
                telegram_id=str(tg_user.id),
                username=tg_user.username,
                full_name=tg_user.full_name,
            )
            new_user = await session.user_repo.create_user(user=user)
            return new_user

    async def get_user(self, telegram_id: str) -> User | None:
        async with self.uow as session:
            user = await session.user_repo.get_user(telegram_id=telegram_id)
            return user
