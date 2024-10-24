import asyncio
from aiogram import Bot, Dispatcher
from handlers import register_handlers
from database import create_db
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = 'token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

register_handlers(dp, bot)

async def on_startup():
    create_db()

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())