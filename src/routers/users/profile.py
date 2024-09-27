from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.deep_linking import create_start_link

from core.text import USER_PROFILE
from keyboards.inline import back_main_menu_keyboard

if TYPE_CHECKING:
    from aiogram import Bot

profile_router = Router(name="profile")


@profile_router.callback_query(F.data == "profile")
async def profile_callback(callback: CallbackQuery, bot: Bot):
    link = await create_start_link(bot, str(callback.from_user.id), encode=True)
    msg = USER_PROFILE.format(
        user_id=callback.from_user.id,
        link=link
    )
    await callback.message.edit_text(
        text=msg,
        reply_markup=back_main_menu_keyboard(),
        parse_mode="HTML",
    )
