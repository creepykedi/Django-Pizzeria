from django.db import models

# Create your models here.



class Topping(models.Model):
    topping = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.topping}"


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
    price = models.FloatField()

    def __str__(self):
        return f"{self.type}; price: {self.price}"


class Category(models.Model):
    ctg_name = models.CharField(max_length=64)
    topping = models.ForeignKey(Topping, null=True, blank=True, default=True,
                                on_delete=models.CASCADE, related_name='toppings')
    DinnerPlatter = models.ForeignKey(DinnerPlatter, null=True, blank=True, related_name='platter', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ctg_name}"

