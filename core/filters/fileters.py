from aiogram.filters import Filter


class MyFilter(Filter):

    def __init__(self, symbol):
        self.symbol = symbol

    async def __call__(self, message):
        if self.symbol.lower() in message.text.lower():
            return True
        return False