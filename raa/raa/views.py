from django.shortcuts import render

from hotel.models import Hotel


def index(request):
    arr = []
    hotel = Hotel.objects.values('hotel_region').distinct()
    for i in hotel:
        arr.append(i)
    

    return render(request,'index.html',{'hotel_details':arr})


def about(request):
    return render(request,'about.html')