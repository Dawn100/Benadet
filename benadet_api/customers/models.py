import uuid
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15)
    location_lat = models.FloatField()
    location_long = models.FloatField()
