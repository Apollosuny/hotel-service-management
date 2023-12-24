from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from room.models import * 
from user.models import User
from booking.models import Booking
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def dashboard(request):
    return render(request, 'manager/components/dashboard-section.html')

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def all_room_type(request):
    room_types = RoomType.objects.all()
    return render(request, 'manager/pages/room-type/all-room-type.html', { 'room_types': room_types })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def create_room_type(request):
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['description'])
        print(request.POST['price'])
        print(request.POST['numb_adults'])
        print(request.POST['numb_children'])
        type = RoomType(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            num_adults=request.POST['numb_adults'],
            num_children=request.POST['numb_children']
        )
        type.save()
        return redirect('all-room-type')
    else:
        form = RoomTypeForm()
    return render(request, 'manager/pages/room-type/create-room-type.html', { 'form': form })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def all_room(request):
    rooms = Room.objects.all()
    return render(request, 'manager/pages/rooms/rooms.html', { 'rooms': rooms })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def create_room(request):
    if request.method == 'POST':
        room_type = RoomType.objects.get(name=request.POST['room_type'])
        new_room = Room(room_number=request.POST['room_number'], room_type_id=room_type.id)
        new_room.save()
        return redirect('all-room')
    else:
        form = RoomForm()
    return render(request, 'manager/pages/rooms/room-create.html', { 'form': form })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def create_service(request):
    if request.method == 'POST':
        new_service = Service(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
        new_service.save()
        return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'manager/pages/services/create-service.html', { 'form': form })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def allServices(request):
    services = Service.objects.all()
    return render(request, 'manager/pages/services/services.html', { 'services': services })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def updateAService(request, id):
    service = get_object_or_404(Service, pk=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            # Update the instance with form data
            service.name = form.cleaned_data['name']
            service.description = form.cleaned_data['description']
            service.price = form.cleaned_data['price']
            service.save()
            return redirect('services')
    else:
        form = ServiceForm(initial={ 'name': service.name, 'description': service.description, 'price': service.price })

    return render(request, 'manager/pages/services/update-service.html', { 'form': form })
    
@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def deleteAService(request, id):
    service = get_object_or_404(Service, pk=id)
    if service:
        service.delete()
        return redirect('services')

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def all_customers(request):
    customers = User.objects.filter(role='USER')
    return render(request, 'manager/pages/customers/all-customers.html', { 'customers': customers })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def all_booking(request):
    booking = Booking.objects.all()
    return render(request, 'manager/pages/booking/all-booking.html', { 'bookings': booking })

def about(request):
    return render(request, 'manager/pages/about.html')