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
from domain.exceptions.base import ApplicationException
from domain.value_objects.currency_code import Code


router = Router()


@router.message(Command(commands=["currency_add"]))
async def currency_handler(
    message: types.Message,
):
    args = message.text[len("/currency_add "):].split("|")  # Разделяем по |
    if len(args) != 3:
        await message.answer(
            "Пожалуйста, используйте формат:\n"
            "/currency_add <Название валюты> | <Код валюты> | <Символ>\n"
            "Пример: /currency_add Azerbaijanian Manat | AZN | C",
        )
        return

    currency_name = args[0].strip()
    currency_code = args[1].strip().upper()
    currency_sign = args[2].strip()

    container: Container = init_container()
    currencies_repository: BaseCurrenciesRepository = container.resolve(
        BaseCurrenciesRepository,
    )

    try:
        currency: Currency = Currency(Code(currency_code), currency_name, currency_sign)
        currency: Currency = await currencies_repository.add_currency(currency)

        if currency:
            currency_str: str = convert_currency_entity_to_string(currency)
            await message.answer(f"<b>Валюта добавлена</b>\n{currency_str}")
        else:
            await message.answer("Не удалось добавить валюту.")
    except ApplicationException as exception:
        await message.answer(exception.message)
