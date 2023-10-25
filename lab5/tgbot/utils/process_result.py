import asyncio

from aiogram.types import Message


async def process_result(message: Message, value: int):
    if value == 6:
        await asyncio.sleep(2)
        await message.answer("Ты выиграл!")
