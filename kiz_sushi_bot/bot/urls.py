from django.urls import path
from kiz_sushi_bot.bot.views import BotWebHookView, TestView

app_name = "bot"
urlpatterns = [
    path('webhook/', BotWebHookView.as_view()),
    path('test/', TestView.as_view())
]
