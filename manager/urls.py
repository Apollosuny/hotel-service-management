from django.urls import path
from . import views as manager
from user.views import registerStaff

urlpatterns = [
    path('room-types/create', manager.create_room_type, name='create-room-type'),
    path('room-types/<int:id>', manager.updateARoomType, name='update-room-type'),
    path('room-types/delete/<int:id>', manager.deleteARoomType, name='delete-room-type'),
    path('room-types/', manager.all_room_type, name='all-room-type'),
    path('rooms/', manager.all_room, name='all-room'),
    path('rooms/create/', manager.create_room, name='create-room'),
    path('services/', manager.allServices, name='services'),
    path('services/create/', manager.create_service, name='create-service'),
    path('services/<int:id>', manager.updateAService, name='update-service'),
    path('services/delete/<int:id>', manager.deleteAService, name='delete-service'),
    path('customers/', manager.all_customers, name='all-customers'),
    path('booking/', manager.all_booking, name='all-booking'),
    path('staffs/register', registerStaff, name='staff-register'),
    path('', manager.dashboard, name='dashboard'),
]