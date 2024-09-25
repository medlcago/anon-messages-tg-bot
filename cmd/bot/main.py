from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from src.core.logger import logger
from src.core.settings import Settings
from routers import register_routes


async def main():
    config = Settings()

    bot = Bot(
        token=config.bot_token.get_secret_value(),
        defaults=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            allow_sending_without_reply=True,
        )
    )

    dp = Dispatcher()
    register_routes(dp)

    bot_info = await bot.get_me()
    logger.info(f"Bot started: {bot_info.full_name}[@{bot_info.username}]")
    await dp.start_polling(bot, close_bot_session=True, config=config, logger=logger)


if __name__ == '__main__':
    import asyncio

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info(f"Bot stopped")
