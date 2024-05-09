from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
import asyncio
import logging
from aiogram.filters import Command
import random
import os



load_dotenv()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}')


@dp.message(Command('info'))
async def start_cmd(message: types.Message):
    await message.answer(f'Вот информация: id: {message.from_user.id},'
                         f' first name: {message.from_user.first_name},'
                         f'username: {message.from_user.username}')

@dp.message(Command('random_pic'))
async def start_cmd(message: types.Message):
    img_list = os.listdir(r'C:\Users\Vladimir\PycharmProjects\pythontelegram_bots\images')
    img_path = random.choice(img_list)
    file = types.FSInputFile(f'images/{img_path}')
    await message.answer_photo(photo=file)




async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
