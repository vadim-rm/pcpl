from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.keyboards.reply import dice_button_text
from tgbot.utils.process_result import process_result


async def dice(message: types.Message):
    result = await message.answer_dice('🎲')
    await process_result(message, result.dice.value)


def register_dice(dp: Dispatcher):
    dp.register_message_handler(dice, Text(equals=dice_button_text))
