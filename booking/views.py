from django.shortcuts import render, redirect
from .forms import *
from room.models import *
from user.models import User, Customer

# Create your views here.
def booking(request):
    if request.method == 'POST':
        print(request.POST['checkin_date'])
        print(request.POST['checkout_date'])
        # print(request.POST['services'])
        print(request.POST['room'])
        user = User.objects.get(pk=request.user.id)
        customer = Customer.objects.get(user=user)
        price = RoomType.objects.get(name=request.POST['room']).price
        new_booking = Booking(
            checkin_date=request.POST['checkin_date'], 
            checkout_date=request.POST['checkout_date'], 
            room_type=request.POST['room'], 
            total_price=price, 
            customer=customer
        )
        new_booking.save()
        # new_booking.services.add(request.POST['services'])
        # new_booking.rooms.add(request.POST['rooms'])
        return redirect('/')