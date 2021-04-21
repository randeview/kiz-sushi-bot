from telegram import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

from kiz_sushi_bot.bot.models import TelegramReplyTemplate

reply_manager = TelegramReplyTemplate
menu_emoji = u'\U00002712'
about_us = u'\U00002b50'
basket_emoji = u'\U00002b55'
thunderstorm = u'\U00002744'


def start_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(reply_manager.get_message('share_phone_button'), request_contact=True)]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup


def main_menu_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(reply_manager.get_message('menu_button')),
            KeyboardButton(reply_manager.get_message('basket_button') + basket_emoji),
        ],
        [
            KeyboardButton(reply_manager.get_message('about_us_button') + about_us),
            KeyboardButton(reply_manager.get_message('my_order_button') + thunderstorm),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup
