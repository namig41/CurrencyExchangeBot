from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command


router = Router()


@router.message(Command(commands=["help"]))
async def help_handler(message: types.Message):
    await message.answer(
        "/start - Приветствие\n"
        "/currency &lt;код валюты&gt - Узнать информацию о валюте\n"
        "/currency_add &lt;Название валюты&gt | &lt;Код валюты&gt | &lt;Символ&gt - Добавить новую валюту\n"
        "/currencies - Список всех валют\n"
        "/exchange_rate &lt;код базовой валюты&gt &lt;код целевой валюты&gt - Узнать информацию о обменнике\n"
        "/exchange_rate_add &lt;Базовая валюта&gt | &lt;Целевая валюта&gt | &lt;Курс&gt - Добавить новый обменник\n"
        "/exchange_rates - Список всех обменников\n",
        "/exchange &lt;Базовая валюта&gt | &lt;Целевая валюта&gt | &lt;Средства&gt - Перевод с одной валюты в другую\n",
    )
