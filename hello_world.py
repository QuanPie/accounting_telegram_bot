#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    """send start message and show reply keyboard"""
    reply_keyboard = [
        ['💸 Expense', '💰 Income'],
        ['⚖️ Balance', '🗂 History'],
        ['🐞\n Report', '✉️ Feedback', '🚩 Version', '⚙️\nSetting'],
    ]
    reply_markup = ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    update.message.reply_text(
        'Welcome this is a accounting bot, send /help to know more', reply_markup=reply_markup)


def help(update: Update, context: CallbackContext):
    """send message of help"""
    """ for copy
help - See list of support commands
start - See inital message
history - See history
version - Show bot version and details
expense - 💸 expense
income - 💰 income
balance - balance
chart - statistic chart (pie,lin.bar...)
feedback - Send us feedback
report - Report bug
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="/help - See list of support commands\n"
        "/start - See inital message\n"
        "/history - See history\n"
        "/version - Show bot version and details\n"
        "/expense - Expense\n"
        "/income - Income\n"
        "/balance - Balance\n"
        "/feedback - Send us feedback\n"
    )


def version(update: Update, context: CallbackContext):
    """send version infomation and detail"""
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Bot version - 1.0.0\n\n"
        "New feature:\n"
        "- add function of bot version"
    )


def expense(update: Update, context: CallbackContext):

    keyboard = [
        [
            InlineKeyboardButton("Food", callback_data="food"),
            InlineKeyboardButton("Cloth", callback_data="cloth"),
            InlineKeyboardButton("Health", callback_data="health"),
        ],
        [
            InlineKeyboardButton("Live", callback_data="live"),
            InlineKeyboardButton(
                "Transportation", callback_data="transportation"),
            InlineKeyboardButton("Others", callback_data="others"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(
        text=f"How much did you cost on {query.data}? (enter the number)")


def main():
    # creat updater and pass it your bot's token
    updater = Updater(token='5228328595:AAH35Qe5QSCyHKgJDNmWGv6JRrsB5CXjdaI')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('version', version))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.regex('💸 Expense'), expense))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # start the bot
    updater.start_polling()


if __name__ == "__main__":
    main()
