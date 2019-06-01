import uuid
from django.db import models
from customers.models import Customer


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, help_text="Name of category")
    description = models.TextField(max_length=1000, blank=True)
    parent = models.OneToOneField('self', related_name="parent_category", blank=True, null=True,
                                  on_delete=models.PROTECT)
    image_url = models.CharField(max_length=2048)

    def __str__(self):
        return self.name


class ProductStatus(models.Model):
    product_status_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_name = models.CharField(max_length=250)


class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag_name = models.CharField(max_length=250)


class AttributeName(models.Model):
    attribute_name_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _attribute_name = models.CharField(max_length=250)


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    categories = models.ManyToManyField(Category)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000)
    stock = models.IntegerField()
    taxable = models.BooleanField(default=False)
    product_status = models.ForeignKey(ProductStatus, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)


class AttributeValue(models.Model):
    attribute_value_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attribute_name = models.ForeignKey(AttributeName, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute_value = models.CharField(max_length=250)


class ProductPhoto(models.Model):
    product_photo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    photo_url = models.CharField(max_length=2048)


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    ratting = models.IntegerField()
    comment = models.CharField(max_length=1000)


class Discount(models.Model):
    discount_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount_pct = models.FloatField(blank=True)
    discount_amount = models.FloatField(blank=True)
    description = models.CharField(max_length=1000)
