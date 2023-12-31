from django.shortcuts import render, get_object_or_404
from .models import *
from helpers.linked_list import linked_list
from helpers.search import searchForRoomType
from django.db.models import Q
from helpers.quick_sort import *
import json
from django.core.serializers import serialize

# Create your views here.
def home(request):
    adults = request.GET.get('adults', '')
    children = request.GET.get('children', '')
    rooms = RoomType.objects.all()[:3]
    if adults or children:
        rooms = RoomType.objects.filter(num_adults=adults, num_children=children)
        return render(request, 'room/rooms.html', { 'rooms': rooms, 'adults': adults, 'children': children })
    
    return render(request, 'room/home.html', { 'rooms': rooms })

def all_rooms(request):
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 2000)
    adults = request.GET.get('adults', "")
    children = request.GET.get('children', "")
    sort = request.GET.get('sort')
    if adults == "" and children == "":
        rooms = RoomType.objects.all()
        json_data = json.loads(serialize('json', rooms))
        rooms = json_data
        if sort is not None:
            if sort == 'asc':
                sort_arr = quick_sort_by_price(json_data, 'price')
                rooms = sort_arr
            elif sort == 'desc':
                sort_arr = quick_sort_by_price_desc(json_data, 'price')
                rooms = sort_arr

        return render(request, 'room/rooms.html', { 'rooms': rooms })
    

    rooms = RoomType.objects.filter(Q(price__range=(min_price, max_price)) & Q(num_adults=adults) & Q(num_children=children))
    return render(request, 'room/rooms.html', { 'rooms': json.loads(serialize('json', rooms)), 'adults': adults, 'children': children, 'min_price': min_price, 'max_price': max_price })

def roomdetail(request, id):
    room = get_object_or_404(RoomType, pk=id)
    services = Service.objects.all()
    return render(request,'room/roomdetail.html', { 'room': room, 'services': services })