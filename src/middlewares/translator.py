from typing import Callable, Any, Awaitable, Dict, cast

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from language.translator import Translator, LocalizedTranslator


class TranslatorMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        new_data = data.copy()
        translator: Translator = new_data["translator"]
        new_data["translator"] = cast(LocalizedTranslator, translator(language=event.from_user.language_code))
        return await handler(event, new_data)
