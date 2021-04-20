from django.db import models


class TelegramClient(models.Model):
    user_id = models.IntegerField()
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=300, null=True, blank=True)
    chat_id = models.CharField('ID Телеграм чата', max_length=255, unique=True)

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
        return reply.message if reply else 'Ошибка шаблона.'
