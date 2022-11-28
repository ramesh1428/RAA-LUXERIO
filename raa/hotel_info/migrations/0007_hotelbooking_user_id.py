# Generated by Django 4.1.3 on 2022-11-27 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_info', '0006_hotelbooking_paid_hotelbooking_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
