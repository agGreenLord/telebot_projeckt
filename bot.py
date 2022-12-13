import telebot
from telebot import types

TOKEN = "5827639233:AAFoJXxbXJ9oWtsL9nIuVbaOEK35apz79AI"
bot = telebot.TeleBot(TOKEN)

print('runned')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Info')
    btn2 = types.KeyboardButton('Oder')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, """Привет! Я бот, который позволяет оставить заявку мастеру на починку электроники, бытовой техники или проводки.
        Вы можете:
        /info - узнать информацию о мастере
        /oder - оставить заявку на звонок мастера""", reply_markup=markup)




@bot.message_handler(content_types=['text'])
def get_message(message):
    #Блок ODER
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
                'Пожалуйста, оставьте свой номер телефона, чтобы мастер смог с вами связаться, узнать о проблеме и назначить удобное время встречи')
    elif message.text.lower() == 'бытовая техника':
        bot.send_message(message.from_user.id,
                'Пожалуйста, оставьте свой номер телефона, чтобы мастер смог с вами связаться, узнать о проблеме и назначить удобное время встречи')
    elif message.text.lower() == 'проводка':
        bot.send_message(message.from_user.id,
                'Пожалуйста, оставьте свой номер телефона, чтобы мастер смог с вами связаться, узнать о проблеме и назначить удобное время встречи')





bot.infinity_polling()

