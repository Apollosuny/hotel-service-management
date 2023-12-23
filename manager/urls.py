from django.urls import path
from . import views as manager
from user.views import registerStaff

urlpatterns = [
    path('room-type/create', manager.room_type, name='room-type'),
    path('room/create/', manager.room, name='room'),
    path('services', manager.allServices, name='services'),
    path('services/create/', manager.service, name='service'),
    path('about/', manager.about, name='about'),
    path('staffs/register', registerStaff, name='staff-register'),
    path('', manager.dashboard, name='dashboard'),
]