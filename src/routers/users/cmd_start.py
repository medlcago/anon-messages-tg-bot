from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F, flags
from aiogram.filters import CommandStart

from core.text import COMMAND_START, START_DIALOG
from filters import TelegramIDFilter
from keyboards.inline import main_keyboard, dialog_keyboard

if TYPE_CHECKING:
    from aiogram.types import Message, CallbackQuery

command_start_router = Router(name="start")


@command_start_router.message(CommandStart(deep_link=True), TelegramIDFilter())
@flags.registration_flag
async def command_start_with_args(message: Message, telegram_id: str):
    await message.answer_sticker(sticker="CAACAgIAAxkBAAICFWb4NomvtcuQlcNG_4tTAAFv6eCSTwACyyUAAlgGUEkFSsHeoT_mizYE")
    await message.answer(
        text=START_DIALOG,
        reply_markup=dialog_keyboard(telegram_id=telegram_id),
        parse_mode="HTML"
    )


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
