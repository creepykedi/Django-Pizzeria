from django.contrib import admin

# Register your models here.
from .models import Topping, Product, Order, CompletedOrder


admin.site.register(Topping)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CompletedOrder)
