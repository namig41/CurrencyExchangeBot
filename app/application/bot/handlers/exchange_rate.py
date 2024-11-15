from aiogram import (
    Router,
    types,
)
from app.infrastructure.repositories.api_repostiory import CurrenciesAPIRepository


router = Router()


@router.message(commands=["exchange"])
async def rate_handler(message: types.Message, repo: CurrenciesAPIRepository):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите код валюты, например: /rate USD")
        return

    currency = args[1].upper()
    rate = await repo.get_currency_rate(currency)
    if rate:
        await message.answer(f"Текущий курс {currency}: {rate}")
    else:
        await message.answer("Не удалось получить курс валюты. Проверьте код валюты.")
