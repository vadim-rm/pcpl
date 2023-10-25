from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.keyboards.reply import dart_button_text
from tgbot.utils.process_result import process_result


async def dart(message: types.Message):
    result = await message.answer_dice('🎯')
    await process_result(message, result.dice.value)


def register_dart(dp: Dispatcher):
    dp.register_message_handler(dart, Text(equals=dart_button_text))
