from django.urls import path, include
from . import views as room

urlpatterns = [
    path('rooms/<int:id>', room.roomdetail, name="room-detail"),
    path('rooms/', room.all_rooms, name="all-rooms"),
    path('', room.home, name="home")
    
]
