from typing import Iterable

from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.repositories.base import BaseCurrenciesRepository

from application.bot.handlers.converters import convert_currencies_entity_to_string
from domain.entities.currency import Currency


router = Router()


@router.message(Command(commands=["currencies"]))
async def currency_handler(
    message: types.Message, currenies_repository: BaseCurrenciesRepository,
):
    currencies: Iterable[Currency] = await currenies_repository.get_currencies()

    if currencies:
        currencies_str = convert_currencies_entity_to_string(currencies)
        await message.answer(f"<b>Список валют</b>\n{currencies_str}")
    else:
        await message.answer("Список валют пустой.")
