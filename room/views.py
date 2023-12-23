from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'room/home.html')

def all_rooms(request):
    return render(request, 'room/rooms.html')

def roomdetail(request):
    return render(request,'room/roomdetail.html')