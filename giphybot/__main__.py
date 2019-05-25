import giphybot.bot

import requests
import telegram.ext

import logging
import os


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    updater = telegram.ext.Updater(token=os.environ["TELEGRAM_TOKEN"])
    giphybot.bot.configure_dispatcher(updater.dispatcher)

    updater.start_polling()


if __name__ == "__main__":
    main()
