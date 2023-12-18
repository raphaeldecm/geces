from decimal import Decimal

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    price = forms.CharField(widget=forms.TextInput(attrs={"class": "money"}))

    class Meta:
        model = Product
        fields = ("name", "price", "stock", "image")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        return Decimal(price.replace(",", "."))
