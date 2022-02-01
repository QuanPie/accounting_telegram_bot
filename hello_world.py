# import telegram
# bot = telegram.Bot(token='5228328595:AAH35Qe5QSCyHKgJDNmWGv6JRrsB5CXjdaI')
# print(bot.get_me())

from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))


updater = Updater('5228328595:AAH35Qe5QSCyHKgJDNmWGv6JRrsB5CXjdaI')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
