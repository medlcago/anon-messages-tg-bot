from __future__ import annotations

from typing import Any, TYPE_CHECKING

from aiogram.filters import Filter

from core.exceptions import InvalidPayloadException, SelfMessageAttemptException
from utils.payload import decode_payload

if TYPE_CHECKING:
    from aiogram.types import Message, User
    from aiogram.filters import CommandObject
    from services import ServiceContainer
    from language.translator import LocalizedTranslator


class TelegramIDFilter(Filter):
    async def __call__(
            self,
            message: Message,
            event_from_user: User,
            command: CommandObject,
            service: ServiceContainer,
            translator: LocalizedTranslator
    ) -> dict[str, Any]:
        telegram_id = decode_payload(command.args)
        if not telegram_id:
            raise InvalidPayloadException(
                message=translator.get("invalid-link-error")
            )

        if telegram_id == str(event_from_user.id):
            raise SelfMessageAttemptException(
                message=translator.get("self-message-attempt-error")
            )

        user = await service.user_service.get_user(telegram_id=telegram_id)
        if not user:
            raise InvalidPayloadException(
                message=translator.get("invalid-link-error")
            )
        return {
            "telegram_id": telegram_id,
        }
