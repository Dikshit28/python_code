import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext, conversationhandler,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

ECHO = range(1)


def start(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(
        'Hi! My name is IEEE Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'You can ask me your doubts',
    )

    return ECHO


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    if "benifits" in str(update.message.text):
        update.message.reply_text("BENIFITS OF IEEE")
    else:
        update.message.reply_text(update.message.text)


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope I was helpful!!!', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1499954995:AAFGlqP8E3PYA_vCACIDcgVdJwgaeFlnABA", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ECHO: [MessageHandler(
                Filters.text & ~Filters.command, echo)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]

    )

    dispatcher.add_handler(conv_handler)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
