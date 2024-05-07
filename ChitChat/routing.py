from django.urls import path
from ChitChat.consumer import ChatConsumer

websocket_urlpatterns = [
    path('', ChatConsumer.as_asgi())
]