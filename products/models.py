from django.db import models
from PIL import Image

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    def __str__(self):
        return self.name
