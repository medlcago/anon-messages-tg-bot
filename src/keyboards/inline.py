from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
