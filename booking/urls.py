from django.urls import path
from . import views as booking

urlpatterns = [
    path('', booking.booking, name='booking'),
]