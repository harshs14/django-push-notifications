from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumers import EchoConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/', EchoConsumer)
    ])
})

