from django.contrib import admin
from django.urls import path
from rooms.views import home_view, room_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('<room>/', room_view, name=""),
]
