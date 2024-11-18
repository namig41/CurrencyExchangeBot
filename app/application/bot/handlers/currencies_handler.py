from typing import Iterable

from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.contrainer.init import init_container
from infrastructure.repositories.base import BaseCurrenciesRepository
from punq import Container

from application.bot.handlers.converters import convert_currencies_entity_to_string
from domain.entities.currency import Currency
from domain.exceptions.base import ApplicationException


router = Router()


@router.message(Command(commands=["currencies"]))
async def currencies_handler(
    message: types.Message,
):
    container: Container = init_container()
    currencies_repository: BaseCurrenciesRepository = container.resolve(
        BaseCurrenciesRepository,
    )
    try:
        currencies: Iterable[Currency] = await currencies_repository.get_currencies()

        if currencies:
            currencies_str: str = convert_currencies_entity_to_string(currencies)
            await message.answer(f"<b>Список валют</b>\n{currencies_str}")
        else:
            await message.answer("Список валют пустой.")
    except ApplicationException as exception:
        await message.answer(exception.message)
