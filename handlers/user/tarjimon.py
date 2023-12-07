from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.mainM import back, settings
from loader import dp
from utils.misc import transliterate


@dp.message_handler(text="📃 Matnni lotinga o'girish")
async def to_latin(msg: types.Message, state: FSMContext):
    await msg.answer("Lotin alifbosiga o'girish uchun matn kiriting", reply_markup=back)
    await state.set_state("lotin")


@dp.message_handler(state="lotin")
async def convert(msg: types.Message):
    respond = transliterate.transliterate(msg.text, to_variant="latin")
    print(respond)
    await msg.answer(respond)


@dp.message_handler(text="⚙️ Sozlamalar")
async def to_latin(msg: types.Message, state: FSMContext):
    await msg.answer("Nimani o'zgartirmoqchisiz marhamat tanlang", reply_markup=settings)
