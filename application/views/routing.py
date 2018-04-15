from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from modules.kanban import consumers as kanban_consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/kanban/<int:kanban_id>', kanban_consumers.KanbanConsumer),

        ])
    ),
})