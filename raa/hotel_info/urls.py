from django.urls import path
from . import views

urlpatterns = [
    path('',views.hotel_info,name='hotel_info'),
    path('hotel_billing/<int:user_id>/',views.hotel_billing,name='hotel_billing'),
]