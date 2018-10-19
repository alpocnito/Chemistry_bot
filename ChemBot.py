from bs4 import BeautifulSoup
import logging
import requests
import telegram
from telegram.ext import *

class User():
    AO_i = 0
    S_i = 0
    O_i = 0
    OVR_i = 0
    chat_id = ""
    state = ""
    def __init__(self, chat_id):
        self.chat_id = chat_id


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater('664984655:AAHB7LtkwYySAz1-BIWravV1TfmZ8odvlXo')
dispatcher = updater.dispatcher
job_queue = updater.job_queue
url = "http://chemequations.com/ru/"
headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
user_list = dict()
custom_keyboard = [['Амфотерные основания', 'Соли'], ['Оксиды', 'ОВР']]
AO_list = ['Cr(OH)3 + HCl = ?', 'CrCl3+3H2O', 'ZnCl2 + NaOH = ?', 'Zn(OH)2+2NaCl', 'Al(OH)3 + H2SO4 = ?', 'Al2(SO4)3+6H2O']
S_list = ['KOH + HBr = ?', 'KBr+H2O', 'HF + LiOH = ?', 'H2O+LiF', 'NaOH + H2SO4 = ?', 'Na2SO4+2H2O']
O_list = ['Li2O + H2O = ?', '2LiOH+O2', 'ZnO + 2HCl = ?', 'ZnCl2+H2O', 'ZnO + H2O = ?', 'Zn(OH)2']
OVR_list = ['H2O2 + KMnO4 + H2SO4 = ?', 'K2SO4+2MnSO4+8H2O+5O2', 'P + HNO3 + H2O = ?', '5NO+3H3PO4', 'K2Cr2O7 + HCl = ?', '2KCl+2CrCl3+7H2O+3Cl2']

def start(bot, update):
    u = User(update.message.chat_id)
    user_list[update.message.chat_id] = u
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, text="Выберите тему или просто введите уравнение",  reply_markup=reply_markup)

