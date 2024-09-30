from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F
from aiogram.exceptions import AiogramError
from aiogram.filters import ExceptionTypeFilter

from core.exceptions import BotException
from core.logger import logger
from keyboards.inline import action_close_keyboard

if TYPE_CHECKING:
    from aiogram.types import ErrorEvent, Message

errors_router = Router(name="errors")


@errors_router.error(ExceptionTypeFilter(BotException), F.update.message.as_("message"))
async def error_handler(event: ErrorEvent, message: Message):
    logger.info(f"{message.from_user.id}: {event.exception.__class__.__name__}")
    await message.answer(
        text=str(event.exception),
        reply_markup=action_close_keyboard(),
        parse_mode="HTML"
    )


@errors_router.error(ExceptionTypeFilter(AiogramError), F.update.message.as_("message"))
async def aiogram_error_handler(event: ErrorEvent, message: Message):
    logger.info(f"{message.from_user.id}: {event.exception.__class__.__name__}")
    await message.answer(
        text=str(event.exception),
        reply_markup=action_close_keyboard()
    )
