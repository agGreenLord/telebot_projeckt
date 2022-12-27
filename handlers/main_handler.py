import telebot

from config import BOT_TOKEN
from reducers import send_staged_message
from state import Store, Record, ClientData
from mocked_data import StageList

bot = telebot.TeleBot(BOT_TOKEN)
user_storage = Store()


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    income_message_text = message.text.lower()

    user_storage.delete_record(chat_id)
    empty_client_data = ClientData(message.from_user.username, '', '')
    record = Record(chat_id, empty_client_data, StageList.start_stage)
    user_storage.add_new_record(record)

    send_staged_message(chat_id, income_message_text, user_storage, bot)


@bot.message_handler(content_types=['text'])
def get_message(message):
    chat_id = message.chat.id

    income_message_text = message.text.lower()

    send_staged_message(chat_id, income_message_text, user_storage, bot)



