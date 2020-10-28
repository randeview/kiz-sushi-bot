import json

import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from .models import Chat, Message
from .serializers import TelegramUserSerializer, ChatSerializer


class TestView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class BotWebHookView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        serializer_user = TelegramUserSerializer(data=data["message"]["from"])

        serializer_user.is_valid(raise_exception=True)
        user = serializer_user.save()
        chat_id = data['message']['chat']['id']
        chat, _ = Chat.objects.get_or_create(chat_id=chat_id, chat_user=user)
        text = data['message']['text']
        message_id = data['message']['message_id']
        message = Message(message_id=message_id, from_user=user, text=text, chat_with=chat)
        message.save()
        response = requests.get(
            f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'.format(
                chat_id, text))
        return Response({'message': 'ok'})
