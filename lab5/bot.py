import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.handlers.dart import register_dart
from tgbot.handlers.dice import register_dice
from tgbot.handlers.bowl import register_soccer
from tgbot.handlers.user import register_user

logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_user(dp)

    register_dice(dp)
    register_dart(dp)
    register_soccer(dp)


async def main():
    config = load_config()

    storage = MemoryStorage()
    bot = Bot(token=config.telegram.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
