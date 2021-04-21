import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import rooms.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings')
django.setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": 
        URLRouter(
            rooms.routing.websocket_urlpatterns
        )
    
})
