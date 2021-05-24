from django.shortcuts import render
from products.models import Product

# Create your views here.
def inventory_view(request):
    products = Product.objects.all()
    return render(request, 'products/inventory.html', {'products': products})