def echo(bot, update):
    if update.message.text == 'Сдаюсь':
        if  user_list[update.message.chat_id].state == "AO":
            bot.send_message(update.message.chat_id, "Правильный ответ: " + AO_list[user_list[update.message.chat_id].AO_i])
            user_list[update.message.chat_id].AO_i += 1
            user_list[update.message.chat_id].AO_i %= 6
            bot.send_message(update.message.chat_id,  AO_list[user_list[update.message.chat_id].AO_i])
            user_list[update.message.chat_id].AO_i += 1
            user_list[update.message.chat_id].AO_i %= 6
        if  user_list[update.message.chat_id].state == "S":
            bot.send_message(update.message.chat_id, "Правильный ответ: " + S_list[user_list[update.message.chat_id].S_i])
            user_list[update.message.chat_id].S_i += 1
            user_list[update.message.chat_id].S_i %= 6
            bot.send_message(update.message.chat_id,  S_list[user_list[update.message.chat_id].S_i])
            user_list[update.message.chat_id].S_i += 1
            user_list[update.message.chat_id].S_i %= 6
        if  user_list[update.message.chat_id].state == "O":
            bot.send_message(update.message.chat_id, "Правильный ответ: " + O_list[user_list[update.message.chat_id].O_i])
            user_list[update.message.chat_id].O_i += 1
            user_list[update.message.chat_id].O_i %= 6
            bot.send_message(update.message.chat_id,  O_list[user_list[update.message.chat_id].O_i])
            user_list[update.message.chat_id].O_i += 1
            user_list[update.message.chat_id].O_i %= 6
        if  user_list[update.message.chat_id].state == "OVR":
            bot.send_message(update.message.chat_id, "Правильный ответ: " + OVR_list[user_list[update.message.chat_id].OVR_i])
            user_list[update.message.chat_id].OVR_i += 1
            user_list[update.message.chat_id].OVR_i %= 6
            bot.send_message(update.message.chat_id,  OVR_list[user_list[update.message.chat_id].OVR_i])
            user_list[update.message.chat_id].OVR_i += 1
            user_list[update.message.chat_id].OVR_i %= 6
        return
    if update.message.text == 'Выйти':
        user_list[update.message.chat_id].state = ""
        user_list[update.message.chat_id].AO_i = 0
        user_list[update.message.chat_id].S_i = 0
        user_list[update.message.chat_id].O_i = 0
        user_list[update.message.chat_id].OVR_i = 0
        custom_keyboard = [['Амфотерные основания', 'Соли'], ['Оксиды', 'ОВР']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id, text="Выберите тему или просто введите уравнение",  reply_markup=reply_markup)
        return
    if update.message.text == 'Амфотерные основания':
        custom_keyboard = [['Сдаюсь'], ['Выйти']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
        user_list[update.message.chat_id].state = "AO"
        bot.send_message(update.message.chat_id, "Вводите ответ без пробелов и со всеми индексами, например: CrCl3+3H2O")
        bot.send_message(update.message.chat_id, AO_list[user_list[update.message.chat_id].AO_i],  reply_markup=reply_markup)
        user_list[update.message.chat_id].AO_i += 1
        return
    if update.message.text == 'Соли':
        custom_keyboard = [['Сдаюсь'], ['Выйти']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
        user_list[update.message.chat_id].state = "S"
        bot.send_message(update.message.chat_id, "Вводите ответ без пробелов и со всеми индексами, например: CrCl3+3H2O")
        bot.send_message(update.message.chat_id, S_list[user_list[update.message.chat_id].S_i],  reply_markup=reply_markup)
        user_list[update.message.chat_id].S_i += 1
        return
    if update.message.text == 'Оксиды':
        custom_keyboard = [['Сдаюсь'], ['Выйти']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
        user_list[update.message.chat_id].state = "O"
        bot.send_message(update.message.chat_id, "Вводите ответ без пробелов и со всеми индексами, например: CrCl3+3H2O")
        bot.send_message(update.message.chat_id, O_list[user_list[update.message.chat_id].O_i],  reply_markup=reply_markup)
        user_list[update.message.chat_id].O_i += 1
        return
    if update.message.text == 'ОВР':
        custom_keyboard = [['Сдаюсь'], ['Выйти']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
        user_list[update.message.chat_id].state = "OVR"
        bot.send_message(update.message.chat_id, "Вводите ответ без пробелов и со всеми индексами, например: CrCl3+3H2O")
        bot.send_message(update.message.chat_id, OVR_list[user_list[update.message.chat_id].OVR_i],  reply_markup=reply_markup)
        user_list[update.message.chat_id].OVR_i += 1
        return
    if user_list[update.message.chat_id].state == "AO":
        if update.message.text != AO_list[user_list[update.message.chat_id].AO_i]:
            bot.send_message(update.message.chat_id, "Попробуй еще раз")
        else:
            bot.send_message(update.message.chat_id, "Молодец, правильно")
            user_list[update.message.chat_id].AO_i += 1
            user_list[update.message.chat_id].AO_i %= 6
            bot.send_message(update.message.chat_id, AO_list[user_list[update.message.chat_id].AO_i])
            user_list[update.message.chat_id].AO_i += 1
            user_list[update.message.chat_id].AO_i %= 6
        return
    if user_list[update.message.chat_id].state == "S":
        if update.message.text != S_list[user_list[update.message.chat_id].S_i]:
            bot.send_message(update.message.chat_id, "Попробуй еще раз")
        else:
            bot.send_message(update.message.chat_id, "Молодец, правильно")
            user_list[update.message.chat_id].S_i += 1
            user_list[update.message.chat_id].S_i %= 6
            bot.send_message(update.message.chat_id, S_list[user_list[update.message.chat_id].S_i])
            user_list[update.message.chat_id].S_i += 1
            user_list[update.message.chat_id].S_i %= 6
        return
    if user_list[update.message.chat_id].state == "O":
        if update.message.text != O_list[user_list[update.message.chat_id].O_i]:
            bot.send_message(update.message.chat_id, "Попробуй еще раз")
        else:
            bot.send_message(update.message.chat_id, "Молодец, правильно")
            user_list[update.message.chat_id].O_i += 1
            user_list[update.message.chat_id].O_i %= 6
            bot.send_message(update.message.chat_id, O_list[user_list[update.message.chat_id].O_i])
            user_list[update.message.chat_id].O_i += 1
            user_list[update.message.chat_id].O_i %= 6
        return
    if user_list[update.message.chat_id].state == "OVR":
        if update.message.text != OVR_list[user_list[update.message.chat_id].OVR_i]:
            bot.send_message(update.message.chat_id, "Попробуй еще раз")
        else:
            bot.send_message(update.message.chat_id, "Молодец, правильно")
            user_list[update.message.chat_id].OVR_i += 1
            user_list[update.message.chat_id].OVR_i %= 6
            bot.send_message(update.message.chat_id, OVR_list[user_list[update.message.chat_id].OVR_i])
            user_list[update.message.chat_id].OVR_i += 1
            user_list[update.message.chat_id].OVR_i %= 6
        return

    s = update.message.text
    ans = ""
    for a in s:
        if a == ' ':
            ans += '+'
        if a == '+':
            ans += '%2B'
        else:
            ans += a

    res = requests.get(url + '?s=' + ans + '&k=1', headers=headers).content
    soup = BeautifulSoup(res, 'html.parser')
    soup = soup.h1
    mes = ""
    #print(soup)
    for link in soup.find_all(['span', 'sub']):
        if link.get("class") != ["compound"] and link.get("class") != ["group"] and link.get("class") != ["charge"]:
            mes += link.text

    bot.send_message(update.message.chat_id, mes, parse_mode=telegram.ParseMode.HTML)


dispatcher.add_handler(MessageHandler (Filters.text, echo))
dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()