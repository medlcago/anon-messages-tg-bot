from aiogram import Router

from .cmd_start import command_start_router

users_router = Router(name="users")
users_router.include_router(command_start_router)
