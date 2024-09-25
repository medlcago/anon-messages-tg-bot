from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

if TYPE_CHECKING:
    from loguru import Logger

command_start_router = Router(name="start")


@command_start_router.message(CommandStart())
async def cmd_start(message: Message, logger: "Logger"):
    logger.info(f"{message.from_user.full_name} started the bot")
    await message.answer(
        text="🤚"
    )
