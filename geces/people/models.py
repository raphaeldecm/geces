from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.core import constants
from geces.core.models import BaseModel


class Address(BaseModel):
    city = models.CharField(verbose_name=_("Cidade"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH)
    address = models.CharField(verbose_name=_("Endereço"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH)
    zip_code = models.CharField(verbose_name=_("CEP"), max_length=8)
    phone = models.CharField(verbose_name=_("Telefone"), max_length=constants.MEDIUM_CHAR_FIELD_NAME_LENGTH)

    class Meta:
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")

    def __str__(self):
        full_address = _("{address}, {city}, {state}, CEP {zip_code}")
        return full_address.format(
            address=self.address,
            city=self.city,
            state=self.country_state.abbreviation,
            zip_code=self.zip_code,
        )


class PersonBase(BaseModel):
    class Gender(models.TextChoices):
        MALE = "MALE", _("Masculino")
        FEMALE = "FEMALE", _("Feminino")

    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH,
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
        max_length=constants.MEDIUM_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    gender = models.CharField(
        verbose_name=_("Gênero"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        choices=Gender.choices,
    )
    birth = models.DateField(verbose_name=_("Nascimento"))
    address = models.ForeignKey(
        Address,
        verbose_name=_("Endereço"),
        on_delete=models.PROTECT,
        related_name="%(class)s",
    )

    class Meta:
        abstract = True
        verbose_name = _("Pessoa")
        verbose_name_plural = _("Pessoas")

    def __str__(self):
        return self.name


class Suplier(PersonBase):
    class Meta:
        verbose_name = _("Fornecedor")
        verbose_name_plural = _("Fornecedores")

    def __str__(self):
        return str(self.name)


class Teacher(PersonBase):
    class Meta:
        verbose_name = _("Professor")
        verbose_name_plural = _("Professores")

    def __str__(self):
        return str(self.name)


class Responsible(PersonBase):
    class Meta:
        verbose_name = _("Responsável")
        verbose_name_plural = _("Responsáveis")

    def __str__(self):
        return str(self.name)


class Student(PersonBase):
    class Status(models.IntegerChoices):
        PENDING = 1, _("Pendente")
        ENROLLED = 2, _("Matriculado")
        STUDYING = 3, _("Cursando")

    status = models.PositiveSmallIntegerField(
        verbose_name=_("Situação"),
        choices=Status.choices,
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        default=Status.PENDING,
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
        return str(self.name)
