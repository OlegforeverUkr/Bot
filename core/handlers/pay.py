from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка через телеграмм",
        description="Пробная оплата через ТГ Бота",
        payload="Внутренняя инфа для статистики или тд...",
        provider_token="1661751239:TEST:zVXH-XmPy-igQo-CcZu",
        currency="UAH",
        prices=[
            LabeledPrice(
                label="Lable product",
                amount=10000
            ),
            LabeledPrice(
                label="NDS",
                amount=2000
            ),
            LabeledPrice(
                label='Bonus',
                amount=1000
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        provider_data=None,
        photo_url="https://img.freepik.com/free-photo/cat-warriors-with-burning-eyes-generative-ai_8829-2909.jpg?size=626&ext=jpg&ga=GA1.1.386372595.1698364800&semt=sph",
        photo_size=100,
        photo_width=417,
        photo_height=626,
        need_name=True,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,  # Меняется ли адрес доставки
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,  # Зависит ли конечгая цена от способа доставки
        disable_notification=True,  # Доставка сообщения без звука
        protect_content=False,
        reply_to_message_id=False,  # Ответить на сообщение
        allow_sending_without_reply=True,
        reply_markup=None,  # Отправить еще одну клавиатуру(1м должно быть ОПЛАТИТЬ)
        request_timeout=30
    )


async def pre_check(pre_check_qwery: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_check_qwery.id, ok=True)


async def succsess_pay(message: Message):
    answ = f"{message.from_user.first_name}, спасибо за оплату!"
    await message.answer(answ)
