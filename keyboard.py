from telebot import types
from localisation.localisation_keyboard import *

def localisation_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_uz = types.KeyboardButton(text="uz")
    btn_ru = types.KeyboardButton(text="ru")
    btn_eng = types.KeyboardButton(text="eng")
    keyboard.row(btn_uz, btn_ru, btn_eng)
    return keyboard

def menu_keyboard(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_computers = types.KeyboardButton(text=catalogs_pc[lang])
    btn_laptops = types.KeyboardButton(text=catalogs_laptop[lang])
    btn_TV = types.KeyboardButton(text=catalogs_tv[lang])
    keyboard.row(btn_computers, btn_laptops, btn_TV)
    return keyboard

def product_inline_url(url, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_buy = types.InlineKeyboardButton(text=for_buy[lang], callback_data="buy")
    btn_url = types.InlineKeyboardButton(text=for_url[lang], url=url)
    keyboard.row(btn_buy, btn_url)
    return keyboard

def generate_pagination(lang):
    keyboard = types.InlineKeyboardMarkup()
    step_go = types.KeyboardButton(text=go_to_next[lang])
    step_back = types.KeyboardButton(text=go_to_back[lang])
    step_back_menu = types.KeyboardButton(text=back_menu[lang])
    keyboard.row(step_go,step_back)
    keyboard.row(step_back_menu)
    return keyboard