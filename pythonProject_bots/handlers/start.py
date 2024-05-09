from aiogram import Router, types, F
from aiogram.filters import Command
from keyborad import start_keyboard
from crawler.house_kg import HouseCrawler

start_router = Router()
@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Добро пожаловать в наше кафе'
                         f' ниже выберите что хотите узнать', reply_markup = start_keyboard())

@start_router.callback_query(F.data == 'info_about_us')
async def info_about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Наш адрес: Пушкина 911 \n'
                                  'Контакты: +123123123 \n'
                                  'Сайт: https://kulikov.com \n')


@start_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Выберите что хотели бы посмотреть из меню то нажмите на /menu' )


@start_router.callback_query(F.data == 'get_links')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    crawler = HouseCrawler()
    all_links = await crawler.get_house()
    await callback.message.answer('Вот ссылки на покупку дома')
    for link in all_links:
        await callback.message.answer(link)









