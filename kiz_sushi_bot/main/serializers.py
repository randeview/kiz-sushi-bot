from rest_framework import serializers
from kiz_sushi_bot.main.models import FastFood


class FastFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastFood
        fields = ('__all__')
