from aiogram import types


def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Информация', callback_data='info_about_us')
            ]
            ,
            [
                types.InlineKeyboardButton(text='Меню', callback_data='menu')
            ]
            ,
            [
                types.InlineKeyboardButton(text='Опрос', callback_data='survey')
            ]
            ,
            [
                types.InlineKeyboardButton(text='Получить ссылки', callback_data='get_links')
            ]
        ]
    )
    return kb