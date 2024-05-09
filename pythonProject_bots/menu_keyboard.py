from aiogram import types


def menu_keyboard():
    menu_kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Заказать', callback_data='bludo')
            ]
        ]
    )
    return menu_kb
