from rest_framework import permissions, views, status
from rest_framework.response import Response

from kiz_sushi_bot.bot.bot import BotUpdater
from telegram import Update


class ClientBotWebHookView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        token = kwargs.get("token")
        print(request.data)
        updater = BotUpdater(token=token)
        update = Update.de_json(request.data, updater.bot)
        updater.dispatcher.process_update(update)
        return Response(status=status.HTTP_200_OK)
