from django.db import models

# Create your models here.

region = (
    ('Mumbai','Mumbai'),
    ('Kolkata','Kolkata'),
    ('Delhi','Delhi'),
    ('Vishakhapatnam','Vishakhapatnam'),
    ('Bengaluru','Bengaluru'),
    ('Lucknow','Lucknow'),
    ('Hyderabad','Hyderabad'),
    ('Pune','Pune'),
    ('Goa','Goa'),
    ('Srinagar','Srinagar')
)

class Hotel(models.Model):
    hotel_name= models.CharField(max_length=40)
    hotel_region = models.CharField(max_length=100,choices=region, default='Hyderabad')
    hotel_image = models.ImageField(upload_to='pics')
    price = models.IntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()