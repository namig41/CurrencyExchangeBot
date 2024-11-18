from decimal import Decimal

from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command
from infrastructure.services.exchange import exchange_by_codes

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
        amount = Decimal(args[2].strip())

        exchange: dict = await exchange_by_codes(base_code, target_code, amount)

        if exchange:
            convertedAmount = float(exchange["convertedAmount"])
            await message.answer(f"<b>Сконвертированная сумма:</b> {convertedAmount}\n")
        else:
            await message.answer("Не удалось сконвертировать валюту.")
    except ApplicationException as exception:
        await message.answer(exception.message)
