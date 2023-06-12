"""Main project module."""
import logging
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text as TextFilter

import keyboard as kb


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def greeting(message):
    """Greeting bot message."""
    await message.answer("Первое сообщение", reply_markup=kb.MainMenuMarkup)


@dp.message_handler(TextFilter(equals=kb.InformationBlock))
async def send_information_block(message):
    """Relocate user to unformaion block."""
    await message.answer(
        "Выберите интересующую Вас тему",
    )


def main():
    """Run bot."""
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
