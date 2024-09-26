from typing import TYPE_CHECKING

from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from .logging import LoggingMiddleware

if TYPE_CHECKING:
    from loguru import Logger


def register_middlewares(dp: Dispatcher, logger: "Logger") -> None:
    dp.callback_query.middleware(CallbackAnswerMiddleware(pre=False, text="OK"))

    dp.message.middleware(LoggingMiddleware(logger=logger))
    dp.callback_query.middleware(LoggingMiddleware(logger=logger))
