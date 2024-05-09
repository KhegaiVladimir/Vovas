from aiogram import Router, types, F
from aiogram.filters import Command
from config import database

menu_router = Router()


@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='блюда')
            ],
            [
                types.KeyboardButton(text='напитки')
            ],
            [
                types.KeyboardButton(text='салаты')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите тип еды', reply_markup=kb)


types_of_food = ['блюда', 'напитки', 'салаты']


@menu_router.message(F.text.lower().in_(types_of_food))
async def show_menu(message: types.Message):
    food_type = message.text.lower()
    kb = types.ReplyKeyboardRemove()
    await message.answer(f'Все наше меню из {food_type}', reply_markup=kb)
    data = await database.fetch(
        """
            SELECT food.* FROM food 
            JOIN type_of_food ON food.type_id = type_of_food.id
            WHERE type_of_food.name = ?
            """,
        (food_type,),
        fetch_type='all')
    for food in data:
        price = food['price']
        name = food['name']
        await message.answer(f'Название еды: {name}\nЦена: {price} сом')