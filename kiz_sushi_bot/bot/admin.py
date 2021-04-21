from django.contrib import admin

# Register your models here.


from .models import TelegramReplyTemplate, TelegramClient

admin.site.register(TelegramReplyTemplate)
admin.site.register(TelegramClient)
