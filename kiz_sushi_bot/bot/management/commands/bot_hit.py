import requests
from django.conf import settings
from django.core.management import BaseCommand

from kiz_sushi_bot.main.models import FastFood
import random
import pprint
titles = ['Бешбармак', 'Гепук', 'Марс', 'Альейра', 'Юпитер', 'Гречаники (блюдо)', 'Брезаола', 'Булетте', 'Верблюжатина',
          'Бармбрэк', 'Долма']
consisits = ['Перец', 'лук', 'майонез', 'тесто', 'колбаса', 'сыр', 'кетчуп', 'специи', 'рыба', 'рис']


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getUpdates')
        print(response.json())
