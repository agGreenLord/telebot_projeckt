
import telebot
from telebot import types

TOKEN = "5827639233:AAFoJXxbXJ9oWtsL9nIuVbaOEK35apz79AI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """
    Бот позволяет оставить заявку на ремонт, диагностику электроники, бытовой техники, проводки. С чем работать будем?
    "Электроника" 
    "Крупная бытовая техника" 
    "Проводка""")

# Попытался сделать кнопку но она пока не работает
@bot.message_handler(commands=['button'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Электроника")
    btn2 = types.KeyboardButton('Бытовая техника')
    btn3 = types.KeyboardButton('Проводка')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Выберете что вам необходимо починить", reply_markup=markup)


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



bot.infinity_polling()

