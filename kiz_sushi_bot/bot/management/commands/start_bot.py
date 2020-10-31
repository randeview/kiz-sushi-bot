import telegram
from django.core.management import BaseCommand
class Command(BaseCommand):

    def handle(self, *args, **options):
        bot = telegram.Bot(token='1240576397:AAH-iQqaDhxy3I6BarVbuW3FHoa8emlBQTM')
