from aiogram import Bot
from aiogram.types import BotCommand

commands_en = [
    BotCommand(
        command="start",
        description="Start the bot",
    ),
]

commands_ru = [
    BotCommand(
        command="start",
        description="Запустить бота",
    ),
]


async def set_bot_commands(bot: Bot) -> None:
    await bot.set_my_commands(
        commands=commands_en
    )

    await bot.set_my_commands(
        commands=commands_ru,
        language_code="ru"
    )
