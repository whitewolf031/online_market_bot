from telebot import TeleBot
from keyboard  import *

token = "7344409682:AAFhtjg7SCH3ldg4-QkS8sTUqSO5E-Nsn_Q"

bot = TeleBot(token)

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
    bot.send_message(chat_id, "bo'limni tanlang", reply_markup=menu_keyboard())

bot.polling()