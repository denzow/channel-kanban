from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from modules.chat import consumers as chat_consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
                path('ws/chat/<str:room_name>/', chat_consumers.ChatConsumer),
        ])
    ),
})