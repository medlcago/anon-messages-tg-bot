from typing import Callable, Dict, Any, Awaitable, TYPE_CHECKING

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

if TYPE_CHECKING:
    from logging import Logger


class LoggingMiddleware(BaseMiddleware):
    def __init__(self, logger: "Logger"):
        self.logger = logger

    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any],
    ) -> Any:
        full_name = event.from_user.full_name
        user_id = event.from_user.id
        username = event.from_user.username
        text, chat_id = self._extract_text_and_chat_id(event)

        self.logger.info(f"{full_name}[{user_id}({username})] --- {text} [chat_id = {chat_id}]")

        return await handler(event, data)

    @staticmethod
    def _extract_text_and_chat_id(event):
        if isinstance(event, Message):
            text = event.text if event.text else event.content_type
            chat_id = event.chat.id
        else:
            text = event.data
            chat_id = event.message.chat.id
        return text, chat_id
