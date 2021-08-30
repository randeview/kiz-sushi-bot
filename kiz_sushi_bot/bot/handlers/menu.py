from .decorators import *
from kiz_sushi_bot.main.models import FastFood

from kiz_sushi_bot.bot import markups


class MenuHandler:
    FOOD_MENU = 10

    def get_menu_page(self, update, context):
        msg = update.message.reply_text('Меню КИЗ Суши пицца!', parse_mode='HTML',
                                        reply_markup=markups.food_menu_markups())
        return self.FOOD_MENU
