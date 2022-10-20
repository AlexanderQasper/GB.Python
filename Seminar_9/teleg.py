from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from random import randint

bot_token = "5732215283:AAEK4rDutfCc6OPsXZZPFGw0CEITWTV5UiE"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(Update.effective_chat.id, "Привет!")

start_handler = CommandHandler('start', start)

def info(update, context):
    context.bot.send_message(Update.effective_chat.id, "это бот")

def roll(update, context):
    context.bot.send_message(Update.effective_chat.id, text=str(randint(1, 6)))

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
roll_handler = CommandHandler('roll', roll)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(roll_handler)
updater.start_polling()
updater.idle()
