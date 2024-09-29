import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

ADMIN_ID = '933411060'
API_TOKEN = '6841922778:AAG8qdkKO6vE0GHrEOgSNlDLAlwu4h8S_MQ'
DATABASE = 'Anonym_message_users'
MESSAGE_DATA = 'anonym_message_all'
QUEUE_DATA = 'users_in_queue'
TABLE = 'table_for_user'
CURRENCY_DATABASE = 'data_currency'
REGISTER_DB = 'database_premium'
INTEREST = 'database_interests'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.ERROR)