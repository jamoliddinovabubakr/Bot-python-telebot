"""
import datatime
x = datetime.datetime.now()
print(x.strftime("%x %X"))
#https://www.w3schools.com/python/python_datetime.asp
"""

import datetime
import telebot
from telebot import types

bot = telebot.TeleBot('5513508050:AAGNMdArFWrkXY_K1ZzQZI-4G3bgFg3q7dc')

name = ''
group = ''
time_input = 0
time_output = 0
loc = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Введите фамилия и имя: ")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text

    if message.text == '/start':
        bot.register_next_step_handler(message, get_name)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # ПМиИ
        btn_M_18_1 = types.KeyboardButton("M1-18")
        btn_M_18_2 = types.KeyboardButton("M2-18")
        btn_M_19_1 = types.KeyboardButton("M1-19")
        btn_M_19_2 = types.KeyboardButton("M2-19")
        btn_M_20_1 = types.KeyboardButton("M1-20")
        btn_M_20_2 = types.KeyboardButton("M2-20")
        btn_M_20_3 = types.KeyboardButton("M3-20")
        btn_M_21_1 = types.KeyboardButton("M1-21")
        btn_M_21_2 = types.KeyboardButton("M2-21")
        # Психология
        btn_P_18_1 = types.KeyboardButton("П1-18")
        btn_P_18_2 = types.KeyboardButton("П2-18")
        btn_P_19_1 = types.KeyboardButton("П1-19")
        btn_P_19_2 = types.KeyboardButton("П2-19")
        btn_P_20_1 = types.KeyboardButton("П1-20")
        btn_P_20_2 = types.KeyboardButton("П2-20")
        btn_P_20_3 = types.KeyboardButton("П3-20")
        btn_P_21_1 = types.KeyboardButton("П1-21")
        btn_P_21_2 = types.KeyboardButton("П2-21")

        btn_F_20_1 = types.KeyboardButton("Ф1-20")
        btn_F_20_2 = types.KeyboardButton("Ф2-20")
        btn_F_21_1 = types.KeyboardButton("Ф1-21")
        btn_F_21_2 = types.KeyboardButton("Ф2-21")

        btn_R_20_1 = types.KeyboardButton("Р1-20")
        btn_R_20_2 = types.KeyboardButton("Р2-20")
        btn_R_21_1 = types.KeyboardButton("Р1-21")
        btn_R_21_2 = types.KeyboardButton("Р2-21")

        markup.add(btn_M_18_1, btn_M_18_2)
        markup.add(btn_M_19_1, btn_M_19_2)
        markup.add(btn_M_20_1, btn_M_20_2, btn_M_20_3)
        markup.add(btn_M_21_1, btn_M_21_2)

        markup.add(btn_P_18_1, btn_P_18_2)
        markup.add(btn_P_19_1, btn_P_19_2)
        markup.add(btn_P_20_1, btn_P_20_2, btn_P_20_3)
        markup.add(btn_P_21_1, btn_P_21_2)

        markup.add(btn_F_20_1, btn_F_20_2)
        markup.add(btn_F_21_1, btn_F_21_2)

        markup.add(btn_R_20_1, btn_R_20_2)
        markup.add(btn_R_21_1, btn_R_21_2)

        bot.send_message(message.chat.id, text="Какая группа?", reply_markup=markup)
        bot.register_next_step_handler(message, location)


@bot.message_handler(content_types=['text'])
def location(message):
    global group
    if message.text != "возвращаться в главную меню":
        group = message.text
        # print(group, end="\t")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("чт")
    btn2 = types.KeyboardButton("видео зал")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="выбирайте место", reply_markup=markup)
    bot.register_next_step_handler(message, intput_func)


def intput_func(message):
    global loc
    loc = message.text
    if message.text == "чт" or message.text == "видео зал":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("вход")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="правила в библиотеке!", reply_markup=markup)
        bot.register_next_step_handler(message, output_func)


def output_func(message):
    if message.text == "вход":
        global time_input
        time_input = datetime.datetime.now()

        print(time_input.strftime("%x"), end='\t')
        print(name, end='\t')
        print(group, end='\t')
        print(loc, end='\t')
        print(time_input.strftime("%X"), end='\t')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("выход")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="хорошего чтения!", reply_markup=markup)
        bot.register_next_step_handler(message, out)


def out(message):
    if message.text == "выход":
        global time_output
        time_output = datetime.datetime.now()

        print(time_output.strftime("%X"))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("возвращаться в главную меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="пж не оставляейте свои вещи(если есть мусор бросайте на ведро)!", reply_markup=markup)
        bot.register_next_step_handler(message, location)


bot.polling(none_stop=True)
