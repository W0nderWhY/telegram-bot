import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
SECRET_CODE = "0878"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, Ильдар! Введи код.")

@bot.message_handler(func=lambda m: True)
def check(message):
    if message.text == SECRET_CODE:
        bot.send_message(message.chat.id, "Ты угадал! Посмотри на кухне под своим стулом!")
    else:
        bot.send_message(message.chat.id, "Не попал. Посмотри на цифры почтового адреса!")

bot.polling()
