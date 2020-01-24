# -*- coding: utf8 -*-
import telebot;
bot = telebot.TeleBot('1073569587:AAHU8xzJx_PCAP9k-8Kj6V0veAqYGeFCV0I');

# Подключаем модуль случайных чисел 
import random

# Если число введено верно — выдаём гороскоп
if 0 < zodiac < 13:
    print(random.choice(first), random.choice(second), random.choice(second_add), random.choice(third))
else:
    print("Вы ошиблись с числом, запустите программу ещё раз")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)