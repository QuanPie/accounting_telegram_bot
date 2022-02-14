#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging

from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    """send start message"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="This is a accounting bot, send /help to know more")


def help(update: Update, context: CallbackContext):
    """send message of help"""
    """
        help - See list of support commands
        start - See inital message
        new - Add new item
        history - See history
        version - Show bot version and details
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="/help - See list of support commands\n"
        "/start - See inital message\n"
        "/new - Add new item\n"
        "/history - See history\n"
        "/version - Show bot version and details\n"
    )


def main():
    # creat updater and pass it your bot's token
    updater = Updater(token='5228328595:AAH35Qe5QSCyHKgJDNmWGv6JRrsB5CXjdaI')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    # start the bot
    updater.start_polling()


if __name__ == "__main__":
    main()
