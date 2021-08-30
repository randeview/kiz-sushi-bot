from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
    )
    changed_at = models.DateTimeField(
        "Время последнего изменения", auto_now=True, db_index=True
    )

    class Meta:
        abstract = True


class FoodType(models.Model):
    title = models.CharField('Название категории', max_length=255)
    emoji = models.CharField('Эмоджи', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class FastFood(TimestampMixin):
    category = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='fast_foods')
    title = models.CharField("Название продукта", max_length=300)
    price = models.IntegerField("Цена", default=0)
    image = models.ImageField(null=True, blank=True)
    consist = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title
