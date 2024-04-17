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
