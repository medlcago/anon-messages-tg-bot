from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F
from aiogram.utils.deep_linking import create_start_link

from keyboards.inline import back_main_menu_keyboard

if TYPE_CHECKING:
    from aiogram.types import CallbackQuery
    from aiogram import Bot
    from language.translator import LocalizedTranslator

profile_router = Router(name="profile")


@profile_router.callback_query(F.data == "profile")
async def profile_callback(callback: CallbackQuery, bot: Bot, translator: LocalizedTranslator):
    link = await create_start_link(bot, str(callback.from_user.id), encode=True)
    await callback.message.edit_text(
        text=translator.get("user-profile-message", user_id=callback.from_user.id, link=link),
        reply_markup=back_main_menu_keyboard(),
        parse_mode="HTML",
    )
