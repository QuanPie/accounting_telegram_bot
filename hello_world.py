# import telegram
# bot = telegram.Bot(token='5228328595:AAH35Qe5QSCyHKgJDNmWGv6JRrsB5CXjdaI')
# print(bot.get_me())

from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram import Update
import logging
from telegram.ext import Updater

updater = Updater(
    token='5228328595:AAH35Qe5QSCyHKgJDNmWGv6JRrsB5CXjdaI', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def hello(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="hello")


start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)

updater.start_polling()


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
