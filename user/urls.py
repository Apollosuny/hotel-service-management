from django.urls import path
from . import views as user

urlpatterns = [
    path('login/', user.login, name='login')
]