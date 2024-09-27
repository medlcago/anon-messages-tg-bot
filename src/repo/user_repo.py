from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select

from models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: User) -> User:
        self.session.add(user)
        await self.session.flush([user])
        return user

    async def get_user(self, telegram_id: str) -> User | None:
        stmt = select(User).filter_by(telegram_id=telegram_id)
        user = await self.session.scalar(stmt)
        return user
