from django.urls import path
from . import views

urlpatterns = [
    path('',views.hotel_list,name='hotel_list'),
]