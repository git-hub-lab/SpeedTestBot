#!/usr/bin/env python

import logging

from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from speedtestbot import speedtest_fun

from configs import Config

BOT_TOKEN = Config.BOT_TOKEN
START_TEXT = Config.START_TEXT
ABOUT_BOT_TEXT = Config.ABOUT_BOT_TEXT
HELP_TEXT = Config.HELP_TEXT
BOTCMDS = Config.BOTCMDS
START_BUTTON = InlineKeyboardMarkup(
	[
		[
		InlineKeyboardButton("Help", callback_data="help"),
		InlineKeyboardButton("About Bot", callback_data="aboutbot")
		]
	]
)
HELP_BUTTON = InlineKeyboardMarkup(
	[
		[
		InlineKeyboardButton("Home", callback_data="home"),
		InlineKeyboardButton("About Bot", callback_data="aboutbot")
		]
	]
)
ABOUT_BOT_BUTTON = InlineKeyboardMarkup(
	[
		[
		InlineKeyboardButton("Help", callback_data="help"),
		InlineKeyboardButton("Home", callback_data="home")
		]
	]
)



logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
	level=logging.INFO
)
logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start_fun(update, context):
	message = update.message
	logger.info('A User,  User Full Name:- "%s"; User Id:- "%s".', message.from_user.full_name, message.chat.id)
	message.reply_text(
		text=START_TEXT.format(message.from_user.full_name, message.chat.id),
		parse_mode=ParseMode.MARKDOWN,
		reply_markup=START_BUTTON
	)


def help_fun(update, context):
	message = update.message
	message.reply_text(
		text=HELP_TEXT,
		parse_mode=ParseMode.MARKDOWN,
		reply_markup=HELP_BUTTON
	)


def about_fun(update, context):
	message = update.message
	message.reply_text(
		text= ABOUT_BOT_TEXT,
		disable_web_page_preview=True,
		parse_mode=ParseMode.MARKDOWN,
		reply_markup=ABOUT_BOT_BUTTON
	)


def callbackquery_fun(update, context):
	callback_query = update.callback_query
	callback_query.answer()
	data = callback_query.data
	if data == "home":
		text=START_TEXT.format(callback_query.from_user.full_name, callback_query.from_user.id)
		button=START_BUTTON
	elif data == "help":
		text=HELP_TEXT
		button=HELP_BUTTON
	elif data == "aboutbot":
		text=ABOUT_BOT_TEXT
		button=ABOUT_BOT_BUTTON
	else:
		print(data)
	callback_query.edit_message_text(
		text=text,
		disable_web_page_preview=True,
		parse_mode=ParseMode.MARKDOWN,
		reply_markup=button
	)




def main():

	updater = Updater(BOT_TOKEN, use_context=True)
	bot = updater.bot
	dp = updater.dispatcher

	bot.set_my_commands(BOTCMDS)

	dp.add_handler(CommandHandler('start', start_fun))
	dp.add_handler(CommandHandler('about', about_fun))
	dp.add_handler(CommandHandler('help', help_fun))
	dp.add_handler(CommandHandler('speedtest', speedtest_fun))
	dp.add_handler(CallbackQueryHandler(callbackquery_fun))
	dp.add_error_handler(error)


	updater.start_polling()
	logger.info("Bot Started...")
	updater.idle()
	logger.info("Bot Stoped...")


if __name__ == '__main__':
    main()
