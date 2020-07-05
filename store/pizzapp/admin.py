from django.contrib import admin

from .models import Order, Pizza

admin.site.register(Order)
admin.site.register(Pizza)