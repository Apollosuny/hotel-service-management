from django.urls import path
from . import views as manager
from user.views import registerStaff

urlpatterns = [
    path('room-types/create', manager.room_type, name='room-type'),
    path('room-types/', manager.all_room_type, name='all-room-type'),
    path('rooms/', manager.all_room, name='all-room'),
    path('rooms/create/', manager.room, name='room'),
    path('services', manager.allServices, name='services'),
    path('services/create/', manager.service, name='service'),
    path('about/', manager.about, name='about'),
    path('staffs/register', registerStaff, name='staff-register'),
    path('', manager.dashboard, name='dashboard'),
]