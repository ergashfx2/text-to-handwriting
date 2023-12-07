from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from data.config import CHANNELS, texts, btns, Text_caption, Button_text
from handlers.user.admin import block_user
from keyboards.default.mainM import main
from loader import bot, dp
from utils.misc import subscription


@dp.callback_query_handler()
async def callback_fun(call):
    cid = call.message.chat.id
    try:
        if call.data == "check_subs":
            user = call.from_user.id
            final_status = True
            chs = []
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
                await call.message.answer(Text_caption[0], reply_markup=types.InlineKeyboardMarkup(inline_keyboard=chs),
                                          disable_web_page_preview=True, parse_mode="markdown")
            else:
                await call.message.answer(texts['accepted'], reply_markup=main, disable_web_page_preview=True)
            await bot.delete_message(cid, call.message.message_id)
    except Exception as e:
        print(e)
        if "was blocked" in str(e):
            block_user(cid)
