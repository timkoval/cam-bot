import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types.bot_command import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WATCH_DIR = os.getenv("WATCH_DIR")
VIDEO_DURATION = os.getenv("VIDEO_DURATION", default=31)

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=API_TOKEN, timeout=None)
dispatcher = Dispatcher(bot, storage=storage)
