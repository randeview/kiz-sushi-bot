from django.db import models


class FastFood(models.Model):
    sushi, pizza, burger, free, drinks, sauce, supplement, action = range(1, 9)
    fastfood_types = (
        (sushi, 'Суши'),
        (pizza, 'Пицца'),
        (burger, 'Бургеры'),
        (free, 'Фри'),
        (drinks, 'Напитки'),
        (sauce, 'Соусы'),
        (supplement, 'Добавки'),
        (action, 'Акции'),
    )
    title = models.CharField("Название продукта", max_length=300)
    price = models.IntegerField("Цена", default=0)
    avatar = models.ImageField(null=True, blank=True)
    type = models.IntegerField(choices=fastfood_types)
