import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from datetime import datetime, timedelta
from setup import bot, CHAT_ID
from hachiko.hachiko import AIOEventHandler


class FilesHandler(AIOEventHandler):
    async def on_any_event(self, event):
        logging.info(event.event_type, event.src_path)

    async def on_created(self, event):
        logging.info("on_created", event.src_path)
        logging.info(event.src_path.strip())
        await bot.send_video(CHAT_ID, open(event.src_path, "rb"))
