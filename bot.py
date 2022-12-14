import telebot
from telebot import types
# from config.config import BOT_TOKEN
from config import BOT_TOKEN, HELLO_MESSAGE
from config.messages import ORDER_MESSAGE

bot = telebot.TeleBot(BOT_TOKEN)

print('runned')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Info')
    btn2 = types.KeyboardButton('Oder')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, HELLO_MESSAGE, reply_markup=markup)




@bot.message_handler(content_types=['text'])
def get_message(message):
    #Блок ORDER
    if message.text.lower() == 'oder' or message.text == '/oder':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Электроника")
        btn2 = types.KeyboardButton('Бытовая техника')
        btn3 = types.KeyboardButton('Проводка')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберете что вам необходимо починить", reply_markup=markup)



    #Блок INFO
    elif message.text.lower() == 'info' or message.text == '/info':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Oder')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Здесь будет текст о мастере', reply_markup=markup)

    #Выбор проблемы
    elif message.text.lower() == 'электроника':
        bot.send_message(message.from_user.id,
                ORDER_MESSAGE)
    elif message.text.lower() == 'бытовая техника':
        bot.send_message(message.from_user.id,
                ORDER_MESSAGE)
    elif message.text.lower() == 'проводка':
        bot.send_message(message.from_user.id,
                ORDER_MESSAGE)





bot.infinity_polling()

