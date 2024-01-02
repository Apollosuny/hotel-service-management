from django.urls import path
from . import views as booking

urlpatterns = [
    path('<int:id>/', booking.update_booking, name='update-booking'),
    path('history-booking/', booking.history_booking, name='history-booking'),
    path('', booking.booking, name='booking'),
]