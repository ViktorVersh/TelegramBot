"""
Здесь создаем клавиатуры
"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from shop.drinks_list import drinks


def start_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=
    [
        [InlineKeyboardButton(text="Новости", callback_data="/news")],
        [InlineKeyboardButton(text="Магазин напитков", callback_data="/sale")]

    ], resize_keyboard=True, input_field_placeholder='Воспользуйтесь меню')
    return kb


def get_drinks_keyboard():
    keyboard = []
    for drink_name, price in drinks.items():
        button = [InlineKeyboardButton(text=f"{drink_name} - {price} ₽", callback_data=drink_name)]
        keyboard.append(button)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def buy_drinks_keyboard():
    buy_key = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплата', url='https://market.yandex.ru'),
        ]
    ], resize_keyboard=True)
    return buy_key
