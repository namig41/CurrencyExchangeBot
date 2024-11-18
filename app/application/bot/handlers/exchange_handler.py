from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.services.exchange import exchange_by_codes

from application.bot.handlers.converters import convert_exchange_entity_to_string
from domain.entities.exchange import Exchange
from domain.exceptions.base import ApplicationException
from domain.value_objects.currency_code import Code


router = Router()


@router.message(Command(commands=["exchange"]))
async def exchange_rate_add_handler(
    message: types.Message,
):
    args = message.text[len("/exchange "):].split("|")  # Разделяем по |
    if len(args) != 3:
        await message.answer(
            "Пожалуйста, используйте формат:\n"
            "/exchange_rate_add &lt;Базовая валюта&gt | &lt;Целевая валюта&gt | &lt;Средства&gt\n"
            "Пример: /exchange USD | EUR | 10",
        )
        return

    try:
        base_code = Code(args[0].strip().upper())
        target_code = Code(args[1].strip().upper())
        amount = float(args[2].strip())

        exchange: Exchange = await exchange_by_codes(
            base_code, target_code, amount,
        )

        if exchange:
            exchange_str = convert_exchange_entity_to_string(exchange)
            await message.answer(f"<b>Расчёт перевода</b>\n{exchange_str}")
        else:
            await message.answer("Не удалось сконвертировать валюту.")
    except ApplicationException as exception:
        await message.answer(exception.message)
