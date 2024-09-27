from __future__ import annotations

from typing import Callable, Dict, Any, Awaitable, TYPE_CHECKING

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from cachetools import TTLCache

from core.logger import logger

if TYPE_CHECKING:
    from services import Service


class UserRegistrationMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache = TTLCache(maxsize=10_000, ttl=900)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        registration_flag: bool = get_flag(data, "registration_flag")
        if not registration_flag:
            return await handler(event, data)

        cache_key = f"registration_flag:{event.from_user.id}"
        if self.cache.get(cache_key):
            return await handler(event, data)

        self.cache[cache_key] = event.from_user.id

        service: Service = data.get("service")
        user = await service.user_service.get_user(telegram_id=event.from_user.id)
        if user:
            return await handler(event, data)

        new_user = await service.user_service.register_user(tg_user=event.from_user)
        logger.info(f"Новый пользователь: {new_user.telegram_id=}")
        return await handler(event, data)
