"""
Файл взаимодействия с клиентом
"""
from aiogram import Router, types
from aiogram.filters import CommandStart

from shop.create_bot import bot
from shop.drinks_list import drinks, formatted_drinks
from shop.keyboard import get_drinks_keyboard, buy_drinks_keyboard

router = Router()


@router.message(CommandStart())
async def sale_command(message: types.Message):
    """Отзыв на команду "/start", подключение инлайн кнопок"""
    await message.answer("Добро пожаловать в магазин напитков! Выберите напиток для заказа:",
                         reply_markup=get_drinks_keyboard())


# Функция отправки сообщения с ошибкой
async def send_error_message(message: types.Message, text: str):
    await message.answer(text)


@router.callback_query()
async def process_drink_order(callback_query: types.CallbackQuery):
    drink_name = callback_query.data  # Получаем название напитка из callback_data
    if drink_name in drinks:
        await bot.send_message(callback_query.from_user.id, f"Вы заказали: {drink_name} за "
                                                            f"{drinks[drink_name]} ₽.\nСпасибо за ваш заказ!",
                               reply_markup=buy_drinks_keyboard())
        await callback_query.answer()  # Ответ на запрос callback
    else:
        await send_error_message(callback_query.message, f"Извините, такой напиток не найден. "
                                                         f"Пожалуйста, выберите из списка:\n{formatted_drinks}")
