from telegram.ext import (
    Updater, CommandHandler, Filters, MessageHandler, ConversationHandler,
    CallbackQueryHandler, PicklePersistence)

from kiz_sushi_bot.bot import markups
from kiz_sushi_bot.bot.models import TelegramClient
from kiz_sushi_bot.bot.handlers.decorators import *


class CoreHandler:
    MENU_STATE = 1

    def get_core_handlers(self):
        return [
            CommandHandler('start', self.start),
        ]

    @core_handlers_decorator
    def get_main_menu_handlers(self):
        return [
            MessageHandler(
                Filters.regex(
                    '^Меню$'
                ), self.get_menu_page),
            MessageHandler(
                Filters.regex(
                    '^Про нас!$'
                ), self.get_about_info),
        ]

    @core_page_message_handler
    def start(self, update, context):
        chat = update.message.chat
        if TelegramClient.objects.filter(chat_id=chat.id).exists():
            self.render_main_page(update, context)
            return self.MENU_STATE
        user = update.message.from_user
        user_data = {
            'user_id': user.id,
            'first_name': user.first_name,
            'username': user.username,
            'chat_id': update.message.chat.id
        }
        client = TelegramClient(**user_data)
        client.save()
        update.message.reply_text(
            "Вас приветствует КИЗ Суши бот. Здесь вы можете посмотреть меню и заказать для себя вкусняшки!!!")
        self.render_main_page(update, context)
        return self.MENU_STATE

    def render_main_page(self, update, context):
        update.message.reply_text("Главное меню",
                                  parse_mode='HTML',
                                  reply_markup=markups.main_menu_markup())

    @simple_message_handler
    def undefined_cmd_msg(self, update, context):
        update.message.reply_text(
            'Я вас не понимаю. Попробуйте ввести команда /start',
            parse_mode='HTML', )

    def get_about_info(self, update, context):
        update.message.reply_text(
            "``` Ресторан по заказу еду  SUSHI 🔥KIZ 🔥PIZZA в КИЗе. "
            "Находимся по адресу ЕРЛЕПЕСОВА БАБАЕВА. "
            "Принимаем заказы с10:00 до 23:00(ежедневно).Номер телефона: +7471166232```",
            parse_mode='Markdown')
