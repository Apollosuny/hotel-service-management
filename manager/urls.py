from django.urls import path
from . import views as manager

urlpatterns = [
    path('', manager.dashboard, name='dashboard')
]