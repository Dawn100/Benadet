import uuid
from django.db import models
from customers.models import Customer


def product_directory_path(instance, filename):
    return 'products/photo_{0}/{1}'.format(instance.product.product_id, str(uuid.uuid4()) + filename)


def category_directory_path(instance, filename):
    return 'categories/photo_{0}/{1}'.format(instance.category_id, str(uuid.uuid4()) + filename)


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, help_text="Name of category")
    description = models.TextField(max_length=1000, blank=True)
    parent = models.OneToOneField('self', related_name="parent_category", blank=True, null=True,
                                  on_delete=models.PROTECT)
    image = models.ImageField(upload_to=category_directory_path)

    def __str__(self):
        return self.name


class ProductStatus(models.Model):
    product_status_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_name = models.CharField(max_length=250)

    def __str__(self):
        return self.status_name


class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag_name = models.CharField(max_length=250)

    def __str__(self):
        return self.tag_name


class AttributeName(models.Model):
    attribute_name_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _attribute_name = models.CharField(max_length=250)

    def __str__(self):
        return self._attribute_name


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    categories = models.ManyToManyField(Category)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    stock = models.IntegerField()
    taxable = models.BooleanField(default=False)
    product_status = models.ForeignKey(ProductStatus, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute_value_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attribute_name = models.ForeignKey(AttributeName, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute_value = models.CharField(max_length=250)

    def __str__(self):
        return str(self.attribute_name) + ' : ' + str(self.attribute_value)


class ProductPhoto(models.Model):
    product_photo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='photos')
    photo = models.ImageField(upload_to=product_directory_path, null=True)

    def __str__(self):
        return str(self.photo)


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    ratting = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment


class Discount(models.Model):
    discount_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount_pct = models.FloatField(default=0.0, null=True)
    discount_amount = models.FloatField(default=0.0, null=True)
    description = models.CharField(max_length=1000, default="Flash sale!!")

    def __str__(self):
        return str(self.description) + " of " + self.product.name
