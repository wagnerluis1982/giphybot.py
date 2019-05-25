from . import giphy


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm gif bot, call me with /random")


def random(bot, update, args):
    bot.send_animation(update.message.chat_id, animation=giphy.random(''.join(args)))


def configure_dispatcher(dispatcher):
    import telegram.ext

    start_handler = telegram.ext.CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    random_handler = telegram.ext.CommandHandler('random', random, pass_args=True)
    dispatcher.add_handler(random_handler)
