from django.shortcuts import render
from . models import Hotel

# Create your views here.

def hotel_list(request):
    if request.method == 'POST':
        region = request.POST.get('region')
        hotel = Hotel.objects.filter(hotel_region=region)
        print(hotel)

    return render(request,'index.html',{'hotel':hotel})

