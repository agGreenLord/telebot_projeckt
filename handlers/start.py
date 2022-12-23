import telebot
from telebot import types

from config import BOT_TOKEN, ADMIN_CHAT_TOKEN
from state import Store, Record, ClientData
from mocked_data import HELLO_MESSAGE, STAGES, StageList




bot = telebot.TeleBot(BOT_TOKEN)
user_storage = Store()
admin_id = ADMIN_CHAT_TOKEN


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Info')
    btn2 = types.KeyboardButton('Order')
    markup.add(btn1, btn2)
    bot.send_message(chat_id, HELLO_MESSAGE, reply_markup=markup)

    user_storage.delete_record(chat_id)
    empty_client_data = ClientData('', '')
    record = Record(chat_id, empty_client_data, StageList.hello_stage)
    user_storage.add_new_record(record)


@bot.message_handler(content_types=['text'])
def get_message(message):
    chat_id = message.chat.id

    get_message_text = message.text.lower()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Надо почитать про утечку памяти и как правильно с ней работать
    send_message_text = 'Произошла непридвиденная ошибка, работы по устранению уже ведутся.\n\n Попробуйте написат позже'

    print('current_stage', user_storage.get_record_by_chat_id(chat_id).current_stage)
    print('StageList.hello_stage', StageList.hello_stage)

    match user_storage.get_record_by_chat_id(chat_id).current_stage:
        case StageList.hello_stage as hello_stage:
            print('hello_stage', hello_stage)
            if get_message_text == 'info' or get_message_text == 'order':
                send_message_text = STAGES[hello_stage]['message']
                user_storage.update_stage(chat_id, hello_stage)
            else:
                send_message_text = STAGES[hello_stage]['error_message']


    bot.send_message(chat_id, send_message_text, reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(admin_id, text='ghbdtnAoifhcn;zx')
