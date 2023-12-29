from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from room.models import * 
from user.models import User
from booking.models import Booking
from django.contrib.auth.decorators import login_required, user_passes_test
from helpers.linked_list import linked_list
from helpers.search import searchForRoomType
from helpers.tsort import timsort
# Create your views here.
@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def dashboard(request):
    return render(request, 'manager/components/dashboard-section.html')

def initialLinkedList(data, text):
    new_linked_list = linked_list()
    room_types = RoomType.objects.all()
    for data in room_types:
        new_linked_list.append(data)
    print(f'Before {text}')
    for item in new_linked_list.display():
        print(f'Name: {item.name} - Price: {item.price}')

def searchPrice(room_types, search):
    # push vào linklist 
    newlinkedlist = linked_list()
    # add data to the linked list 
    for item in room_types:
        newlinkedlist.append(item)
    # search data return the array 
    ArrRoom = searchForRoomType(linklist=newlinkedlist,price=int(search))
    if  ArrRoom == "Not found":
        print("Not found")
    else : 
        for item in ArrRoom:
            print('Name: ' , item.name , " " , "Price: ",item.price ," ","Num_adults: ",item.num_adults," ","Num_children: ",item.num_children)

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def all_room_type(request):
    if request.method == 'GET':
        room_types = RoomType.objects.all()
        search = request.GET.get('search')
        sort = request.GET.get('sort')
        if search is not None and search != '':
            searchPrice(room_types, search)
            room_types = RoomType.objects.filter(price=int(search))
            return render(request, 'manager/pages/room-type/all-room-type.html', { 'room_types': room_types, 'search': search })

        newlinkedlist = linked_list()
        # add data to the linked list 
        for item in room_types:
            newlinkedlist.append(item)
        print("Before sort")
        for item in newlinkedlist.display():
            print(f'Name: {item.name} - Price: {item.price}')
        # sort_room = timsort(newlinkedlist, key=lambda x: x.price)
        # print("After sort")
        # for item in sort_room:
        #     print(f'Name: {item.name} - Price: {item.price}')

        return render(request, 'manager/pages/room-type/all-room-type.html', { 'room_types': room_types })
    return render(request, 'manager/pages/room-type/all-room-type.html', { 'room_types': room_types })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def create_room_type(request):
    new_linked_list = linked_list()
    room_types = RoomType.objects.all()
    for data in room_types:
        new_linked_list.append(data)
    print("Before add new")
    for item in new_linked_list.display():
        print(f'Name: {item.name} - Price: {item.price}')
    if request.method == 'POST':
        type = RoomType(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            num_adults=request.POST['numb_adults'],
            num_children=request.POST['numb_children']
        )
        new_linked_list.append(type)
        type.save()
        print("After add new")
        for item in new_linked_list.display():
            print(f'Name: {item.name} - Price: {item.price}')
        return redirect('all-room-type')
    else:
        form = RoomTypeForm()
    
    return render(request, 'manager/pages/room-type/create-room-type.html', { 'form': form })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def updateARoomType(request, id):
    all_room_type = RoomType.objects.all()
    room_type = get_object_or_404(RoomType, pk=id)
    new_linked_list = linked_list()
    for data in all_room_type:
        new_linked_list.append(data)
    print("Before add new")
    for item in new_linked_list.display():
        print(f'Name: {item.name} - Price: {item.price} - Adults: {item.num_adults} - Children: {item.num_children}')
    
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            # Update the instance with form data
            room_type.name = form.cleaned_data['name']
            room_type.description = form.cleaned_data['description']
            room_type.price = form.cleaned_data['price']
            room_type.num_adults = form.cleaned_data['numb_adults']
            room_type.num_children = form.cleaned_data['numb_children']
            new_linked_list.update_node(id, room_type)
            # print(new_linked_list.get_node_at_index(id))
            room_type.save()

            print("After update data:")
            for item in new_linked_list.display():
                print(f'Name: {item.name} - Price: {item.price} - Adults: {item.num_adults} - Children: {item.num_children}')

            return redirect('all-room-type')
    else:
        form = RoomTypeForm(initial={ 
            'name': room_type.name, 
            'description': room_type.description, 
            'price': room_type.price,
            'numb_adults': room_type.num_adults,
            'numb_children': room_type.num_children
        })

    return render(request, 'manager/pages/room-type/update-room-type.html', { 'form': form })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def deleteARoomType(request, id):
    all_room_type = RoomType.objects.all()
    room_type = get_object_or_404(RoomType, pk=id)
    new_linked_list = linked_list()
    for data in all_room_type:
        new_linked_list.append(data)
    print("Before delete")
    for item in new_linked_list.display():
        print(f'Name: {item.name} - Price: {item.price} - Adults: {item.num_adults} - Children: {item.num_children}')
    if room_type:
        new_linked_list.delete_node_by_index(id)
        room_type.delete()
        print("After delete")
        for item in new_linked_list.display():
            print(f'Name: {item.name} - Price: {item.price} - Adults: {item.num_adults} - Children: {item.num_children}')
        return redirect('all-room-type')

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def all_room(request):
    rooms = Room.objects.all()
    return render(request, 'manager/pages/rooms/rooms.html', { 'rooms': rooms })

@login_required(login_url='login')
@user_passes_test(lambda user: user.role == 'STAFF', login_url='home')
def create_room(request):
    error_message = ''
    form = RoomForm()
    if request.method == 'POST':
        room_number = request.POST['room_number']
        if Room.objects.filter(room_number=room_number).exists():
            error_message = 'The room is duplicated'
            return render(request, 'manager/pages/rooms/room-create.html', { 'form': form, 'message': error_message })
        room_type = RoomType.objects.get(name=request.POST['room_type'])
        new_room = Room(room_number=request.POST['room_number'], room_type_id=room_type.id)
        new_room.save()
        return redirect('all-room')
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