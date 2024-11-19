from decimal import Decimal

from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.contrainer.init import init_container
from infrastructure.repositories.base import BaseExchangeRatesRepository
from punq import Container

from application.bot.handlers.converters import convert_exchange_rate_entity_to_string
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from domain.value_objects.currency_code import Code
from domain.value_objects.rate import Rate


router = Router()


@router.message(Command(commands=["exchange_rate_update"]))
async def exchange_rate_update_handler(
    message: types.Message,
):
    args = message.text[len("/exchange_rate_update "):].split("|")  # Разделяем по |
    if len(args) != 3:
        await message.answer(
            "Пожалуйста, используйте формат:\n"
            "/exchange_rate_update &lt;Базовая валюта&gt | &lt;Целевая валюта&gt | &lt;Курс&gt\n"
            "Пример: /exchange_rate_update USD | EUR | 0.5",
        )
        return

    container: Container = init_container()
    exchange_rates_repository: BaseExchangeRatesRepository = container.resolve(
        BaseExchangeRatesRepository,
    )

    try:
        base_code = Code(args[0].strip().upper())
        target_code = Code(args[1].strip().upper())
        rate = Rate(Decimal(args[2].strip()))

        exchange_rate: ExchangeRate = (
            await exchange_rates_repository.update_exchange_rate(
                base_code.as_generic_type(),
                target_code.as_generic_type(),
                rate,
            )
        )

        if exchange_rate:
            exchange_rate_str: str = convert_exchange_rate_entity_to_string(
                exchange_rate,
            )
            await message.answer(f"<b>Обменник обнавлен</b>\n{exchange_rate_str}")
        else:
            await message.answer("Не удалось обновить валюту.")
    except ApplicationException as exception:
        await message.answer(exception.message)
