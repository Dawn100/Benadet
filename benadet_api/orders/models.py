import uuid
from django.db import models
from customers.models import Customer


class Coupon(models.Model):
    coupon_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_created=True)
    end_date = models.DateTimeField(blank=True)


class ShippingRegion(models.Model):
    shipping_region_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()


class Shipping(models.Model):
    shipping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shipping_region = models.ForeignKey(ShippingRegion, on_delete=models.PROTECT)
    shipping_date = models.DateTimeField(auto_created=True)


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    is_fulfilled = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    coupon_id = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    total = models.FloatField()


class Tax(models.Model):
    tax_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tax_pct = models.FloatField()
    amount = models.FloatField()
    tax_name = models.CharField(max_length=250)
    shipping = models.OneToOneField(Shipping, on_delete=models.PROTECT)


class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    transaction_date = models.DateTimeField(auto_created=True)
    amount = models.FloatField()
    payment_passcode = models.CharField(max_length=50)
