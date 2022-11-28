from django.db import models
from hotel.models import Hotel
from django.contrib.auth.models import User
# import uuid
# Create your models here.

class HotelBooking(models.Model):
    fk = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    hotel_name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    rooms = models.IntegerField()
    total_amount = models.IntegerField(default=0)
    order_id = models.CharField(max_length=1000,default='noid')
    payment_id = models.CharField(max_length=100,default='noid')
    paid = models.BooleanField(default=False)
    # uuid = models.UUIDField(default=uuid.uuid4,unique=True,db_index=True,editable=False)



# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post_title = models.CharField(max_length=100)
#     post_cat = models.CharField(max_length=100)