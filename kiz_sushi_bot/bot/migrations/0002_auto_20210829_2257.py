# Generated by Django 2.2.5 on 2021-08-29 22:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramclient',
            name='is_bot',
        ),
        migrations.AddField(
            model_name='telegramclient',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время последнего изменения'),
        ),
        migrations.AddField(
            model_name='telegramclient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='telegramclient',
            name='chat_id',
            field=models.CharField(max_length=255, unique=True, verbose_name='Идентификатор чата'),
        ),
        migrations.AlterField(
            model_name='telegramclient',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя пользователья'),
        ),
        migrations.AlterField(
            model_name='telegramclient',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='telegramclient',
            name='user_id',
            field=models.IntegerField(verbose_name='Идентификатор пользователя'),
        ),
        migrations.AlterField(
            model_name='telegramclient',
            name='username',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Никнейм'),
        ),
    ]