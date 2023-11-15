from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.academics.models import Serie, Shift
from geces.core import constants
from geces.core.models import BaseModel


class Address(BaseModel):
    city = models.CharField(
        verbose_name=_("Cidade"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH
    )
    address = models.CharField(
        verbose_name=_("Endereço"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH
    )
    zip_code = models.CharField(verbose_name=_("CEP"), max_length=8)
    phone = models.CharField(verbose_name=_("Telefone"), max_length=11)

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


class Person(BaseModel):
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
        unique=False,
    )
    phone = models.CharField(verbose_name=_("Telefone"), max_length=constants.MEDIUM_CHAR_FIELD_NAME_LENGTH)
    gender = models.CharField(
        verbose_name=_("Gênero"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        choices=Gender.choices,
    )
    address = models.ForeignKey(
        Address,
        verbose_name=_("Endereço"),
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = _("Pessoa")
        verbose_name_plural = _("Pessoas")

    def __str__(self):
        return self.name


class Suplier(Person):

    class Meta:
        verbose_name = _("Fornecedor")
        verbose_name_plural = _("Fornecedores")

    def __str__(self):
        return str(self.name)


class Teacher(Person):

    class Meta:
        verbose_name = _("Professor")
        verbose_name_plural = _("Professores")

    def __str__(self):
        return str(self.name)


class Responsible(Person):

    class Meta:
        verbose_name = _("Responsável")
        verbose_name_plural = _("Responsáveis")

    def __str__(self):
        return str(self.name)


class Student(Person):
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
    responsible_student = models.ForeignKey(
        Responsible,
        verbose_name=_("Responsável"),
        on_delete=models.PROTECT,
        null=True,
        related_name="responsible_student",
    )
    balance = models.DecimalField(_("Saldo"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Discente")
        verbose_name_plural = _("Discentes")

    def __str__(self):
        return str(self.name)


class StudentGroup(BaseModel):
    code = models.CharField(
        verbose_name=_("Código"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    reference_year = models.PositiveSmallIntegerField(verbose_name=_("Ano referência"))
    shift = models.ForeignKey(
        Shift,
        verbose_name=_("Turno"),
        on_delete=models.PROTECT,
    )
    serie = models.ForeignKey(
        Serie,
        verbose_name=_("Série"),
        on_delete=models.PROTECT,
    )
    students = models.ManyToManyField(
        Student,
        verbose_name=_("Discentes"),
        related_name="student_group",
    )

    class Meta:
        verbose_name = _("Turma")
        verbose_name_plural = _("Turmas")

    def __str__(self):
        return f"{self.code} - {self.serie.name}/{self.shift.name}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"GRP-{self.shift.code[:3]}-{self.serie.code[:3]}-{self.reference_year}"

        super().save(*args, **kwargs)
