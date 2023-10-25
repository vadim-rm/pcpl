from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.keyboards.reply import bowl_button_text
from tgbot.utils.process_result import process_result


async def bowl(message: types.Message):
    result = await message.answer_dice('🎳')
    await process_result(message, result.dice.value)


def register_soccer(dp: Dispatcher):
    dp.register_message_handler(bowl, Text(equals=bowl_button_text))
