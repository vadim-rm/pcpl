from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.reply import menu_keyboard


async def user_start(message: Message):
    await message.reply(
        "Привет! Выбери что хочешь сделать с помощью меню",
        reply_markup=menu_keyboard(),
    )


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
