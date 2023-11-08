from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import CommandStart, Command

from setting import TOKEN
from core.handlers.basic import get_start, get_photo, say_hi, echo, help
from core.handlers.corses import get_dollar, get_euro, get_bitcoin, get_ether
from core.handlers.pizza import get_menu_pizza
from core.filters.fileters import MyFilter
from core.utils.commands import get_commands
from core.handlers.pay import order, pre_check, succsess_pay

import asyncio
import logging


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    await get_commands(bot)

    dp.message.register(get_start, CommandStart())
    dp.message.register(get_photo, F.photo)

    dp.message.register(order, Command(commands="pay"))
    dp.pre_checkout_query.register(pre_check)
    dp.message.register(succsess_pay, F.content_type == ContentType.SUCCESSFUL_PAYMENT)

    dp.message.register(say_hi, MyFilter('Hi'))
    dp.message.register(get_dollar, F.text == '$')
    dp.message.register(get_dollar, MyFilter('Dollar'))
    dp.message.register(get_euro, MyFilter('Euro'))
    dp.message.register(get_bitcoin, MyFilter('Bitcoin'))
    dp.message.register(get_ether, MyFilter('Ether'))
    dp.message.register(get_menu_pizza, F.text == "Pizza")
    dp.message.register(help, MyFilter('Help'))
    dp.message.register(echo)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())

