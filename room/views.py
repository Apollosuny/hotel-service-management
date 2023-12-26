from django.shortcuts import render, get_object_or_404
from .models import *
from helpers.linked_list import linked_list
from helpers.search import searchForRoomType

# Create your views here.
def home(request):
    return render(request, 'room/home.html')

def all_rooms(request):
    ll = linked_list()
    price = request.GET.get('price', '')
    adults = request.GET.get('adults', '')
    if adults == '':
        rooms = Room.objects.all()
        for data in rooms:
            ll.append(data)
        ll.display()

        return render(request, 'room/rooms.html', { 'rooms': rooms, 'adults': adults })
    rooms = Room.objects.filter(room_type__num_adults=adults)
    return render(request, 'room/rooms.html', { 'rooms': rooms, 'adults': adults })

def roomdetail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request,'room/roomdetail.html', { 'room': room })