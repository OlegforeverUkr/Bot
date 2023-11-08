import logging

from aiogram import Bot
from aiogram.types import Message
from core.keyboards.menu import select_menu



async def get_start(message: Message):
    logging.info(f"{message.from_user.first_name}")
    await message.answer(f"Привет {message.from_user.first_name}, рад тебя видеть тут!",
                         reply_markup=select_menu)


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Прикольная картинка, {message.from_user.first_name}, примо как ты!!")


async def say_hi(message: Message, bot: Bot):
    await message.answer(f"И тебе привет!!!")


async def help(message: Message, bot: Bot):
    await message.answer(f"Привет, {message.from_user.first_name}, это бот поможет узнать курс валют, жми на START")


async def echo(message: Message, bot: Bot):
    logging.info(f"{message.from_user.first_name}")
    await message.reply(f"{message.from_user.first_name}, я не знаю тках команд(((")
