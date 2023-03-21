from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/scan/<str:groupkaname>/', ChatConsumer.as_asgi()),
]