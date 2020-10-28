from rest_framework import serializers

from .models import TelegramUser, Message, Chat


class TelegramUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id')

    class Meta:
        model = TelegramUser
        fields = ('id', 'is_bot', 'first_name', 'last_name', 'username')

    def create(self, validated_data):
        print('create:', validated_data)
        id = validated_data['user_id']
        user = TelegramUser.objects.filter(user_id=id)
        if user.exists():
            return user.first()
        else:
            return super().create(validated_data)


class ChatSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(source='chat_user')

    class Meta:
        model = Chat
        fields = ('user', 'chat_id')
