from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):

    list_display = ['name_bussines', 'representative', 'phone']
    ordering = ['name_bussines']


admin.site.register(Customer, CustomerAdmin)
