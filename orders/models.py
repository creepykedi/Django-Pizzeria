from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Topping(models.Model):
    topping = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.topping}"


class Price(models.Model):
    price = models.FloatField()

    def __str__(self):
        return f"{self.price}"


class DinnerPlatter(models.Model):
    dinnerPlatter = models.CharField(max_length=64)
    priceSmall = models.FloatField()
    priceLarge = models.FloatField()

    def __str__(self):
        return f"{self.dinnerPlatter}; price: small {self.priceSmall}; large {self.priceLarge}"


class PizzaType(models.Model):
    type = models.CharField(max_length=64)
    priceSmall = models.FloatField()
    priceLarge = models.FloatField()

    def __str__(self):
        return f"{self.type}; price: small {self.priceSmall}; large {self.priceLarge}"


class SicilianPizzaType(models.Model):
    type = models.CharField(max_length=64)
    priceSmall = models.FloatField()
    priceLarge = models.FloatField()

    def __str__(self):
        return f"{self.type}; price: small {self.priceSmall}; large {self.priceLarge}"


class Sub(models.Model):
    type = models.CharField(max_length=64)
    priceSmall = models.FloatField(blank=True, null=True, default=6.5)
    priceLarge = models.FloatField(default=7.95)

    def __str__(self):
        return f"{self.type}; price: small {self.priceSmall}; large {self.priceLarge}"


class Pasta(models.Model):
    type = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.type}; price: {self.price}"


class Salad(models.Model):
    type = models.CharField(max_length=64)
    price = models.DecimalField()

    def __str__(self):
        return f"{self.type}; price: {self.price}"




class Product(models.Model):
    topping = models.ManyToManyField(Topping)
    dinner_plt = models.ForeignKey(DinnerPlatter, null=True, blank=True, default=True,
                                on_delete=models.CASCADE)
    pizza_normal = models.ForeignKey(PizzaType, null=True, blank=True, default=True,
                                on_delete=models.CASCADE)
    pizza_siz = models.ForeignKey(SicilianPizzaType, null=True, blank=True, default=True,
                                on_delete=models.CASCADE)
    sub = models.ForeignKey(Sub, null=True, blank=True, default=True,
                                on_delete=models.CASCADE)
    salad = models.ForeignKey(Salad, null=True, blank=True, default=True,
                            on_delete=models.CASCADE)
    sizeLarge = models.BooleanField(default=True)


    # showing products

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            if field:
                field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


#class Purchase(models.Model):
  #  product =
    #price =
  #  size =

class Customer(models.Model):
    customer = models.OneToOneField(User, null=True, blank=True, default=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Product, null=True, blank=True, default=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.customer} cart: {self.cart}"


class Order(models.Model):
    items = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fulfilled = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.owner} ordered {self.items.all()} on {self.date_ordered}, fulfilled: {self.fulfilled}"

    def get_order_items(self):
        ordered = str(self.items.all())
        return ordered


   # def get_total(self):
  #      return sum([item.])