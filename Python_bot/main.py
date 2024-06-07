import asyncio
import sys
import logging
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from config import TOKEN
from handler.command import cmd_router
from handler.message import msg_router


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(cmd_router, msg_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream= sys.stdout)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")