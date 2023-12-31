from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from room.models import *
from user.models import User, Customer
from helpers.linked_list import *
from helpers.search import *

# Create your views here.
def booking(request):
    if request.method == 'POST':
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
    booked_room = []
    selected_room = []
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            if 'rooms' in request.POST:
                for data in request.POST['rooms']:
                    selected_room.append(data)
            print("Rooms: ", form.cleaned_data['rooms'])
            

            # Update the instance with form data
            booking.checkin_date = form.cleaned_data['checkin_date']
            booking.checkout_date = form.cleaned_data['checkout_date']
            # booking.room_type = form.cleaned_data['rooms']
            booking.total_price = form.cleaned_data['total_price']
            booking.status = form.cleaned_data['status']
    
            booking.save()
            if selected_room is not None:
                for data in selected_room:
                    booking.rooms.add(data)

            # Updata status room
            if booking.status == Booking.PaymentStatus.FULLY_PAID:
                booked_room = Booking.objects.get(pk=id).rooms.all()
                for data in booked_room:
                    data.status = 'EMPTY'
                    data.save()
            else:
                for data in request.POST['rooms']:
                    data.status = 'BOOKED'
                    data.save()

            return redirect('all-booking')
        else:
            print(form.errors)
            return redirect('all-booking')
    else:
        form = BookingForm(room_type = booking.room_type, initial={ 
            'checkin_date': booking.checkin_date, 
            'checkout_date': booking.checkout_date, 
            'rooms': booking.room_type, 
            'total_price': booking.total_price,
            'status': booking.status
        })
        booked_room = Booking.objects.get(pk=id).rooms.all()


    return render(request, 'booking/update-booking.html', { 'form': form, 'booked_room': booked_room })