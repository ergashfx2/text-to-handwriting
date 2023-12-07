from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types.base import InputFile
from unidecode import unidecode

from data.config import texts
from handlers.user.admin import get_user_data
from keyboards.default.mainM import main
from keyboards.inline.page import page1, page2, page3
from loader import bot
from loader import dp
from utils.misc import transliterate

error = "Xatolik yuz berdi kiritgan matningizda klaviaturada mavjud bo'lmagan belgilar mavjud bo'lishi mumkin ular quyidagilar bo'lishi mumkin\n\n’\n‘\n”\n“\n„\n«\n»\n‹\n›\n\n*Agar bula mavjud bo'lmasa @Contactim_bot ga kiritgan matningizni yozib yuboring adminimiz tomonidan tekshirib beriladi*"
import re

values = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890-_=+/?,.!"\n  ')


def remover(my_string=""):
    for item in my_string:
        if item not in values:
            my_string = my_string.replace(item, "")
    return my_string


@dp.message_handler(state='stil1')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson1.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson11.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")


@dp.message_handler(state='stil2')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson2.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson22.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")


# 3

@dp.message_handler(state='stil3')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson3.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson33.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")

            # 4


@dp.message_handler(state='stil4')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/new1.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson44.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")


# 5

@dp.message_handler(state='stil5')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/new2.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson55.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")


# 6

@dp.message_handler(state='stil6')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/new3.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson66.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")


# 7

@dp.message_handler(state='stil7')
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    print(aniq)
    respond = msg.text
    b = unidecode(respond).replace('"', "'")
    a = remover(b)
    if aniq == 2:
        try:
            await msg.answer_photo(f"https://grabus.uz/new4.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
    else:
        try:
            await msg.answer_photo(f"https://grabus.uz/oson77.php?text={a}&rang={rangi}",
                                   caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                                   parse_mode="markdown")
            await msg.answer("Bizning ikkinchi botimizni sinab ko'ring : @Konspektor_bot")
        except:
            await msg.answer(error, parse_mode="markdown")
