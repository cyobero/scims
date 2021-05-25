from django.db import models
from products.models import Product, Flower


class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # size in grams
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class FlowerStock(ProductStock):
    pass
