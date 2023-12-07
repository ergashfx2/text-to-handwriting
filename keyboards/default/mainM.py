from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Konspekt yozish ✍🏻"),
        KeyboardButton(text=" 📃 Matnni lotinga o'girish")
    ],
    [
        KeyboardButton(text="⚙️ Sozlamalar"),
        KeyboardButton(text="❓ Botdan qanday foydalanaman")
    ],
    [
        KeyboardButton(text="📄 Insho yozdirish")
    ],
])

stillar = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="1"),
        KeyboardButton(text="2"),
        KeyboardButton(text="3"),
        KeyboardButton(text="4"),
        KeyboardButton(text="5"),
        KeyboardButton(text="6"),
        KeyboardButton(text="7"),

    ],
    [
        KeyboardButton(text="Ortga qaytish"),
    ]
])

back = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Ortga qaytish")
    ]
])

settings = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="✏️ Yozuv stili"),
        KeyboardButton(text="✒️ Yozuv rangi")
    ],
    [
        KeyboardButton("Ortga qaytish")
    ]
])

fonts = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="1"),
        KeyboardButton(text="2"),
    ],
    [
        KeyboardButton("Ortga qaytish")
    ]
])

ranglar = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="🔵 Ko'k rang"),
        KeyboardButton(text="⚫️ Qora rang"),
        KeyboardButton(text="🟢 Yashil rang")
    ],
    [
        KeyboardButton("Ortga qaytish")
    ]
])
