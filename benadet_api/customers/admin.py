from django.contrib import admin
from .models import Customer


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_no')


admin.site.register(Customer, CustomerAdmin)

