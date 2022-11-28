from django.shortcuts import redirect, render
from django.http import HttpResponse
from hotel.models import Hotel
from . models import HotelBooking
from datetime import datetime
import random
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

def hotel_info(request,id=id):
    obj = Hotel.objects.filter(id=id)
    rand = random.randint(0,100000)
    

    return render(request,'tours.html',{'info':obj,'rand':rand})

def hotel_billing(request,id=id,user_id=id):
    if request.method == 'POST':
        usid = User.objects.get(id=user_id)
        print(usid)
        hotel_name = request.POST.get('hotel_name')
        price = int(request.POST.get('price')) * 100
        print(price)
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        from_date=datetime.strptime(from_date,"%m/%d/%Y").strftime("%Y-%m-%d")
        to_date=datetime.strptime(to_date,"%m/%d/%Y").strftime("%Y-%m-%d")
        print(from_date)
        rooms = request.POST.get('rooms')
        print(rooms)
        total_amount=int(price) * int(rooms)
        print(int(total_amount))
        order_id=request.POST.get('order_id')
        client = razorpay.Client(auth=("rzp_test_Dqvc5VVKB7Gqi9","VmgHnzoeQQ1nWb7eEsQlTAxP"))
        payment_id= client.order.create({'amount':total_amount,'currency':'INR', 'payment_capture':'1'})
        print(payment_id)
        book_hotel = HotelBooking(hotel_name=hotel_name,price=price,from_date=from_date,to_date=to_date,rooms=rooms,fk_id=id,order_id=order_id,payment_id=payment_id['id'],user_id=usid,total_amount=total_amount)
        book_hotel.save()
    obj = Hotel.objects.filter(id=id)
    hotel_bill = HotelBooking.objects.filter(order_id=order_id)
    return render(request,'tours.html',{'info':obj,'hotel_bill':hotel_bill,'payment':payment_id})


