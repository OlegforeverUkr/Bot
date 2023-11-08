from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType



select_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Dollar"
        )
    ],
    [
        KeyboardButton(
            text="Euro"
        )
    ],
    [
        KeyboardButton(
            text="Bitcoin"
        )
    ],
    [
        KeyboardButton(
            text="Ethereum"
        )
    ],
    [
        KeyboardButton(
            text="Pizza"
        )
    ],
])