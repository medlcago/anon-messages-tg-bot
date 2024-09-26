from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from middlewares import register_middlewares
from routers import register_routes
from src.core.logger import logger
from src.core.settings import Settings


async def main():
    config = Settings()

    bot = Bot(
        token=config.bot_token.get_secret_value(),
        defaults=DefaultBotProperties(
            allow_sending_without_reply=True
        )
    )

    dp = Dispatcher()
    register_middlewares(dp, logger=logger)
    register_routes(dp)

    bot_info = await bot.get_me()
    logger.info(f"Bot started: {bot_info.full_name}[@{bot_info.username}]")
    await dp.start_polling(bot, close_bot_session=True, config=config)


if __name__ == '__main__':
    import asyncio

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info(f"Bot stopped")
