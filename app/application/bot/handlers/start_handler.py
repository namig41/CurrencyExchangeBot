from aiogram import (
    Router,
    types,
)
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я бот для обмена валют. Используй /help, чтобы узнать доступные команды.",
    )
