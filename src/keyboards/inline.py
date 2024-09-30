from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data import DialogCallback


def main_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="💼Профиль", callback_data="profile")
        ],
        [
            InlineKeyboardButton(text="❓О боте", callback_data="about_bot")
        ]
    ])
    return keyboard


def back_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
        ]
    ])
    return keyboard


def action_close_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Закрыть ", callback_data="close")
        ]
    ])
    return keyboard


def dialog_keyboard(telegram_id: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Начать диалог",
                callback_data=DialogCallback(telegram_id=telegram_id).pack()
            )
        ]
    ])
    return keyboard
