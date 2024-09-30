from __future__ import annotations

from typing import Any, TYPE_CHECKING

from aiogram.filters import Filter

from core.exceptions import InvalidPayloadException, SelfMessageAttemptException
from utils.payload import decode_payload

if TYPE_CHECKING:
    from aiogram.types import Message, User
    from aiogram.filters import CommandObject
    from services import ServiceContainer


class TelegramIDFilter(Filter):
    async def __call__(
            self,
            message: Message,
            event_from_user: User,
            command: CommandObject,
            service: ServiceContainer
    ) -> dict[str, Any]:
        telegram_id = decode_payload(command.args)
        if not telegram_id:
            raise InvalidPayloadException

        if telegram_id == str(event_from_user.id):
            raise SelfMessageAttemptException

        user = await service.user_service.get_user(telegram_id=telegram_id)
        if not user:
            raise InvalidPayloadException
        return {
            "telegram_id": telegram_id,
        }
