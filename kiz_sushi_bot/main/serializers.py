from rest_framework import serializers
from kiz_sushi_bot.main.models import FastFood


class FastFoodSerializer(serializers.ModelSerializer):
    food_type = serializers.SerializerMethodField()

    def get_food_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = FastFood
        fields = ('id','title', 'price', 'image', 'food_type', 'consist')
