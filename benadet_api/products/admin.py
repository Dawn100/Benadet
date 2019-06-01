from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'description', 'parent', 'image_url')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'regular_price','discounted_price','stock','taxable','product_status')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
