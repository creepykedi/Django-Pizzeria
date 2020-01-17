from django.contrib import admin

# Register your models here.
from .models import PizzaType, Topping, Category, DinnerPlatter, Sub, SicilianPizzaType, Pasta, Salad,\
    Product, Customer, Order

admin.site.register(PizzaType)
admin.site.register(Topping)
admin.site.register(Category)
admin.site.register(DinnerPlatter)
admin.site.register(Sub)
admin.site.register(SicilianPizzaType)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
