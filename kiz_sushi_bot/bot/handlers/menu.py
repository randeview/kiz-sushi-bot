from .decorators import *
from kiz_sushi_bot.main.models import FastFood, FoodType
from telegram.ext import (
    Updater, CommandHandler, Filters, MessageHandler, ConversationHandler,
    CallbackQueryHandler, PicklePersistence)

from kiz_sushi_bot.bot import markups


class MenuHandler:
    FOOD_MENU = 10

    def get_food_menu_handlers(self):
        return [MessageHandler(Filters.regex('^(.*?)$'), self.get_foods), CommandHandler('start', self.start)]

    def get_menu_page(self, update, context):
        msg = update.message.reply_text('Меню КИЗ Суши пицца!', parse_mode='HTML',
                                        reply_markup=markups.food_menu_markups())
        return self.FOOD_MENU

    def get_foods(self, update, context):
        text = update.message.text
        if text == 'Назад':
            update.message.reply_text("Главное меню",
                                      parse_mode='HTML',
                                      reply_markup=markups.main_menu_markup())
            return self.MENU_STATE

        food_type = FoodType.objects.get(title=text)
        for ff in food_type.fast_foods.all():
            message = f"Название: {ff.title} \n Цена: {ff.price} \n Состав: {ff.consist}"
            if ff.image:
                self.bot.send_photo(
                    update.message.chat_id, photo=ff.image, parse_mode='HTML')
            update.message.reply_text(text=message)
        return self.FOOD_MENU
