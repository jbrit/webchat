from django.urls import re_path
from .consumers import EchoConsumer
websocket_urlpatterns = [
    # re_path("", EchoConsumer.as_asgi()),
    re_path("(?P<room>\w+)/", EchoConsumer.as_asgi()),
]