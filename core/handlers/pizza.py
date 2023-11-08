from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto

import os

images_dir = r"C:\Users\Олег\PycharmProjects\Bot\core\handlers\pizza"


async def get_menu_pizza(message: Message, bot: Bot):
    media = []

    for image in os.listdir(path=images_dir):
        photo_file = FSInputFile(f"{images_dir}\{image}")
        name = image.split(".")[0]
        await bot.send_photo(chat_id=message.chat.id, photo=photo_file, caption=f"{name}")

