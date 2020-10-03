from django.core.management import BaseCommand

from pprint import pprint
from kiz_sushi_bot.main.models import FastFood
import random

titles = ['Бешбармак', 'Гепук', 'Марс', 'Альейра', 'Юпитер', 'Гречаники (блюдо)', 'Брезаола', 'Булетте', 'Верблюжатина',
          'Бармбрэк', 'Долма']
consisits = ['Перец', 'лук', 'майонез', 'тесто', 'колбаса', 'сыр', 'кетчуп', 'специи', 'рыба', 'рис']


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(20):
            f = FastFood()
            f.title = titles[random.randint(0, 4)]
            f.price = random.randint(1000, 3000)
            f.type = random.randint(1, 9)
            con = ""
            for j in range(random.randint(1, 5)):
                con = con + ", " + consisits[random.randint(1, 9)]
            f.consist = con
            print(f.save())
