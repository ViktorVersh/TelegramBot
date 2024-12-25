import asyncio
import logging

# from shop import drink_run
from shop.create_bot import bot, dp
from shop.drink_run import router

"""
Основной файл запуска бота.
Структура проекта:
    1. create_bot.py - создание бота
    2. drink_run.py - роутер для бота, handlers 
    3. drink.py - основной файл, в котором запускается бот
    4. config.py - файл с конфигурацией
    5. db.py - файл с базой данных
    6. drinks_list.py - файл со списком доступных напитков
    7. state_info.py - файл с информацией о состоянии бота(пока не использовал)
"""


async def main():
    dp.include_router(router)  # в диспетчер dp добавляем роутер для выполнения роутером задач которые
    # определены в drink_run
    await bot.delete_webhook(
        drop_pending_updates=True)  # аналог записи skip_updates=True из более старых версий aiogram
    await dp.start_polling(bot)  # Запуск бота в режиме опроса (polling)


if __name__ == '__main__':
    # Настройка логирования
    (
        logging.basicConfig
        (
            level=logging.INFO,
            format='%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    )
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен пользователем")
