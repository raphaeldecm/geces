from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from .forms import ProductForm
from .models import Product


class ProductFormView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/products_form.html"
    success_url = reverse_lazy("canteen:products_list")
    success_message = _("Produto cadastrado com sucesso!")


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/products_form.html"
    success_url = reverse_lazy("canteen:products_list")
    success_message = _("Produto atualizado com sucesso!")


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = "products/products_confirm_delete.html"
    success_url = reverse_lazy("canteen:products_list")
    success_message = _("Produto excluído com sucesso!")


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 5
    ordering = ["name"]
    template_name = "products/products_list.html"
    queryset = Product.objects.all()


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    queryset = Product.objects.all()
