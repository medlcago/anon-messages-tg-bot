from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline import back_main_menu_keyboard

if TYPE_CHECKING:
    from core.settings import Settings
    from language.translator import LocalizedTranslator

about_bot_router = Router(name="about_bot")


@about_bot_router.callback_query(F.data == "about_bot")
async def about_bot_callback(callback: CallbackQuery, config: Settings, translator: LocalizedTranslator):
    await callback.message.edit_text(
        text=translator.get("about-bot-message", name=config.bot_name),
        reply_markup=back_main_menu_keyboard(),
        parse_mode="HTML",
    )
