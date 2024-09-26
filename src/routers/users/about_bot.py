from typing import TYPE_CHECKING

from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.text import ABOUT_BOT
from keyboards.inline import back_main_menu_keyboard

if TYPE_CHECKING:
    from core.settings import Settings

about_bot_router = Router(name="about_bot")


@about_bot_router.callback_query(F.data == "about_bot")
async def about_bot_callback(callback: CallbackQuery, config: "Settings"):
    await callback.message.edit_text(
        text=ABOUT_BOT.format(name=config.bot_name),
        reply_markup=back_main_menu_keyboard(),
        parse_mode="HTML",
    )
