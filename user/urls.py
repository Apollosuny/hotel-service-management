from django.urls import path
from . import views as user

urlpatterns = [
    path('login/', user.loginUser, name='login'),
    path('register/', user.registerCustomer, name='register'),
    path('logout/', user.logoutUser, name='logout'),
    path('profile/', user.profile, name='profile'),
]