from telegram import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

from kiz_sushi_bot.bot.models import TelegramReplyTemplate
from kiz_sushi_bot.main.models import FoodType

reply_manager = TelegramReplyTemplate
menu_emoji = u'\U00002712'
about_us = u'\U00002b50'
basket_emoji = u'\U00002b55'
thunderstorm = u'\U00002744'


def main_menu_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton('Меню'),
        ],
        [
            KeyboardButton('Про нас!'),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return markup


def food_menu_markups() -> ReplyKeyboardMarkup:
    keyboard = []
    for category in FoodType.objects.all():
        keyboard.append([KeyboardButton(category.title + u'\U0001F464')])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
