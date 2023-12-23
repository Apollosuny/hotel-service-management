from django.shortcuts import render, redirect
from .forms import *
from room.models import * 

# Create your views here.
def dashboard(request):
    return render(request, 'manager/components/dashboard-section.html')

def room_type(request):
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
        return redirect('/')
    else:
        form = RoomTypeForm()
    return render(request, 'manager/pages/room-type.html', { 'form': form })

def room(request):
    if request.method == 'POST':
        print(request.POST['room_type'])
        new_room = Room(room_number=request.POST['room_number'], room_type_id=request.POST['room_type'])
        new_room.save()
    else:
        form = RoomForm()
    return render(request, 'manager/pages/room-create.html', { 'form': form })

def service(request):
    if request.method == 'POST':
        new_service = Service(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
        new_service.save()
    else:
        form = ServiceForm()
    return render(request, 'manager/pages/create-service.html', { 'form': form })

def allServices(request):
    services = Service.objects.all()
    return render(request, 'manager/pages/services.html', { 'services': services })

def about(request):
    return render(request, 'manager/pages/about.html')