from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'regular_price', 'discounted_price', 'stock', 'taxable', 'product_status')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent', 'image')


class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ('product_status_id', 'status_name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount_pct', 'discount_amount', 'description')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'ratting', 'comment')


class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'photo')


class AttributeNameAdmin(admin.ModelAdmin):
    list_display = ('_attribute_name',)


class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute_name', 'attribute_value')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
admin.site.register(AttributeName, AttributeNameAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)

admin.site.register(Discount, DiscountAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductStatus, ProductStatusAdmin)
admin.site.register(Tag, TagAdmin)
