from telebot import types


def localisation_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_uz = types.KeyboardButton(text="uz")
    btn_ru = types.KeyboardButton(text="ru")
    btn_eng = types.KeyboardButton(text="eng")
    keyboard.row(btn_uz, btn_ru, btn_eng)
    return keyboard

def menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_computers = types.KeyboardButton(text="computers")
    btn_laptops = types.KeyboardButton(text="laptop")
    btn_TV = types.KeyboardButton(text="TVs")
    btn_else = types.KeyboardButton(text="else items")
    keyboard.row(btn_computers, btn_laptops, btn_TV, btn_else)
    return keyboard