from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F, flags
from aiogram.filters import CommandStart

from filters import TelegramIDFilter
from keyboards.inline import main_keyboard, dialog_keyboard

if TYPE_CHECKING:
    from aiogram.types import Message, CallbackQuery
    from language.translator import LocalizedTranslator

command_start_router = Router(name="start")


@command_start_router.message(CommandStart(deep_link=True), TelegramIDFilter())
@flags.registration_flag
async def command_start_with_args(message: Message, telegram_id: str, translator: LocalizedTranslator):
    await message.answer_sticker(sticker="CAACAgIAAxkBAAICFWb4NomvtcuQlcNG_4tTAAFv6eCSTwACyyUAAlgGUEkFSsHeoT_mizYE")
    await message.answer(
        text=translator.get("start-deep-link-message"),
        reply_markup=dialog_keyboard(telegram_id=telegram_id),
        parse_mode="HTML"
    )


@command_start_router.message(CommandStart())
@flags.registration_flag
async def command_start(message: Message, translator: LocalizedTranslator):
    await message.answer(
        text=translator.get("start-message"),
        reply_markup=main_keyboard()
    )


@command_start_router.callback_query(F.data == "main_menu")
async def command_start_callback(callback: CallbackQuery, translator: LocalizedTranslator):
    await callback.message.edit_text(
        text=translator.get("start-message"),
        reply_markup=main_keyboard()
    )
