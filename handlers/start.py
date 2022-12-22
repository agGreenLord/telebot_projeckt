import telebot
from telebot import types

from config import BOT_TOKEN, ADMIN_CHAT_TOKEN
from state import Store, Record, ClientData
from mocked_data import HELLO_MESSAGE, STAGES, STAGES_TYPES



bot = telebot.TeleBot(BOT_TOKEN)
user_storage = Store()
admin_id = ADMIN_CHAT_TOKEN


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Info')
    btn2 = types.KeyboardButton('Order')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, HELLO_MESSAGE, reply_markup=markup)

    empty_client_data = ClientData('', '')
    record = Record(message.from_user.id, empty_client_data, STAGES_TYPES[0])
    user_storage.add_new_record(record)
    print(user_storage.storage)


@bot.message_handler(content_types=['text'])
def get_message(message):
    user_id = message.from_user.id
    get_message_text = message.text.lower()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Надо почитать про утечку памяти и как правильно с ней работать
    send_message_text = ' '

    print('current_stage', (user_storage.get_record_by_chat_id(user_id)).current_stage)
    print('STAGES_TYPES[0]' + STAGES_TYPES[0])

    match (user_storage.get_record_by_chat_id(user_id)).current_stage:
        case STAGES_TYPES[0]:
            if get_message_text == 'Info' or get_message_text == 'Order':
                send_message_text = STAGES[STAGES_TYPES[0]]['message']
                user_storage.update_stage(user_id, STAGES_TYPES[1])
            else:
                send_message_text = STAGES[STAGES_TYPES[0]]['error_message']
        # case STAGES_TYPES[1]:
        # case STAGES_TYPES[2]:




    bot.send_message(user_id, send_message_text, reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(admin_id, text='ghbdtnAoifhcn;zx')
