from django.contrib import admin
from products.models import Product, Flower, PreRoll, Edible, Vape
from products.inventory.models import ProductStock

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass


class FlowerAdmin(admin.ModelAdmin):
    pass


class PreRollAdmin(admin.ModelAdmin):
    pass


class ProductStockAdmin(admin.ModelAdmin):
    pass


class EdibleAdmin(admin.ModelAdmin):
    pass


class VapeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(PreRoll, PreRollAdmin)
admin.site.register(ProductStock, ProductStockAdmin)
admin.site.register(Edible, EdibleAdmin)
admin.site.register(Vape, VapeAdmin)
