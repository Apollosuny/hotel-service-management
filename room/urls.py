from django.urls import path, include
from . import views as room

urlpatterns = [
    path('', room.home, name="home")
]
