import telegram
from django.core.management import BaseCommand
from telegram import Update
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackContext

from kiz_sushi_bot.bot.models import Chat, TelegramUser


def do_echo(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    reply_text = "ID = {}".format(chat_id)
    update.message.reply_text(text=reply_text)


def do_count(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p = TelegramUser.objects.count()
    print(p)
    update.message.reply_text(text=p)


class Command(BaseCommand):

    def handle(self, *args, **options):
        bot = telegram.Bot(token='1240576397:AAH-iQqaDhxy3I6BarVbuW3FHoa8emlBQTM')
        print(bot.getMe())
        updater = Updater(bot=bot, use_context=True)

        message_handler2 = CommandHandler('count', do_count)
        updater.dispatcher.add_handler(message_handler2)

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)
        updater.start_polling()
        updater.idle()
