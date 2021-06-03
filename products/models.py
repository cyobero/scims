from django.db import models
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True,
                                     null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(args, **kwargs)


FLOWER_TYPE_CHOICES = (
    ('I', "Indica"),
    ('S', "Sativa"),
    ('H', "Hybrid")
)


class Flower(Product):
    flower_type = models.CharField(max_length=10, choices=FLOWER_TYPE_CHOICES, blank=True,
                                   null=True)
    thc_content = models.DecimalField(verbose_name="THC Content (%)", max_digits=5,
                                      decimal_places=2, blank=True, null=True)
    cbd_content = models.DecimalField(verbose_name='CBD Content (%)', max_digits=5,
                                      decimal_places=2, blank=True, null=True)
    final_test_date = models.DateField()
    package_date = models.DateField()
    harvest_date = models.DateField()

    def __str__(self):
        return "{}, {}".format(self.name, self.flower_type)


class PreRoll(Flower):
    pass


class Edible(Product):
    pass


class Vape(Flower):
    pass


class Resin(Flower):
    pass
