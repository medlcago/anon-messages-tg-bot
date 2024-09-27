from __future__ import annotations

from typing import TYPE_CHECKING

from models import User

if TYPE_CHECKING:
    from repo.unitofwork import UnitOfWork
    from aiogram.types import User as TgUser


class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def register_user(self, tg_user: TgUser) -> User:
        async with self.uow as session:
            user = User(
                telegram_id=str(tg_user.id),
                username=tg_user.username,
                full_name=tg_user.full_name,
            )
            new_user = await session.user_repo.create_user(user=user)
            return new_user

    async def get_user(self, telegram_id: int) -> User | None:
        async with self.uow as session:
            user = await session.user_repo.get_user(telegram_id=str(telegram_id))
            return user
