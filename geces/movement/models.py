from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.core import constants
from geces.core.models import BaseModel
from geces.people.models import Student, Suplier


class Product(BaseModel):
    name = models.CharField(_("Nome"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH)
    price = models.DecimalField(_("Preço"), max_digits=5, decimal_places=2)
    stock = models.IntegerField(_("Estoque"), default=0)
    image = models.ImageField(
        upload_to="ProductImages",
        height_field=None,
        width_field=None,
        max_length=constants.MEDIUM_CHAR_FIELD_NAME_LENGTH,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")

    def __str__(self):
        return str(self.name, self.price, self.stock)


class Purchase(BaseModel):
    supplier = models.ForeignKey(
        Suplier,
        verbose_name=_("Fornecedor"),
        on_delete=models.PROTECT,
        related_name="compras",
        null=True,
    )
    products = models.ManyToManyField(
        Product,
        verbose_name=_("Produtos"),
        related_name="compras",
        blank=True,
    )

    class Meta:
        verbose_name = _("Compra")
        verbose_name_plural = _("Compras")

    def __str__(self):
        return str(self.created_at, self.supplier)


class Sell(BaseModel):
    student = models.ForeignKey(
        Student,
        verbose_name=_("Estudante"),
        on_delete=models.PROTECT,
        related_name="vendas",
        null=True,
    )
    products = models.ManyToManyField(
        Product,
        verbose_name=_("Produtos"),
        related_name="vendas",
        blank=True,
    )

    class Meta:
        verbose_name = _("Venda")
        verbose_name_plural = _("Vendas")

    def __str__(self):
        return str(self.created_at, self.student)
