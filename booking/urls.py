from django.urls import path
from . import views as booking

urlpatterns = [
    path('<int:id>/', booking.update_booking, name='update-booking'),
    path('', booking.booking, name='booking'),
]