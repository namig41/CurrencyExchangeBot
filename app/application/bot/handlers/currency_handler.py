from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.repositories.base import BaseCurrenciesRepository

from application.bot.handlers.converters import convert_currencies_entity_to_string


router = Router()


@router.message(Command(commands=["currency"]))
async def currency_handler(
    message: types.Message, currensies_repository: BaseCurrenciesRepository,
):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите код валюты, например: /currency USD")
        return

    currency_code = args[1].upper()
    currency = await currensies_repository.get_currency_by_code(currency_code)
    if currency:
        currency_str = convert_currencies_entity_to_string(currency)
        await message.answer(f"<b>Информация о валюте</b>\n{currency_str}")
    else:
        await message.answer("Не удалось получить курс валюты. Проверьте код валюты.")
