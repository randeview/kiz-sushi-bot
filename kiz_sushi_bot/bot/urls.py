from django.urls import path
from . import views

app_name = "bot"
urlpatterns = [
    path('client/<str:token>/', views.ClientBotWebHookView.as_view(), name='client')
]
