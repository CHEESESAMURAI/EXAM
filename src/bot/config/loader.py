from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.config.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
storage = JSONStorage(f'{Path.cwd()}/{"fsm_data.json"}')
dp = Dispatcher(bot, storage=storage)
user_data = {}
