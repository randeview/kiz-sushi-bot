import telegram
from django.conf import settings
from django.core.management import BaseCommand
from telegram import Update
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackContext

from ...bot import BotUpdater


class Command(BaseCommand):

    def handle(self, *args, **options):
        token = settings.BOT_TOKEN
        updater = BotUpdater(token=token)
        bot = updater.bot
        url = f"https://2b35-37-99-33-82.ngrok.io/api/webhook/client/{token}/"
        bot.set_webhook(url)
