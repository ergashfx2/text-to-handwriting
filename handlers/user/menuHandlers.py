import openai
from PIL import Image
from aiogram import types
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import CallbackQuery
from aiogram.types.base import InputFile
from aiogram.types.base import InputFile
from pytesseract import pytesseract
from unidecode import unidecode

from data.config import texts
from data.config import texts, stil
from handlers.user.admin import get_user_data
from handlers.user.sendimages import remover
from keyboards.default import mainM
from keyboards.default.mainM import main, back, fonts, ranglar
from keyboards.default.mainM import main, back, stillar
from keyboards.inline.page import page1, page2, page3, page4, page5, page6, page7
from keyboards.inline.page import page1, page2, page3, page4, page5, page6, page7
from loader import bot
from loader import bot
from loader import dp
from loader import dp

openai.api_key = "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"


def chat(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": message},
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return result


@dp.message_handler(text="Konspekt yozish ✍🏻")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer_photo(photo="https://t.me/testiszlar/234", caption="*O'zingizga kerakli varoq "
                                                                        "sonini tanlang👇*",
                           parse_mode="markdown", reply_markup=stillar)
    await state.set_state("stillar")


@dp.message_handler(state="stillar")
async def welcome(msg: types.Message, state: FSMContext):
    number = msg.text
    stil_number = stil[f"{number}"]
    await msg.answer("*Varoqqa yozish uchun matn kiriting ...✍🏻*", parse_mode="markdown", reply_markup=back)
    await state.set_state(stil_number)


@dp.message_handler(text="📄 Insho yozdirish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer("*Mavzu yozing*", parse_mode="markdown", reply_markup=back)
    await state.set_state("chatgdp")


@dp.message_handler(state="chatgdp")
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer("Kutib turing bu 1 2 daqiqa vaqt olishi mumkin")
    await bot.send_chat_action(message.chat.id, action=types.ChatActions.TYPING)
    await bot.send_chat_action(message.chat.id, action=types.ChatActions.TYPING)
    msg = chat(message.text)
    await bot.send_chat_action(message.chat.id, action=types.ChatActions.TYPING)
    await message.answer(msg)


# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def to_latin(msg: types.Message, state: FSMContext):
#     kim = get_user_data(cid=msg.from_user.id)
#     aniq = int(kim[3])
#     rangi = str(kim[4]).replace(" ", "")
#     await msg.answer("Kutib turing....")
#     id = msg.photo[2]["file_id"]
#     file = await bot.get_file(id)
#     file_path = file.file_path
#     await bot.download_file(file_path, destination="images/image.png")
#     img = Image.open('images/image.png')
#     pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#     result = pytesseract.image_to_string(img)
#     b = unidecode(result).replace('"',"'")
#     a = remover(b)
#     await msg.answer(result)
#     await msg.answer_photo(f"https://grabus.uz/oson1.php?text={a}&rang={rangi}",
#                            caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
#                            parse_mode="markdown")


@dp.message_handler(text="✏️ Yozuv stili")
async def to_latin(msg: types.Message, state: FSMContext):
    await msg.answer_photo("https://t.me/testiszlar/339",
                           caption="BIzda 2 ta yozuv uslubi mavjud o'zingizga yoqqanini tanlang", reply_markup=fonts)
    await state.set_state("font")


@dp.message_handler(text="✒️ Yozuv rangi")
async def to_latin(msg: types.Message, state: FSMContext):
    await msg.answer("Bizda 3 ta rang mavjud qaysi biriga o'zgartirmoqchisiz ?", reply_markup=ranglar)
    await state.set_state("rang")


@dp.message_handler(text="❓ Botdan qanday foydalanaman")
async def to_latin(msg: types.Message, state: FSMContext):
    await msg.answer_video("https://t.me/testiszlar/236",
                           caption="Botdan qanday foydalanishni bilmasangiz ushbu videoni ko'ring")
