from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.academics.models import Enrollment
from geces.core.constants import SMALL_CHAR_FIELD_NAME_LENGTH
from geces.core.models import BaseModel


class Invoice(BaseModel):
    class Status(models.IntegerChoices):
        PENDING = 1, _("PENDING")
        PAID = 2, _("PAID")
        CANCELLED = 3, _("CANCELLED")

    class Type(models.IntegerChoices):
        MONTHLY = 1, _("MONTHLY")
        OTHER = 2, _("OTHER")

    status = models.PositiveSmallIntegerField(
        verbose_name=_("Situação"),
        choices=Status.choices,
        validators=[MinValueValidator(1), MaxValueValidator(3)],
        default=Status.PENDING,
    )
    type = models.PositiveSmallIntegerField(
        verbose_name=_("Tipo"),
        choices=Type.choices,
        validators=[MinValueValidator(1), MaxValueValidator(2)],
        default=Type.MONTHLY,
    )
    enrollment = models.ForeignKey(Enrollment, on_delete=models.PROTECT, related_name="invoices")
    value = models.DecimalField(verbose_name=_("Valor"), max_digits=6, decimal_places=2, default=0)
    due_date = models.DateField(
        verbose_name=_("Data de Vencimento"),
    )
    observations = models.TextField(verbose_name=_("Observações"), blank=True)

    class Meta:
        verbose_name = _("Fatura")
        verbose_name_plural = _("Faturas")

    def __str__(self):
        return f"Fatura para {self.enrollment.student.name} - Vencimento: {self.due_date}"


# TODO: Allow multiple payments for the same invoice
class Payment(BaseModel):
    class PaymentType(models.IntegerChoices):
        CASH = 1, _("Dinheiro")
        CREDIT_CARD = 2, _("Cartão de Crédito")
        DEBIT_CARD = 3, _("Cartão de Débito")
        BANK_SLIP = 4, _("Boleto")
        PIX = 5, _("PIX")

    payment_type = models.CharField(
        max_length=SMALL_CHAR_FIELD_NAME_LENGTH, choices=PaymentType.choices, default=PaymentType.CASH
    )
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="payments")
    value = models.DecimalField(verbose_name=_("Valor"), max_digits=6, decimal_places=2, default=0)
    discount = models.DecimalField(verbose_name=_("Desconto"), max_digits=6, decimal_places=2, default=0)
    observations = models.TextField(verbose_name=_("Observações"), blank=True)

    class Meta:
        verbose_name = _("Pagamento")
        verbose_name_plural = _("Pagamentos")

    def __str__(self):
        return f"Pagamento de {self.amount_paid} para fatura: {self.invoice.id}"
