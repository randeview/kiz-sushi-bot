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
    temporary_list = []
    for index, category in enumerate(FoodType.objects.all()):
        temporary_list.append(KeyboardButton(category.title))
        if index % 2 == 0:
            keyboard.append(temporary_list)
            temporary_list = []
    keyboard.append([KeyboardButton('Назад')])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
