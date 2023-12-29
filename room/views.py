from django.shortcuts import render, get_object_or_404
from .models import *
from helpers.linked_list import linked_list
from helpers.search import searchForRoomType

# Create your views here.
def home(request):
    adults = request.GET.get('adults', '')
    if adults:
        rooms = RoomType.objects.filter(num_adults=adults)
        return render(request, 'room/rooms.html', { 'rooms': rooms, 'adults': adults })
    
    return render(request, 'room/home.html')

def all_rooms(request):
    ll = linked_list()
    price = request.GET.get('price', '')
    adults = request.GET.get('adults', '')
    if adults == '':
        rooms = RoomType.objects.all()
        for data in rooms:
            ll.append(data)
        ll.display()

        return render(request, 'room/rooms.html', { 'rooms': rooms, 'adults': adults })
    rooms = RoomType.objects.filter(num_adults=adults)
    return render(request, 'room/rooms.html', { 'rooms': rooms, 'adults': adults })

def roomdetail(request, id):
    room = get_object_or_404(RoomType, pk=id)
    return render(request,'room/roomdetail.html', { 'room': room })