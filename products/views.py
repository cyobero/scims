from django.shortcuts import render
from products.inventory.models import ProductStock

# Create your views here.
def inventory_view(request):
    products = ProductStock.objects.all()
    return render(request, 'products/inventory.html', {'products': products})
