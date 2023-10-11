from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.core import constants


class Person(models.Model):
    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH,
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
        max_length=constants.MEDIUM_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    phone = models.CharField(verbose_name=_("Telefone"), max_length=11)

    class Meta:
        verbose_name = _("Pessoa")
        verbose_name_plural = _("Pessoas")

    def __str__(self):
        return self.name


class Suplier(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="suplier",
    )

    class Meta:
        verbose_name = _("Fornecedor")
        verbose_name_plural = _("Fornecedores")

    def __str__(self):
        return str(self.person)


class Responsible(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="responsible",
    )

    class Meta:
        verbose_name = _("Responsável")
        verbose_name_plural = _("Responsáveis")

    def __str__(self):
        return str(self.person)


class Student(models.Model):
    class Shift(models.IntegerChoices):
        MORNING = 1, _("Matutino")
        AFTERNOON = 2, _("Vespertino")
        NIGHT = 3, _("Noturno")

    class Series(models.IntegerChoices):
        LEVEL1 = 1, _("Nível I")
        LEVEL2 = 2, _("Nível II")
        LEVEL3 = 3, _("Nível III")
        LEVEL4 = 4, _("Alfabetização")
        YEAR1 = 5, _("1° Ano")
        YEAR2 = 6, _("2° Ano")
        YEAR3 = 7, _("3° Ano")
        YEAR4 = 8, _("4° Ano")

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="student",
    )
    serie = models.PositiveSmallIntegerField(
        verbose_name=_("Série"),
        choices=Series.choices,
        validators=[MinValueValidator(1), MaxValueValidator(3)],
    )
    serie = models.PositiveSmallIntegerField(
        verbose_name=_("TURNO"),
        choices=Shift.choices,
        validators=[MinValueValidator(1), MaxValueValidator(8)],
    )
    responsible = models.ForeignKey(
        Responsible,
        verbose_name=_("Responsável"),
        on_delete=models.PROTECT,
        null=True,
        related_name="students",
    )
    balance = models.DecimalField(_("Saldo"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Discente")
        verbose_name_plural = _("Discentes")

    def __str__(self):
        return str(self.person)
