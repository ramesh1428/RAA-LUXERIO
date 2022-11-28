from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from hotel_info.models import HotelBooking
from hotel.models import Hotel

# Create your views here.

@csrf_exempt
def success(request,user_id=id):
    if request.method=='POST':
        a = request.POST
        print(a)
        razorpay_order_id = request.POST.get('razorpay_order_id')
        paid = HotelBooking.objects.get(payment_id=razorpay_order_id)
        paid.paid=1
        paid.save()
    # usid = User.objects.get(id=user_id)
    hotel_bill = HotelBooking.objects.filter(user_id = user_id)
    
    return render(request,'bookings.html',{'hotel_bill':hotel_bill})