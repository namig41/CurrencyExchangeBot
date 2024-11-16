from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command


router = Router()


@router.message(Command(commands=["help"]))
async def help_handler(message: types.Message):
    await message.answer(
        "/currency &lt;код валюты&gt - Узнать информацию о валюте\n"
        "/currencies - Список всех валют\n"
        "/exchange_rate &lt;код базовой валюты&gt &lt;код целевой валюты&gt - Узнать информацию о обменнике\n"
        "/exchange_rates - Список всех обменников\n",
    )
