import asyncio
from aiogram import executor
from setup import dispatcher, WATCH_DIR
from handlers import FilesHandler
from hachiko.hachiko import AIOWatchdog


async def watch_fs(watch_dir):
    event_handler = FilesHandler()
    observer = AIOWatchdog(watch_dir, event_handler=event_handler)
    observer.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(watch_fs(WATCH_DIR))
    executor.start_polling(dispatcher, skip_updates=True)
