BOT_TOKEN = '1816873661:AAEuynpfpPr0KRJ2IhrmV5gQQCUAoi3KFHE'
from utils.db_api.sqlite import db

admins = db.select_all_adminss()
channels = db.select_all_channel()
id_list = [id[0] for id in channels]
CHANNELS = list(map(lambda x: x[0], channels))

ids = [id[0] for id in admins]
ADMINS = list(map(lambda x: x[0], admins))
texts = db.select_all_from_texts()

Button_text = [texts[0][1]]
Text_caption = [texts[0][0]]

btns = {
    "accept": "Tekshirish",
    "back": "Ortga qaytish",
}

texts = {
    "main_menu": "Iltimos quyidagi menulardan birini tanlang!",
    "accepted": "*Kerakli bo'limni tanlang 👇*"
}

stil = {
    "1": "stil1",
    "2": "stil2",
    "3": "stil3",
    "4": "stil4",
    "5": "stil5",
    "6": "stil6",
    "7": "stil7"
}
