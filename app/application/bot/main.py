import asyncio
import logging

from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from application.bot.handlers import (
    currencies_handler,
    currency_handler,
    help_handler,
    start_handler,
)
from settings.config import config


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Запуск процесса поллинга новых апдейтов
async def main():
    bot = Bot(
        token=config.TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()
    dp.include_router(start_handler.router)
    dp.include_router(help_handler.router)
    dp.include_router(currency_handler.router)
    dp.include_router(currencies_handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
