import telebot

TOKEN = "8050333359:AAEc7mNDQpH27krujRlRpYZXuPqp0nH81Z8"
SECRET_CODE = "1234"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, Ильдар! Введи код.")

@bot.message_handler(func=lambda m: True)
def check(message):
    if message.text == SECRET_CODE:
        bot.send_message(message.chat.id, "Ты угадал!")
    else:
        bot.send_message(message.chat.id, "Не попал")

bot.polling()
