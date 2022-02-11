from transliterate import to_latin, to_cyrillic
from mytoken import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет чувак (Salom ...).\n"
                          "Напиши что-нибудь ✍ (Biron nima yoz)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)

if __name__ == '__main__':
    bot.polling()