import logging
import telebot


TOKEN = "5827639233:AAFoJXxbXJ9oWtsL9nIuVbaOEK35apz79AI"
logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """
    Бот позволяет оставить заявку на ремонт, диагностику электроники, бытовой техники, проводки. С чем работать будем?
    "Электроника" 
    "Крупная бытовая техника" 
    "Проводка""")

@bot.message_handler(content_types=['text'])
def send_massage(message):
    if message.text.lower() == 'электроника':
         bot.send_message(message.chat.id, 'Когда вам было бы удобно, чтобы с вами связался мастер?')
    elif message.text.lower() == 'бытовая техника':
        bot.send_message(message.chat.id, 'Когда вам было бы удобно, чтобы с вами связался мастер?')
    elif message.text.lower() == 'проводка':
        bot.send_message(message.chat.id, 'Когда вам было бы удобно, чтобы с вами связался мастер?')
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю, пожалуйста напишите один из предложенных вариантов')



bot.polling()

