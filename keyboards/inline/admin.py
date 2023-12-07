from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="➕ Kanal qo'shish", callback_data="add")
    ],
    [
        InlineKeyboardButton(text="➖ Kanal uzish", callback_data="remove")
    ],
    [
        InlineKeyboardButton(text="👨‍💻 Adminlar", callback_data="admins")
    ],
    [
        InlineKeyboardButton(text="📡 Barcha kanallar", callback_data="channels")
    ],
    [
        InlineKeyboardButton(text=" ⚙️ Boshqa sozlamalar", callback_data="settings")

    ],
    [
        InlineKeyboardButton("❌ Panelni yopish", callback_data="hide")
    ]
])

admin_second = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✏️ Matn o'zgartirish", callback_data="add_text")
    ],
    [
        InlineKeyboardButton(text="🕹 Tugma nomi", callback_data="button")
    ],
    [
        InlineKeyboardButton("🔝 Asosiy menyu", callback_data="main")
    ]
])

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⛔️ Bekor qilish", callback_data="main"),
    ]
])

yes_no = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅", callback_data="yes"),
        InlineKeyboardButton(text="❌", callback_data="no")
    ]
])


def create_channels_button(names):
    channels_button = InlineKeyboardMarkup()
    back = InlineKeyboardButton(text="🔝 Asosiy menyu", callback_data="main")
    for text, callback_data in names.items():
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        channels_button.add(button)
    channels_button.add(back)
    return channels_button


def create_admins_button(names):
    list = InlineKeyboardMarkup()
    add = InlineKeyboardButton(text="➕ Admin qo'shish", callback_data="add_admin")
    back = InlineKeyboardButton(text="🔝 Asosiy menyu", callback_data="main")
    list.add(add)
    for text, callback_data in names.items():
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        list.add(button)
    list.add(back)
    return list
