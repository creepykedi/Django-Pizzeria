from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
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
    items = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner} ordered {self.items.all()} on {self.date_ordered}, fulfilled: {self.fulfilled}"

    def get_order_items(self):
        ordered = str(self.items.name)
        return ordered


   # def get_total(self):
  #      return sum([item.])