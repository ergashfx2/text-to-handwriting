from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.user.admin import create_user, get_user_data
from keyboards.default.mainM import main
from loader import dp
from utils.db_api.sqlite import db


@dp.message_handler(text=["/start", "Ortga qaytish"])
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer("*Kerakli bo'limni tanlang 👇*", parse_mode="markdown", reply_markup=main)
    await state.finish()


@dp.message_handler(text=["/start", "Ortga qaytish"],
                    state=["font", "rang", "lotin", "stil1", "stil2", "stil3", "stil4", "stil5", "stil6", "stil7",
                           "stillar", "chatgdp"])
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer("*Kerakli bo'limni tanlang 👇*", parse_mode="markdown", reply_markup=main)
    await state.finish()
