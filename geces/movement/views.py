from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product


@login_required
def cadastrar_produto(request):
    if request.method == "POST":
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            form_product.save()
            return redirect("movement:listar_produtos")
    else:
        form_product = ProductForm()
    return render(request, "products/products_form.html", {"form_product": form_product})

@login_required
def editar_produto(request, pk):
    produto = Product.objects.get(pk=pk)
    form_product = ProductForm(request.POST or None, instance=produto)
    if form_product.is_valid():
        form_product.save()
        return redirect("movement:listar_produtos")
    return render(request, "products/products_form.html", {"form_product": form_product})

@login_required
def excluir_produto(request, pk):
    produto = Product.objects.get(pk=pk)
    produto.delete()
    return redirect("movement:listar_produtos")

@login_required
def listar_produtos(request):
    produtos = Product.objects.all()
    return render(request, "products/products_list.html", {"produtos": produtos})
