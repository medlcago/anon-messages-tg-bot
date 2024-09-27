from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F, flags
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery

from core.text import COMMAND_START
from keyboards.inline import main_keyboard
from utils.payload import decode_payload

if TYPE_CHECKING:
    from services import ServiceContainer

command_start_router = Router(name="start")


@command_start_router.message(CommandStart(deep_link=True))
@flags.registration_flag
async def command_start_with_args(message: Message, command: CommandObject, service: ServiceContainer):
    telegram_id = decode_payload(command.args)
    if telegram_id is None:
        return await message.answer(
            text=COMMAND_START,
            reply_markup=main_keyboard()
        )

    user = await service.user_service.get_user(telegram_id=telegram_id)
    if user is None:
        return await message.answer(
            text=COMMAND_START,
            reply_markup=main_keyboard()
        )
    await message.answer(f"Your payload: {telegram_id}")


@command_start_router.message(CommandStart())
@flags.registration_flag
async def command_start(message: Message):
    await message.answer(
        text=COMMAND_START,
        reply_markup=main_keyboard()
    )


@command_start_router.callback_query(F.data == "main_menu")
async def command_start_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=COMMAND_START,
        reply_markup=main_keyboard()
    )
