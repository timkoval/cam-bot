import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from datetime import datetime, timedelta
from setup import bot, CHAT_ID
from hachiko.hachiko import AIOEventHandler
from asyncio import sleep

EVENT_TYPE_OPENED = "opened"

class FilesHandler(AIOEventHandler):
    def __init__(self, loop=None):
        super().__init__(loop)
        self._method_map[EVENT_TYPE_OPENED] = self.on_opened

    async def on_any_event(self, event):
        ...

    async def on_created(self, event):
        logging.info(event.src_path.strip())
        await sleep(65)
        await bot.send_video(CHAT_ID, open(event.src_path, "rb"))

    async def on_opened(self, event):
        ...