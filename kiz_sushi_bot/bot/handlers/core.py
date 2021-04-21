from telegram import ReplyKeyboardRemove
from telegram.ext import (
    Updater, CommandHandler, Filters, MessageHandler, ConversationHandler,
    CallbackQueryHandler, PicklePersistence)

from .. import markups
from ..models import TelegramClient
from .decorators import *


class CoreHandler:
    """
       Handler for bot configs and core methods like start, stop, authorize
       """
    # Core states
    BASE_STATE, MENU_STATE, BASKET_STATE, ORDER_HISTORY_STATE, MANAGER_STATE = range(100, 105)

    def get_core_handlers(self):
        return [
            CommandHandler('start', self.start),
        ]

    def get_base_handlers(self):
        return [
            MessageHandler(
                Filters.regex(
                    f'^({self.reply_manager.get_message("menu_button")})$'
                ), self.menu_page)
        ]

    def get_auth_handlers(self):
        return [
            MessageHandler(Filters.contact, self.authorize),
            MessageHandler(Filters.text, self.authorize)
        ]

    @core_handlers_decorator
    def get_main_menu_handlers(self):
        return [
            MessageHandler(
                Filters.regex(
                    f'^({self.reply_manager.get_message("menu_button")})$'
                ), self.menu_page),
            # MessageHandler(
            #     Filters.regex(
            #         f'^({self.reply_manager.get_message("my_offers_button")})$'
            #     ), self.offers_page),
            # MessageHandler(
            #     Filters.regex(
            #         f'^({self.reply_manager.get_message("news_button")})$'
            #     ), self.news_page),
            # MessageHandler(
            #     Filters.regex(
            #         f'^({self.reply_manager.get_message("my_contracts_button")})$'
            #     ), self.payments_page),
            # CallbackQueryHandler(self.accept_offer, pattern='^accept_offer_(default|history)_(-?[0-9]+)$'),
            # CallbackQueryHandler(self.reject_offer, pattern='^reject_offer_(default|history)_(-?[0-9]+)$'),
        ]

    @core_page_message_handler
    def start(self, update, context):
        """Send a message when the command /start is called."""
        chat = update.message.chat
        if TelegramClient.objects.filter(chat_id=chat.id).exists():
            client = TelegramClient.objects.get(chat_id=chat.id)
            self.render_main_page(update, context)
            return self.MAIN_MENU_STATE
        user = update.message.from_user
        user_data = {
            'user_id': user.id,
            'first_name': user.first_name,
            'is_bot': user.is_bot,
            'username': user.username,
            'chat_id': update.message.chat.id
        }
        client = TelegramClient(**user_data)
        client.save()
        msg = update.message.reply_text(
            text=self.reply_manager.get_message('welcome_reply'),
            parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove())
        return self.BASE_STATE

    def render_main_page(self, update, context):
        # self.clear_messages(context, update.message.chat.id, all=True)
        msg = update.message.reply_text(
            self.reply_manager.get_message('get_base_text'),
            parse_mode='HTML',
            reply_markup=markups.main_menu_markup())

    @simple_message_handler
    def authorize(self, update, context):
        contact = update.message.contact
        if contact:
            phone_number = contact.phone_number
        else:
            phone_number = update.message.text
        if phone_number[0] != '+':
            phone_number = f"+{phone_number}"

        # chat_id = update.message.chat.id
        # try:
        #     phonenumbers.parse(phone_number, None)
        # except NumberParseException as e:
        #     msg = update.message.reply_text(
        #         self.reply_manager.get_message('phone_prompt_reply'), parse_mode='HTML', )
        #     self.add_message_to_history(context, msg)
        #     return
        #
        # try:
        #     sms_code = send_otp(phone_number)
        #     context.user_data['auth_sms_code'] = sms_code
        # except:
        #     pass
        #
        # context.user_data['phone'] = phone_number
        # msg = update.message.reply_text(
        #     text=f'{self.reply_manager.get_message("sms_code_prompt_reply")}',
        #     parse_mode='HTML',
        #     reply_markup=ReplyKeyboardRemove()
        # )
        # self.add_message_to_history(context, msg)
        return self.AUTH_SMS_STATE
