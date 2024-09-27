from aiogram import Dispatcher

from .any_message import any_message_router
from .users import users_router


def register_routes(dp: Dispatcher) -> None:
    dp.include_router(users_router)
    dp.include_router(any_message_router)
