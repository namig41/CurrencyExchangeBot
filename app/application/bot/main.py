from aiohttp import web

from application.bot.bot import telegram_factory
from settings import config


async def init_app() -> web.Application:
    app = web.Application()

    app.router.add_route(
        "*",
        config.TELEGRAM_WEBHOOK_PATH,
        await telegram_factory(),
        name="tg_webhook_handler",
    )

    return app


if __name__ == "__main__":
    web.run_app(init_app())
