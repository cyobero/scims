from django.shortcuts import render, redirect
from django.contrib import messages
from products.inventory.models import ProductStock
from products.forms import ProductStockForm
# Create your views here.


def inventory_view(request):
    products = ProductStock.objects.all()
    return render(request, 'products/inventory.html', {'products': products})


def add_product_view(request):
    if request.method == 'POST':
        form = ProductStockForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data.get('product')
            size = form.cleaned_data.get('size')
            quantity = form.cleaned_data.get('quantity')
            price = form.cleaned_data.get('price')

            new_product = ProductStock(product=product, size=size, quantity=quantity,
                                       price=price)
            messages.success(request, "{} added to inventory".format(new_product.product.name))
            new_product.save()
            return redirect('add_product')
    else:
        form = ProductStockForm()
    form = ProductStockForm()
    return render(request, 'products/add_product.html', {'form': form})
