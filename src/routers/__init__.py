from aiogram import Dispatcher

from .users import users_router


def register_routes(dp: Dispatcher) -> None:
    dp.include_router(users_router)
