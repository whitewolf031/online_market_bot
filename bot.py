from _ast import Lambda
from operator import call
from telebot import TeleBot
from telebot.types import LabeledPrice
from db_bot.computer_db import Computer_db
from db_bot.tv_db import Tv_db
from keyboard import *
from db_bot.laptop_db import Laptop_db
from localisation.localisation_keyboard import *
from localisation.localisation_bot import *
from config import Config

token = Config().token
bot = TeleBot(token)
click_token = Config().click_token
localisation_lang = {}

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f"Assalomu aleykum {first_name} Bizning onlayn market botimizga xush kelibsiz ")
    localisation(message)

def localisation(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "tilni tanlang", reply_markup=localisation_keyboard())
    bot.register_next_step_handler(message, menu)

def menu(message):
    chat_id = message.chat.id
    lang = localisation_lang.get(chat_id)


    if message.text == "uz":
        lang = "uz"

    if message.text == "ru":
        lang = "ru"

    if message.text == "eng":
        lang = "eng"

    bot.send_message(chat_id, select_catalog[lang], reply_markup=menu_keyboard(lang))

    localisation_lang[chat_id] = lang
    bot.register_next_step_handler(message, products_catalog)


def products_catalog(message, product_id=0, products=None):
    chat_id = message.chat.id
    lang = localisation_lang.get(chat_id)

    if message.text == back_menu[lang]:
        return start(message)

    if message.text == catalogs_laptop[lang]:
        products = Laptop_db().select_data()

    if message.text == catalogs_pc[lang]:
        products = Computer_db().select_data()

    if message.text == catalogs_tv[lang]:
        products = Tv_db().select_data()

    if message.text == go_to_next[lang] and product_id < len(products):
        product_id += 1

    if message.text == go_to_back[lang] and product_id > 0:
        product_id -= 1

    product = products[product_id]


    product_title = product[0]
    product_url = product[1]
    image = product[2]
    product_price = product[3]
    product_description = product[4]
    bot.send_photo(chat_id, image, caption=f'{"Brand_name"}: {product_title}\n\n'
                                           f'{"Description"}: {product_description}'
                                           f'\n\n{"Price"}: {product_price}',
                   reply_markup=product_inline_url(product_url, lang))

    user_message = bot.send_message(chat_id, f"{"Qolgan malumotlar soni"} : {len(products) - (product_id + 1)}", reply_markup=generate_pagination(lang))

    if message.text == "Oldinga" and len(products) - (product_id + 1) == 0:
        bot.delete_message(chat_id, message.id + 2)
        bot.send_message(chat_id, "No products!", reply_markup=generate_pagination(lang))
        product_id = product_id - len(products) # -1
    bot.register_next_step_handler(user_message, products_catalog, product_id, products)

@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    chat_id = call.message.chat.id
    if call.data == "buy":
        product_info = call.message.caption.split(": ")
        product_price = ""
        price = product_info[-1].replace('UZS', "")
        for x in price:
            if x.isdigit():
                product_price += x

        INVOICE = {
            "title": product_info[1],
            "description": product_info[3],
            "invoice_payload": "bot-defined invoice payload",
            "provider_token": click_token,
            "start_parameter": "pay",
            "currency": "UZS",
            "prices": [LabeledPrice(label=product_info[1], amount=int(product_price + "00"))],
        }

        bot.send_invoice(chat_id, **INVOICE)

bot.polling(non_stop=True)