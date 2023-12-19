from django.urls import path
from . import views as manager

urlpatterns = [
    path('room-type/create', manager.room_type, name='room-type'),
    path('room/create/', manager.room, name='room'),
    path('services', manager.allServices, name='services'),
    path('services/create/', manager.service, name='service'),
    path('', manager.dashboard, name='dashboard')
]