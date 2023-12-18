from django.core.validators import MaxValueValidator, MinValueValidator
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
        return self.name


class Purchase(BaseModel):
    class Status(models.IntegerChoices):
        PENDING = 1, _("Pendente")
        PAID = 2, _("Pago")
        CANCELED = 3, _("Cancelado")

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
        through="ProductPurchase",
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_("Status"),
        choices=Status.choices,
        validators=[MinValueValidator(1), MaxValueValidator(3)],
    )

    class Meta:
        verbose_name = _("Compra")
        verbose_name_plural = _("Compras")

    def __str__(self):
        return str(self.created_at, self.supplier)


class ProductPurchase(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Produto"),
        on_delete=models.PROTECT,
        related_name="product_purchases",
    )
    purchase = models.ForeignKey(
        Purchase,
        verbose_name=_("Compra"),
        on_delete=models.PROTECT,
        related_name="product_purchases",
    )
    quantity = models.IntegerField(_("Quantidade"), default=0)

    class Meta:
        verbose_name = _("Produto Compra")
        verbose_name_plural = _("Produtos Compras")

    def __str__(self):
        return str(self.product, self.purchase, self.quantity)


class Sell(BaseModel):
    class Status(models.IntegerChoices):
        PENDING = 1, _("Pendente")
        PAID = 2, _("Pago")
        CANCELED = 3, _("Cancelado")

    student = models.ForeignKey(
        Student,
        verbose_name=_("Estudante"),
        on_delete=models.PROTECT,
        related_name="sells",
        null=True,
    )
    products = models.ManyToManyField(
        Product,
        verbose_name=_("Produtos"),
        related_name="sells",
        blank=True,
        through="ProductSell",
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_("Status"),
        choices=Status.choices,
        validators=[MinValueValidator(1), MaxValueValidator(3)],
    )

    class Meta:
        verbose_name = _("Venda")
        verbose_name_plural = _("Vendas")

    def __str__(self):
        return str(self.created_at, self.student)


class ProductSell(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Produto"),
        on_delete=models.PROTECT,
        related_name="product_sell",
    )
    sell = models.ForeignKey(
        Sell,
        verbose_name=_("Venda"),
        on_delete=models.PROTECT,
        related_name="product_sell",
    )
    quantity = models.IntegerField(_("Quantidade"), default=0)

    class Meta:
        verbose_name = _("Produto Venda")
        verbose_name_plural = _("Produtos Vendas")

    def __str__(self):
        return str(self.product, self.sell, self.quantity)
