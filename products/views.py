from django.shortcuts import render, redirect
from django.contrib import messages
from products.forms import NewProductForm, NewFlowerForm, NewPreRollForm, NewEdibleForm, NewVapeForm
from products.models import Product
from django.contrib.auth.decorators import login_required
from datatableview import Datatable
from datatableview.views import DatatableView
# Create your views here.

class ProductConfigDataTableView(DatatableView):

    model = Product

    class datatable_class(Datatable):

        class Meta:
            model = Product
            columns = ['id', 'name', 'price', 'quantity', 'date_added']

PRODUCT_FORMS = {
    'Product': NewProductForm,
    'Flower': NewFlowerForm,
    'Pre-Roll': NewPreRollForm,
    'Vape': NewVapeForm,
    'Edible': NewEdibleForm
}


@login_required(login_url='user_login')
def inventory_view(request):
    # retrieve only objects that are in stock
    products = Product.objects.filter(quantity__gte=1)
    return render(request, 'products/inventory.html', {'products': products})


@login_required(login_url='user_login')
def add_product_view(request):
    product_type = request.GET.get('product_type')
    # If a product was selected from the drop-down menu then load the correct form.
    if product_type is not None:
        form = PRODUCT_FORMS[product_type]
        if request.method == 'POST':
            form = form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Added product')
                return redirect('add_product')
        return render(request, 'products/add_product.html', {'product_type': product_type,
                                                             'form': form})
    return render(request, 'products/add_product.html', {'product_type': product_type})


@login_required(login_url='user_login')
def product_view(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product.html', {'product': product})
