from django.db import models
from products.models import Product


class ProductStock(models.Model):
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # size in grams
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
