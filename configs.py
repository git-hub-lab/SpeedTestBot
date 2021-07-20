import os

from telegram import BotCommand


class Config(object):
	BOT_TOKEN = os.environ.get('TOKEN')
	BOT_USERNAME = "xvarna279bot"
	START_TEXT =  "Hi, [{}](tg://user?id={}), I'm Speed Test Bot. \nCheck The /help For More Info."
	HELP_TEXT = """*Help menu!*\n
Command available:
`/speedtest` -  Run Speed Test."""
	ABOUT_BOT_TEXT = f"""
*About Menu!*

 A Telegram Bot Which Returns Clients Current Download / Upload Network Speed!

🤖 *My Name:* [Speed Test Bot](https://t.me/{BOT_USERNAME})

📝 *Language:* [Python3](https://www.python.org)

📚 *Library:* [Python Telegram Bot](https://python-telegram-bot.org/)

📡 *Hosted on:* [Heroku](https://heroku.com)

🧑🏻‍💻 *Developer:* @VarnaX

👥 *Support Group:* [abc](https://t.me/abc)

📢 *Updates Channel:* [ABC](https://t.me/ABC)
"""
	
	BOTCMDS = [
	BotCommand('start', 'Start Bot'),
	BotCommand('help','Get Help'),
	BotCommand('about','About Bot'),
	BotCommand('speedtest','Run Speed Test'),
	]
