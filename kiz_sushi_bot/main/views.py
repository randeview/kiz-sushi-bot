from kiz_sushi_bot.main.models import FastFood
from kiz_sushi_bot.main.serializers import FastFoodSerializer

from rest_framework import mixins, generics, viewsets, status


class FastFoodViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
