import sqlite3

from aiogram import types, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, types


survey_router = Router()
db = sqlite3.connect('db.sqlite')
cursor = db.cursor()
class Survey(StatesGroup):
    name = State()
    phone_number = State()
    last_appearence = State()
    food_quality = State()
    clearity = State()
    additional_info = State()

@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()

@survey_router.callback_query(F.data == 'survey')
async def start_survey(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Survey.name)
    await callback.message.answer('Как вас зовут?')

@survey_router.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Survey.phone_number)
    await message.answer('Какой у вас номер телефона?')

@survey_router.message(Survey.phone_number)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(Survey.last_appearence)
    await message.answer('Сколько дней назад вы были в кафе?')

@survey_router.message(Survey.last_appearence)
async def process_last_appearence(message: types.Message, state: FSMContext):
    data=message.text
    if not data.isdigit():
        await message.answer('Введите кол-во дней')
        return
    if int(data) <= 1 or int(data) >= 100:
        await message.answer('Пожалуйста введите кол-во дней от 1 до 100')
        return
    await state.update_data(last_appearence=message.text)
    await state.set_state(Survey.food_quality)
    await message.answer('Оцените качество еды')


@survey_router.message(Survey.food_quality)
async def process_food_quality(message: types.Message, state: FSMContext):
    await state.update_data(food_quality=message.text)
    await state.set_state(Survey.clearity)
    await message.answer('Оцениту чистоту ресторана')

@survey_router.message(Survey.clearity)
async def process_clearity(message: types.Message, state: FSMContext):
    await state.update_data(clearity=message.text)
    await state.set_state(Survey.additional_info)
    await message.answer('Укажите дополнительную информацию')

@survey_router.message(Survey.additional_info)
async def process_additional_info(message: types.Message, state: FSMContext):
    await state.update_data(additional_info=message.text)
    data = await state.get_data()
    cursor.execute(
        "INSERT INTO survey (name, phone_number, last_appearence, food_quality, clearity, additional_info) VALUES (?,?,?,?,?,?)",
        (data['name'], data['phone_number'], data['last_appearence'], data['food_quality'], data['clearity'],
         data['additional_info'])
        )

    await message.answer('Спасибо за пройденный опрос!')
    db.commit()