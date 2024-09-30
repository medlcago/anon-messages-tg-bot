from aiogram import Router

from .about_bot import about_bot_router
from .cancel_action import cancel_action_router
from .cmd_start import command_start_router
from .profile import profile_router
from .start_dialog import start_dialog_router

users_router = Router(name="users")

users_router.include_router(cancel_action_router)
users_router.include_router(command_start_router)
users_router.include_router(start_dialog_router)
users_router.include_router(about_bot_router)
users_router.include_router(profile_router)
