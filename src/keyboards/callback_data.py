from aiogram.filters.callback_data import CallbackData


class DialogCallback(CallbackData, prefix="dialog"):
    telegram_id: str
