from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.contrainer.init import init_container
from infrastructure.repositories.base import BaseCurrenciesRepository
from punq import Container

from application.bot.handlers.converters import convert_currency_entity_to_string
from domain.entities.currency import Currency
from domain.value_objects.currency_code import Code


router = Router()


@router.message(Command(commands=["currency_add"]))
async def currency_handler(
    message: types.Message,
):
    args = message.text.split()
    if len(args) != 4:
        await message.answer(
            "Пожалуйста, укажите название валюты, код валюты, символ валюты."
            "\nнапример: /currency_add Euro EUR €",
        )
        return

    container: Container = init_container()
    currencies_repository: BaseCurrenciesRepository = container.resolve(
        BaseCurrenciesRepository,
    )

    currency_name = args[1]
    currency_code = args[2].upper()
    currency_sign = args[3]
    currency: Currency = Currency(Code(currency_code), currency_name, currency_sign)

    currency: Currency = await currencies_repository.add_currency(currency)
    if currency:
        currency_str: str = convert_currency_entity_to_string(currency)
        await message.answer(f"<b>Валюта добавлена</b>\n{currency_str}")
    else:
        await message.answer("Не удалось добавить валюту.")
