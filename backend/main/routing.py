from django.urls import path
from main.consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/my_consumer/', MyConsumer.as_asgi()),
]
