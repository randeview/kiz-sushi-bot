from kiz_sushi_bot.main.models import FastFood
from kiz_sushi_bot.main.serializers import FastFoodSerializer

from rest_framework import mixins, generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


class FastFoodViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FastFoodTypeView(APIView):
    def get(self, request, type, format=None):
        queryset = FastFood.objects.filter(type=type)
        serializer = FastFoodSerializer(queryset, many=True)
        return Response(serializer.data)


class FastFoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer
