import logging
import telebot


TOKEN = "5827639233:AAFoJXxbXJ9oWtsL9nIuVbaOEK35apz79AI"
logging.basicConfig(level=logging.INFO)


# def telegram_bot(token):
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hello')

bot.polling()

# if __name__ == '__main__':
#     telegram_bot(TOKEN)