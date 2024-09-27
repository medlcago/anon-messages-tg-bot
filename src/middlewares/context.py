from __future__ import annotations

from typing import Callable, Dict, Any, Awaitable, TYPE_CHECKING

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from repo import UnitOfWork
from services import ServiceContainer

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class ContextMiddleware(BaseMiddleware):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any],
    ) -> Any:
        uow = UnitOfWork(session=self.session)

        data["service"] = ServiceContainer(uow=uow)
        data["session"] = self.session
        return await handler(event, data)
