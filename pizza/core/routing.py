from django.urls import path
from .consumers import KafkaConsumerWebSocket

websocket_urlpatterns = [
    path("ws/", KafkaConsumerWebSocket.as_asgi()),
]