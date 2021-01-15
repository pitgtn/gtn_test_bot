import telebot
import config
import random
from epic_free_games import epic

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
egn = epic()

# @bot.message_handler(commands=['ts'])
# def ts_msg(message):
# 	keyboard = types.InlineKeyboardMarkup()
# 	url_btn = types.InlineKeyboardButton(text = "Сервер Team Speak", url="ts3server://kstorage.ru")
# 	keyboard.add(url_btn)
# 	bot.send_message(message.chat.id, "Наш сервер", reply_markup=keyboard)
@bot.message_handler(commands=['ts'])
def ts_msg(message):
	bot.send_message(message.chat.id, "79.173.84.84 - адрес сервера TS3\n".format(message.from_user, bot.get_me()),
		parse_mode='html')



@bot.message_handler(commands=['help'])
def help_msg(message):
	bot.send_message(message.chat.id, "Список команд для бота <b>{1.first_name}</b>:\n/epic - бесплатная игра в Epic Store\n/ts - адрес сервера TS3\n".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(commands=['epic'])
def epic_msg(message):
	# egn = epic()
	bot.send_message(message.chat.id,"<b>{0.first_name}</b>, забирай:".format(message.from_user, bot.get_me()) + egn, parse_mode='html')

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html')


# RUN
bot.polling(none_stop=True)