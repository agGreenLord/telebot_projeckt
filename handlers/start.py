import re

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

    income_message_text = message.text.lower()

    user_storage.delete_record(chat_id)
    empty_client_data = ClientData(message.from_user.username, '', '')
    record = Record(chat_id, empty_client_data, StageList.start_stage)
    user_storage.add_new_record(record)

    send_staged_message(chat_id, user_storage, income_message_text)


@bot.message_handler(content_types=['text'])
def get_message(message):
    chat_id = message.chat.id

    income_message_text = message.text.lower()

    send_staged_message(chat_id, user_storage, income_message_text)


@bot.message_handler(commands=['admin'])
def admin(message):
    bot.send_message(admin_id, text='ghbdtnAoifhcn;zx')


def send_staged_message(chat_id: str, storage: Store, income_message: str):
    current_stage_name = storage.get_record_by_chat_id(chat_id).current_stage
    current_stage = STAGES[current_stage_name]
    income_message = income_message.lower()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    message_to_send = \
        'Произошла непридвиденная ошибка, работы по устранению уже ведутся.\n\n Попробуйте написать позже'
    is_error = False

    match current_stage_name:
        case StageList.start_stage:

            next_stage = STAGES[StageList.hello_stage]
            message_to_send = next_stage['message']

            if next_stage['buttons']:
                for service in next_stage['buttons']:
                    markup.add(types.KeyboardButton(service))

            user_storage.update_stage(chat_id, StageList.hello_stage)

        case StageList.hello_stage:

            match income_message:
                case 'info':
                    message_to_send = 'У нас нет этого этапа'

                case 'order':
                    next_stage = STAGES[StageList.choose_service_stage]
                    message_to_send = next_stage['message']

                    if next_stage['buttons']:
                        for service in next_stage['buttons']:
                            markup.add(types.KeyboardButton(service))
                    else:
                        markup = telebot.types.ReplyKeyboardRemove()

                    user_storage.update_stage(chat_id, StageList.choose_service_stage)

                case _:
                    bot.send_message(chat_id, message_to_send, reply_markup=markup)
                    user_storage.update_stage(chat_id, StageList.start_stage)
                    send_staged_message(chat_id, storage, '/start')
                    is_error = True

        case StageList.choose_service_stage:

            match income_message:
                case 'электроника' | 'бытовая техника' | 'проводка':
                    next_stage = STAGES[StageList.get_phone_stage]
                    message_to_send = next_stage['message']

                    if next_stage['buttons']:
                        for service in next_stage['buttons']:
                            markup.add(types.KeyboardButton(service))
                    else:
                        markup = telebot.types.ReplyKeyboardRemove()

                    user_storage.update_stage(chat_id, StageList.get_phone_stage)
                    user_storage.update_service(chat_id, income_message)

                case _:
                    bot.send_message(chat_id, message_to_send, reply_markup=markup)
                    user_storage.update_stage(chat_id, StageList.start_stage)
                    send_staged_message(chat_id, storage, '/start')
                    is_error = True

        case StageList.get_phone_stage:

            next_stage = STAGES[StageList.finish_stage]

            print(' 10 <= len(income_message) <= 1',  10 <= len(income_message) <= 12)
            # print('re.findall(r"\A(1|8|9)[0-9]+", income_message)', re.findall(r"\A(1|8|9)[0-9]+", income_message))
            # print('len(re.findall(r"\A(1|8|9)[0-9]+", income_message))', len(re.findall(r"\A(1|8|9)[0-9]+", income_message)))
            # print('len(re.findall(r"\A(1|8|9)[0-9]+", income_message)) and 10 <= len(income_message) <= 12', len(re.findall(r"\A(1|8|9)[0-9]+", income_message)) and 10 <= len(income_message) <= 12)

            if len(re.findall(r"^[0-9]+$", income_message)) and 10 <= len(income_message) <= 12:
                message_to_send = next_stage['message']

                if next_stage['buttons']:
                    for service in next_stage['buttons']:
                        markup.add(types.KeyboardButton(service))
                else:
                    markup = telebot.types.ReplyKeyboardRemove()

                user_storage.update_stage(chat_id, StageList.finish_stage)
                user_storage.update_phone(chat_id, income_message)
                send_message_to_admin(chat_id, storage)
            else:
                message_to_send = "Номер не подходит\n" + current_stage['message']

        case StageList.finish_stage:

            next_stage = STAGES[StageList.hello_stage]
            message_to_send = next_stage['message']

            if next_stage['buttons']:
                for service in next_stage['buttons']:
                    markup.add(types.KeyboardButton(service))
            else:
                markup = telebot.types.ReplyKeyboardRemove()

            user_storage.update_stage(chat_id, StageList.hello_stage)

    if not is_error:
            bot.send_message(chat_id, message_to_send, reply_markup=markup)


def send_message_to_admin(chat_id: str, storage: Store):
    user_info = storage.get_record_by_chat_id(chat_id).data
    message = "Новый заказ \nНик пользователя: @" \
              + user_info.nick_name \
              + "\nНомер телефона пользователя: " + user_info.phone_number \
              + "\nВид услуги: " + user_info.selected_service
    print('message', message)
    bot.send_message(admin_id, text=message)
