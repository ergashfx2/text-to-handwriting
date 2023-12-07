from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

from loader import bot


async def message_throttled(message: types.Message, throttled: Throttled):
    if throttled.exceeded_count <= 2:
        await bot.send_message(message.chat.id, "Iltimos qayta-qayta yozmang!")


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=0.6, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        print(f"{message.from_user.full_name}[{message.from_user.id}] => {message.text}")
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await message_throttled(message, t)
            raise CancelHandler()
