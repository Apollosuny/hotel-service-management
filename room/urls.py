from django.urls import path, include
from . import views as room
from manager import views as manager

urlpatterns = [
    path('rooms/<int:id>', room.roomdetail, name="room-detail"),
    path('rooms/', room.all_rooms, name="all-rooms"),
    path('about/', manager.about, name='about'),
    path('', room.home, name="home")
    
]
