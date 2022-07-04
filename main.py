"""Main project module."""
import logging
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def greeting(message):
    """Greeting bot message."""
    await message.answer("Первое сообщение")


def main():
    """Run bot."""
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
