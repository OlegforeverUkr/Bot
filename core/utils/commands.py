from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def get_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Начало работы"
        ),
        BotCommand(
            command="help",
            description="Помощь"
        ),
        BotCommand(
            command="pay",
            description="Оплата"
        ),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
