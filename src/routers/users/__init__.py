from aiogram import Router

from .cmd_start import command_start_router
from .about_bot import about_bot_router
from .profile import profile_router

users_router = Router(name="users")

users_router.include_router(command_start_router)
users_router.include_router(about_bot_router)
users_router.include_router(profile_router)
