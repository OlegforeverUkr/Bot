from core.courses.find_cours import find_cripto, find_curses
from aiogram.types import Message
from aiogram import Bot


async def get_dollar(message: Message, bot: Bot):
    dollar = find_curses()[:2]
    await message.answer(f"Курс на доллар нынче такой - {dollar[0]}  {dollar[1]}")


async def get_euro(message: Message, bot: Bot):
    euro = find_curses()[2:]
    await message.answer(f"Курс на евро нынче такой - {euro[0]}  {euro[1]}")


async def get_bitcoin(message: Message, bot: Bot):
    bitcoin = find_cripto()[0]
    await message.answer(f"Курс битка - {bitcoin}")


async def get_ether(message: Message, bot: Bot):
    ether = find_cripto()[1]
    await message.answer(f"Курс ефира - {ether}")
