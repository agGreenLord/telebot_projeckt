import telebot
from telebot import types

from config import BOT_TOKEN, ADMIN_CHAT_TOKEN
from state import Store, Record, ClientData
from mocked_data import HELLO_MESSAGE, ORDER_MESSAGE, INFO_MESSAGE, PROBLEMS_MESSAGE, OTHER_MESSAGE, STAGES


bot = telebot.TeleBot(BOT_TOKEN)
user_storage = Store()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Info')
    btn2 = types.KeyboardButton('Order')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, HELLO_MESSAGE, reply_markup=markup)

    empty_client_data = ClientData('', '')
    record = Record(message.from_user.id, empty_client_data, STAGES[0])
    user_storage.add_new_record(record)
    print(user_storage.storage)

@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id
    get_message_text = message.text.lower()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Надо почитать про утечку памяти и как правильно с ней работать
    send_message_text = ' '

    match get_message_text:
        #Блок ORDER
        case 'order' | '/order':
            send_message_text = PROBLEMS_MESSAGE
            btn1 = types.KeyboardButton('Электроника')
            btn2 = types.KeyboardButton('Бытовая техника')
            btn3 = types.KeyboardButton('Проводка')
            markup.add(btn1, btn2, btn3)
        #Блок INFO
        case 'info' | '/info':
            send_message_text = INFO_MESSAGE
            btn1 = types.KeyboardButton('Order')
            markup.add(btn1)
        #Выбор проблемы
        case 'электроника' | 'бытовая техника' | 'проводка':
            send_message_text = ORDER_MESSAGE
        case _:
            if get_message_text.isdigit() and get_message_text.startswith("351") and len(get_message_text)==12:
                send_message_text = 'cпасибо, мастер скоро с вами свяжется'
            elif get_message_text.isalnum() or len(get_message_text) != 12:
                send_message_text = 'номер введен неверно, попробуйте еще'
            else:
                send_message_text = OTHER_MESSAGE
    bot.send_message(user_id, send_message_text, reply_markup=markup)

