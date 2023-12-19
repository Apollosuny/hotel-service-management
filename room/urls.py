from django.urls import path, include
from . import views as room

urlpatterns = [
    path('roomdetail/', room.roomdetail, name="roomdetail"),
    path('', room.home, name="home")
    
]
