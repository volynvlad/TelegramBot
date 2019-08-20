from config import *
from news import *
from weather import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # bot

import logging                      
import emoji


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('To know 🌧 weather type /weather <city>\n' +
                              'To know 📰 news type /news <source>\n' +
                              'For more information type /news_start or /weather_start')


def git(bot, update):
    update.message.reply_text('https://github.com/volynvlad')


def error(bot, update, error):
    logger.warning('Update {} caused error {}').format(update, error)


def main():
    updater = Updater(bot_token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("git", git))
    dp.add_handler(CommandHandler("weather_start", weather_start))
    dp.add_handler(CommandHandler("news_start", news_start))
    dp.add_handler(CommandHandler("news_help", news_help))
    dp.add_handler(CommandHandler("weather", weather, pass_args=True))
    dp.add_handler(CommandHandler("weather_help", weather_help))
    dp.add_handler(CommandHandler("news", news, pass_args=True))
    dp.add_handler(CommandHandler("sources", sources))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

