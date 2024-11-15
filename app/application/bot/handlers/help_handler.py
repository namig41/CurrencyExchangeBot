from aiogram import (
    Router,
    types,
)
from aiogram.filters import Command


router = Router()


@router.message(Command(commands=["help"]))
async def help_handler(message: types.Message):
    await message.answer(
        "/currency \\<код валюты\\> - Узнать информацию о валюте\n"
        "/currencies - Список всех валют\n",
    )
