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


router = Router()


@router.message(Command(commands=["exchange_rate"]))
async def currency_handler(
    message: types.Message,
):
    args = message.text.split()
    if len(args) != 3:
        await message.answer(
            "Пожалуйста, укажите код базовой валюты валюты и целевой, например: /exchange_rate USD EUR",
        )
        return

    container: Container = init_container()
    exchange_rates_repository: BaseExchangeRatesRepository = container.resolve(
        BaseExchangeRatesRepository,
    )

    base_code = args[1].upper()
    target_code = args[2].upper()
    exchange_rate: ExchangeRate = (
        await exchange_rates_repository.get_exchange_rate_by_codes(
            base_code=base_code, target_code=target_code,
        )
    )

    if exchange_rate:
        currency_str = convert_exchange_rate_entity_to_string(exchange_rate)
        await message.answer(f"<b>Информация о обменнике</b>\n{currency_str}")
    else:
        await message.answer("Не удалось получить обменник. Проверьте коды валют.")
