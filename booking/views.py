from django.shortcuts import render, redirect, get_object_or_404
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
    
def update_booking(request, id):
    booking = get_object_or_404(Booking, pk=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print("Valid")
            selected_room = Room.objects.get(pk = request.POST['rooms'])
            print(selected_room)
            # Update the instance with form data
            booking.checkin_date = form.cleaned_data['checkin_date']
            booking.checkout_date = form.cleaned_data['checkout_date']
            # booking.room_type = form.cleaned_data['rooms']
            booking.total_price = form.cleaned_data['total_price']
    
            booking.save()
            # booking.rooms.add(selected_room)

            # Updata status room
            booked_room = Room.objects.get(pk = request.POST['rooms'])
            booked_room.status = 'BOOKED'
            booked_room.save()

            return redirect('all-booking')
        else:
            print(form.errors)
            return redirect('all-booking')
    else:
        form = BookingForm(room_type = booking.room_type, initial={ 
            'checkin_date': booking.checkin_date, 
            'checkout_date': booking.checkout_date, 
            'room_type': booking.room_type, 
            'total_price': booking.total_price,
        })

    return render(request, 'booking/update-booking.html', { 'form': form })