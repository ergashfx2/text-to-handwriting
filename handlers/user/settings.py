from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.db_api.sqlite import db


@dp.message_handler(state="font")
async def hello(msg: types.Message):
    num = db.update_user_font(font=msg.text, cid=msg.from_user.id)
    await msg.answer("✅ *Muvaffaqiyatli o'zgartirildi*", parse_mode="Markdown")


@dp.message_handler(text="🔵 Ko'k rang", state="rang")
async def hello(msg: types.Message):
    num = db.update_user_color(rang="Ko'k", cid=msg.from_user.id)
    await msg.answer("✅ *Muvaffaqiyatli o'zgartirildi*", parse_mode="Markdown")


@dp.message_handler(state="rang")
async def hello(msg: types.Message):
    rangi = msg.text[2:]
    color = rangi[:6]
    num = db.update_user_color(rang=color, cid=msg.from_user.id)
    await msg.answer("✅ *Muvaffaqiyatli o'zgartirildi*", parse_mode="Markdown")
