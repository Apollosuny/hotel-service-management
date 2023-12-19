from django.shortcuts import render
from .forms import *

# Create your views here.
def booking(request):
    if request.method == 'POST':
        print(request.POST['checkin_date'])
        print(request.POST['checkout_date'])
        print(request.POST['services'])
        print(request.POST['rooms'])
        new_booking = Booking(checkin_date=request.POST['checkin_date'], checkout_date=request.POST['checkout_date'], total_price=123.41, customer=Customer.objects.get(pk=1))
        new_booking.save()
        new_booking.services.add(request.POST['services'])
        new_booking.rooms.add(request.POST['rooms'])
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', { 'form': form })