from telegram import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

from kiz_sushi_bot.bot.models import TelegramReplyTemplate

reply_manager = TelegramReplyTemplate


def start_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(reply_manager.get_message('share_phone_button'), request_contact=True)]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup


def main_menu_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(reply_manager.get_message('my_profile_button')),
            KeyboardButton(reply_manager.get_message('my_offers_button')),
        ],
        [
            KeyboardButton(reply_manager.get_message('news_button')),
            KeyboardButton(reply_manager.get_message('my_contracts_button')),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup
