from .decorators import *
from ..models import TelegramClient
from kiz_sushi_bot.main.models import FastFood


class MenuHandler:
    @main_menu_handlers_decorator
    def get_menu_handlers(self):
        return [

        ]

    @core_page_message_handler
    def menu_page(self, update, context):
        chat = update.message.chat
        client = TelegramClient.objects.get(chat_id=chat.id)
        foods = FastFood.objects.first()
        msg = update.message.reply_text(foods.title, parse_mode='HTML')
        return self.MENU_STATE
