# Generated by Django 2.2.5 on 2020-10-03 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FastFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название продукта')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('type', models.IntegerField(choices=[(1, 'Суши'), (2, 'Пицца'), (3, 'Бургеры'), (4, 'Фри'), (5, 'Напитки'), (6, 'Соусы'), (7, 'Добавки'), (8, 'Акции')])),
            ],
        ),
    ]
