from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
import json
from ...models import TelegramReplyTemplate


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file = open(finders.find('replies.json'), 'r')
        raw_data = file.read()
        data = json.loads(raw_data)
        for item in data:
            if not TelegramReplyTemplate.objects.filter(code=item['code']).exists():
                TelegramReplyTemplate.objects.create(**item)
