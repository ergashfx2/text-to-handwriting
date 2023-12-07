from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS, btns, texts, Button_text, Text_caption
from handlers.user.admin import create_user
from loader import bot
from utils.misc import subscription


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            full_name = update.message.from_user.full_name
            create_user(user, full_name, font="1", rang="Ko'k")
        elif update.callback_query:
            user = update.callback_query.from_user.id
            full_name = update.callback_query.from_user.full_name
            create_user(user, full_name, font="1", rang="Ko'k")
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        result = Text_caption[0]
        final_status = True
        chs = []
        if update.message and update.message.chat.type == "private":
            for channel in CHANNELS:
                status = await subscription.check(
                    user_id=user,
                    channel=channel
                )
                final_status *= status
                channel = await bot.get_chat(channel)
                if not status:
                    invite_link = await channel.export_invite_link()
                    chs.append([types.InlineKeyboardButton(Button_text[0], url=invite_link)])
            chs.append([types.InlineKeyboardButton(text=btns["accept"], callback_data="check_subs")])
            if not final_status:
                await update.message.answer(result, reply_markup=types.InlineKeyboardMarkup(inline_keyboard=chs),
                                            disable_web_page_preview=True, parse_mode="markdown")
                raise CancelHandler()
