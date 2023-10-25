from django.urls import re_path

# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from djangolive.apps.chat.consumers import ChatConsumer


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
    ]),
})
