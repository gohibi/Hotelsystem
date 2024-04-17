from django.shortcuts import render , get_object_or_404
from hotel.models import *

# Create your views here.
def index(request):
    hotels = Hotel.objects.filter(status="Live")
    context={
        'hotels':hotels
    }
    return render(request,'partials/index.html',context)

def detail_hotel(request , slug):
    detail_hotel = Hotel.objects.get(slug=slug , status="Live")
    context = {
        'detail':detail_hotel
    }
    return render(request,'partials/detail_hotel.html',context)

def room_type_detail(request, slug , rt_slug):
    hotel = Hotel.objects.get(status="Live",slug=slug)
    room_type = RoomType.objects.get(hotel=hotel,slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type , is_available=True)

    context = {
        'hotel':hotel,
        'room_type':room_type,
        'rooms':rooms
    }
    return render(request,'partials/room_type_detail.html',context)