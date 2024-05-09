import asyncio
import logging
from aiogram import Bot
from config import bot, dp, database
from handlers.menu import menu_router
from handlers.start import start_router
from handlers.survey import survey_router


async def on_startup(bot: Bot):
    await database.create_tables()


async def main():
    dp.include_router(menu_router)
    dp.include_router(start_router)
    dp.include_router(survey_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
