import logging
from aiogram import executor

import filters
import handlers
import middlewares
from loader import dp

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp)
