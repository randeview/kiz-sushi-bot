from django.urls import path
from rest_framework.routers import SimpleRouter
from kiz_sushi_bot.main.views import FastFoodViewSet, FastFoodTypeView, FastFoodDetail

router = SimpleRouter()

# router.register(r"status-check", views.OrderStatusCheckingViewSet)
app_name = "bot"
urlpatterns = [
    path('foods/', FastFoodViewSet.as_view()),
    path('foods/<int:type>', FastFoodTypeView.as_view()),
    path('food/<int:pk>', FastFoodDetail.as_view())
]
