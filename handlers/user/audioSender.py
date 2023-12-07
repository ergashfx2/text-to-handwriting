import speech_recognition as sr
from PIL import Image
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
from pytesseract import pytesseract
from unidecode import unidecode

from data.config import texts
from handlers.user.admin import get_user_data
from handlers.user.sendimages import remover, error
from keyboards.default.mainM import main
from keyboards.inline.page import page1, page2, page3
from loader import bot
from loader import dp

# initialize the recognizer
r = sr.Recognizer()

from handlers.user.speechToText import get_large_audio_transcription


@dp.message_handler(state='stil1', content_types=types.ContentType.VOICE)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.voice.file_id
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/voice.wav")
    textlari = get_large_audio_transcription(path="images/voice.wav")
    await msg.answer(textlari)
    b = unidecode(textlari).replace('"', "'")
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


@dp.message_handler(state='stil2', content_types=types.ContentType.PHOTO)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/image.png")
    img = Image.open('images/image.png')
    pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    b = unidecode(result).replace('"', "'")
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

@dp.message_handler(state='stil3', content_types=types.ContentType.PHOTO)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/image.png")
    img = Image.open('images/image.png')
    pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    b = unidecode(result).replace('"', "'")
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


@dp.message_handler(state='stil4', content_types=types.ContentType.PHOTO)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/image.png")
    img = Image.open('images/image.png')
    pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    b = unidecode(result).replace('"', "'")
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

@dp.message_handler(state='stil5', content_types=types.ContentType.PHOTO)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/image.png")
    img = Image.open('images/image.png')
    pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    b = unidecode(result).replace('"', "'")
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

@dp.message_handler(state='stil6', content_types=types.ContentType.PHOTO)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/image.png")
    img = Image.open('images/image.png')
    pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    b = unidecode(result).replace('"', "'")
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

@dp.message_handler(state='stil7', content_types=types.ContentType.PHOTO)
async def send_stil1(msg: types.Message, state: FSMContext):
    kim = get_user_data(cid=msg.from_user.id)
    aniq = int(kim[3])
    rangi = str(kim[4]).replace(" ", "")
    await msg.answer("Kutib turing....")
    id = msg.photo[2]["file_id"]
    file = await bot.get_file(id)
    file_path = file.file_path
    await bot.download_file(file_path, destination="images/image.png")
    img = Image.open('images/image.png')
    pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    b = unidecode(result).replace('"', "'")
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
