import requests
from django.conf import settings


def send_message(chat_id, text):
    response = requests.get(
        f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'.format(
            chat_id, text))
    return response
