from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


FLOWER_TYPE_CHOICES = (
    ('I', "Indica"),
    ('S', "Sativa"),
    ('H', "Hybrid")
)


class Flower(Product):
    flower_type = models.CharField(max_length=10, choices=FLOWER_TYPE_CHOICES)
    thc_content = models.DecimalField(max_digits=4, decimal_places=2, blank=True,
                                      null=True)


class PreRoll(Flower):
    pass


class Edible(Product):
    thc_content = models.DecimalField(verbose_name='THC (%)', max_digits=4,
                                      decimal_places=1, blank=True, null=True)
    calories = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)


class Vape(Flower):
    pass
