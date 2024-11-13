from aiogram import (
    Bot,
    Dispatcher,
)

from application.bot.view import TelegramWebhookView
from settings import config


def add_handlers(dispatcher: Dispatcher) -> None:
    ...


async def telegram_factory() -> TelegramWebhookView:
    bot = Bot(token=config.TELEGRAM_TOKEN)

    await bot.set_webhook(config.TELEGRAM_WEB_HOOK)

    dispatcher = Dispatcher()
    add_handlers(dispatcher)

    return TelegramWebhookView(dispatcher=dispatcher, bot=bot)
