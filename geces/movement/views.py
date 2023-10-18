from django.shortcuts import render  # noqa: F401

from .forms import ProductForm


# Create your views here.
def cadastrar_produto(request):
    form_product = ProductForm()
    return render(request, 'products/products_form.html', {'form_product': form_product})
