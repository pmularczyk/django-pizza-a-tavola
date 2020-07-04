from django.contrib import admin

from .models import Order, Pizza, Variation

admin.site.register(Order)
admin.site.register(Pizza)
admin.site.register(Variation)