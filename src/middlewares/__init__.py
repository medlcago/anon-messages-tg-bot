from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from .context import ContextMiddleware
from .logging import LoggingMiddleware
from .translator import TranslatorMiddleware
from .user_registration import UserRegistrationMiddleware

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


def register_middlewares(dp: Dispatcher, session: AsyncSession) -> None:
    dp.message.outer_middleware(TranslatorMiddleware())
    dp.callback_query.outer_middleware(TranslatorMiddleware())

    dp.message.outer_middleware(ContextMiddleware(session=session))

    dp.callback_query.middleware(CallbackAnswerMiddleware(pre=False, text="OK"))

    dp.message.outer_middleware(LoggingMiddleware())
    dp.callback_query.outer_middleware(LoggingMiddleware())

    dp.message.middleware(UserRegistrationMiddleware())
