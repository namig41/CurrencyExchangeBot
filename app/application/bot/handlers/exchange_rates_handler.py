from typing import Iterable

from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.contrainer.init import init_container
from infrastructure.repositories.base import BaseExchangeRatesRepository
from punq import Container

from application.bot.handlers.converters import convert_exchange_rates_entity_to_string
from domain.entities.exchange_rate import ExchangeRate


router = Router()


@router.message(Command(commands=["exchange_rates"]))
async def currency_handler(
    message: types.Message,
):
    container: Container = init_container()
    exchange_rates_repository: BaseExchangeRatesRepository = container.resolve(
        BaseExchangeRatesRepository,
    )

    exchange_rates: Iterable[ExchangeRate] = (
        await exchange_rates_repository.get_exchange_rates()
    )

    if exchange_rates:
        exchange_rates_str = convert_exchange_rates_entity_to_string(exchange_rates)
        await message.answer(f"<b>Список всех обменников</b>\n{exchange_rates_str}")
    else:
        await message.answer("Не удалось получить обменник валют.")
