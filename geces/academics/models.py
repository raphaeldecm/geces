from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.core import constants
from geces.core.models import BaseModel
from geces.people.models import Student, Teacher


# Create your models here.
class Shift(BaseModel):
    code = models.CharField(
        verbose_name=_("Código"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    name = models.CharField(verbose_name=_("Nome"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH, unique=True)

    class Meta:
        verbose_name = _("Turno")
        verbose_name_plural = _("Turnos")

    def __str__(self):
        return self.name


class Serie(BaseModel):
    code = models.CharField(
        verbose_name=_("Código"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    name = models.CharField(verbose_name=_("Nome"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH)
    shift = models.ForeignKey(
        Shift,
        verbose_name=_("Turno"),
        on_delete=models.PROTECT,
        related_name="series",
    )
    teacher = models.ForeignKey(
        Teacher,
        verbose_name=_("Professor"),
        on_delete=models.PROTECT,
        related_name="series",
        null=True,
    )

    class Meta:
        verbose_name = _("Série")
        verbose_name_plural = _("Séries")

    def __str__(self):
        return f"{self.name} - {self.shift.name}"


class StudentGroup(BaseModel):
    code = models.CharField(
        verbose_name=_("Código"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    reference_year = models.PositiveSmallIntegerField(verbose_name=_("Ano referência"))
    offers = models.PositiveSmallIntegerField(verbose_name=_("Limite de Discentes"))
    serie = models.ForeignKey(
        Serie,
        verbose_name=_("Série"),
        on_delete=models.PROTECT,
        related_name="student_groups",
    )
    students = models.ManyToManyField(
        Student,
        through="Enrollment",
        verbose_name=_("Discentes"),
        related_name="student_groups",
    )

    class Meta:
        verbose_name = _("Turma")
        verbose_name_plural = _("Turmas")

    def __str__(self):
        return f"{self.serie.name}/{self.serie.shift.name}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"{self.serie.shift.code}{self.serie.code}{self.reference_year}"

        super().save(*args, **kwargs)


class Enrollment(BaseModel):
    class Status(models.IntegerChoices):
        ACTIVE = 1, _("Ativa")
        CANCELED = 2, _("Cancelada")
        PENDING = 3, _("Pendente")
        CLOSED = 4, _("Trancada")
        FINISHED = 5, _("Concluída")  # Discente concluiu a oferta de disciplina

    status = models.PositiveSmallIntegerField(
        verbose_name=_("Situação"),
        choices=Status.choices,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=Status.PENDING,
    )

    code = models.CharField(
        verbose_name=_("Código"),
        max_length=constants.SMALL_CHAR_FIELD_NAME_LENGTH,
        unique=True,
    )
    student = models.ForeignKey(
        Student,
        verbose_name=_("Discente"),
        related_name="enrollments",
        on_delete=models.CASCADE,
    )
    student_group = models.ForeignKey(
        StudentGroup,
        verbose_name=_("Turma"),
        related_name="enrollments",
        on_delete=models.CASCADE,
    )
    enrollment_date = models.DateField(
        verbose_name=_("Data de Matrícula"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Matrícula")
        verbose_name_plural = _("Matrículas")

    def __str__(self):
        return f"{self.student.name} matriculado em {self.student_group.code}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"{self.pk}{self.student_group.serie.shift.code}{self.student_group.serie.code}{self.enrollment_date.year}"  # noqa

        super().save(*args, **kwargs)
