from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/group/<int:groupkid>/', ChatConsumer.as_asgi()),
]