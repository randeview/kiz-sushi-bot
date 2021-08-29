from django.db import models

from kiz_sushi_bot.main.models import TimestampMixin


class TelegramClient(TimestampMixin):
    user_id = models.IntegerField('Идентификатор пользователя')
    first_name = models.CharField('Имя пользователья', max_length=300, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=300, null=True, blank=True)
    username = models.CharField('Никнейм', max_length=300, null=True, blank=True)
    chat_id = models.CharField('Идентификатор чата', max_length=255, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Телеграм клиент'
        verbose_name_plural = 'Телеграм клиенты'


class TelegramReplyTemplate(models.Model):
    """
    Model to store Telegram bot replies templates
    """
    code = models.CharField("Код сообщения", max_length=255, unique=True)
    message = models.TextField("Сообщение")
    is_html = models.BooleanField("HTML", default=False, blank=True)

    class Meta:
        verbose_name = 'Шаблон ответа в Телеграм боте'
        verbose_name_plural = 'Шаблоны ответа в Телеграм боте'

    def __str__(self):
        return self.code

    @classmethod
    def get_message(cls, code):
        reply = cls.objects.filter(code=code).first()
        print(code)
        return reply.message if reply else 'Ошибка шаблона.'
