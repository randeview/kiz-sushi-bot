from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    user_id = models.IntegerField()
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Chat(models.Model):
    chat_id = models.IntegerField()
    chat_user = models.ForeignKey(TelegramUser, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.chat_user, self.chat_id}"

    class Meta:
        verbose_name = "Чаты"
        verbose_name_plural = "Чаты"


class Message(models.Model):
    message_id = models.IntegerField()
    from_user = models.ForeignKey(TelegramUser, null=True, blank=True, on_delete=models.CASCADE)
    chat_with = models.ForeignKey(Chat, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
