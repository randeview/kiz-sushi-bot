import os

from django.conf import settings
from telegram import BotCommand
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, PicklePersistence

from .handlers import *
from .models import TelegramReplyTemplate


class BotUpdater(CoreHandler, MenuHandler, Updater):
    def __init__(self, token, *args, **kwargs):
        persistence_file = os.path.join(settings.MEDIA_ROOT, 'persistence_files/{}'.format(token))
        persistence = PicklePersistence(filename=persistence_file)
        super(BotUpdater, self).__init__(token, persistence=persistence, use_context=True, *args, **kwargs)
        self.set_commands()
        self.reply_manager = TelegramReplyTemplate
        dp = self.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', self.start)],
            states={
                self.MENU_STATE: self.get_main_menu_handlers(),
            },
            fallbacks=[
                CommandHandler('start', self.start)],
            persistent=True,
            name='client_conversation'
        )

        dp.add_handler(conv_handler)
        dp.add_handler(MessageHandler(Filters.text, self.undefined_cmd_msg))

    def set_commands(self):
        bot = self.bot
        commands_raw = [
            {'command': 'start', 'description': 'Начать общение с ботом'}
        ]
        bot.set_my_commands([BotCommand(**comm) for comm in commands_raw])
