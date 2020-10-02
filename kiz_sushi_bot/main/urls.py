from django.urls import path
from rest_framework.routers import SimpleRouter
from kiz_sushi_bot.main.views import FastFoodViewSet
router = SimpleRouter()

# router.register(r"status-check", views.OrderStatusCheckingViewSet)
app_name = "bot"
urlpatterns = [
    path('fastfood/', FastFoodViewSet.as_view())
]
