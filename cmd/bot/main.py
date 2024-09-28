from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from core.db import DatabaseHelper
from core.logger import logger
from core.settings import settings
from middlewares import register_middlewares
from routers import register_routes


async def on_startup(bot: Bot):
    bot_info = await bot.get_me()
    logger.info(f"Bot started: {bot_info.full_name}[@{bot_info.username}]")


async def main():
    db_helper = DatabaseHelper(
        url=str(settings.db_url)
    )

    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        defaults=DefaultBotProperties(
            allow_sending_without_reply=True
        )
    )

    if settings.fsm_mode == "redis":
        storage = RedisStorage.from_url(
            url=str(settings.redis_url),
            connection_kwargs={"decode_responses": True}
        )
    else:
        storage = MemoryStorage()

    dp = Dispatcher(storage=storage)
    dp.startup.register(on_startup)
    register_middlewares(dp, session=db_helper.session)
    register_routes(dp)
    await dp.start_polling(bot, close_bot_session=True, config=settings)


if __name__ == '__main__':
    import asyncio

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
