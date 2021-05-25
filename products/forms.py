from django import forms
from products.inventory.models import ProductStock


class ProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductStock
        fields = ('product', 'size', 'quantity', 'price')
