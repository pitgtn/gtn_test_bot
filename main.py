from telebot import TeleBot
from config import TOKEN
from libs.epic_query_lib import query_epic_games
import time
from datetime import datetime
import os


bot = TeleBot(TOKEN)
directory_path = os.getcwd()

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
	games = query_epic_games(cached_game_infos)
	pretty = ""
	for game in games:
		pretty += game.pretty_print_me()

	bot.send_message(message.chat.id,"<b>{0.first_name}</b>, забирай:".format(message.from_user, bot.get_me()) + pretty, parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open(f'{directory_path}/static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html')


def run_bot():
	try:
		bot.polling(none_stop=True, timeout=120)
	except Exception as e:
		current_date = datetime.now().date()
		with open(f'{directory_path}/log_bot_{current_date}.txt', 'a') as f:
			f.write(f'{e} \n')
		f.close()
		time.sleep(5)
	run_bot()


if __name__ == '__main__':
	cached_game_infos = query_epic_games([])
	run_bot()

