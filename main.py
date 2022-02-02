from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from key import TOKEN


def main():

    updater = Updater(
        token=TOKEN,
        use_context=True
    )
    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.all, echo)

    hello_handler = MessageHandler(Filters.text('Hello, hello'), say_hello)

    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    print('successful launch')
    updater.idle()


def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    id = update.message.chat_id
    name = update.message.from_user.first_name
    update.message.reply_text(f"Hello, {name}. Yours message {text}\n"
                              f'Yours id {id}')


def say_hello(update: Update, context: CallbackContext):
    name = update.message.from_user.first_name
    update.message.reply_text(f"Hello, {name}. I'm bot")


if __name__ == '__main__':
    main()
