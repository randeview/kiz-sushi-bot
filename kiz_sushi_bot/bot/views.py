import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings


class BotWebHookView(APIView):
    def post(self, request):
        response = requests.get(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getMe').json()
        response = requests.get(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getUpdates').json()
        return Response({'message': response})
