from django.contrib import admin

# Register your models here.
from .models import Topping, Product, Order


admin.site.register(Topping)
admin.site.register(Product)
admin.site.register(Order)
