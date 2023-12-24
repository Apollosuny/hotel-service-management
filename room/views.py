from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render(request, 'room/home.html')

def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', { 'rooms': rooms })

def roomdetail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request,'room/roomdetail.html', { 'room': room })