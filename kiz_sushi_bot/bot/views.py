import json
from rest_framework.views import APIView
from rest_framework.response import Response
import telegram
from .models import Chat, Message
from .serializers import TelegramUserSerializer, ChatSerializer

bot = telegram.Bot(token='1240576397:AAH-iQqaDhxy3I6BarVbuW3FHoa8emlBQTM')


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
        location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
        contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
        custom_keyboard = [[location_keyboard, contact_keyboard]]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        print(chat_id)
        bot.send_message(chat_id=chat_id, text="Would you mind sharing your location and contact with me?",
                         reply_markup=reply_markup)
        return Response({'message': 'ok'})
