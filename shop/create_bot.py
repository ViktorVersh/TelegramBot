"""
Отдельно создал бота, чтобы в дальнейшем избежать перекрестных ссылок
"""
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import config

bot: Bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
