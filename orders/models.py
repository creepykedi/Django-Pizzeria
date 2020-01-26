from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.


class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"


class Product(models.Model):
    choices = [
        ('L', 'LARGE'),
        ('S', 'SMALL'),
        ('SING', 'SINGLE')
    ]
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    name = models.CharField(max_length=64, default=0)
    type = models.CharField(max_length=64, default=0)
    size = models.CharField(choices=choices, max_length=64, default=0)

    def __str__(self):
        return f"{self.name} {self.type}, {self.size}, price {self.price}"


class Order(models.Model):
    choices = [
        ('Sausage', 'Sausage'),
        ('Pepperoni', 'Pepperoni'),
        ('Mushrooms', 'Mushrooms'),
        ('Onions', 'Onions'),
        ('Ham', 'Ham'),
        ('Canadian', 'Canadian Bacon'),
        ('Spinach', 'Spinach'),
        ('Tomato', 'Tomato & Basil'),
        ('Green', 'Green Pepper'),
        ('Anchovies', 'Anchovies'),
        ('Artichoke', 'Artichoke'),
        ('Buffalo', 'Buffalo Chicken'),
        ('Eggplant', 'Eggplant'),
        ('Zucchini', 'Zucchini'),
        ('Fresh', 'Fresh Garlic')
    ]
    items = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    toppingchoice = MultiSelectField(choices=choices, null=True, blank=True)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"#{self.pk} {self.owner} ordered {self.items.first()}, {self.toppingchoice} on {self.date_ordered}," \
               f"fulfilled: {self.fulfilled}, topping: {self.toppingchoice}"

    def get_order_items(self):
        ordered = str(self.items.name)
        return ordered

    def clean_fulfilled(self):
        fulfilled = Order.objects.filter(fulfilled=True)
        for order in fulfilled:
            order.delete()



class CompletedOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

   # def get_total(self):
  #      return sum([item.])