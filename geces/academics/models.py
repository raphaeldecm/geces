from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.core import constants
from geces.core.models import BaseModel
from geces.people.models import Student, Teacher


# Create your models here.
class Shift(BaseModel):
    name = models.CharField(verbose_name=_("Nome"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH, unique=True)

    class Meta:
        verbose_name = _("Turno")
        verbose_name_plural = _("Turnos")

    def __str__(self):
        return self.name


class Serie(BaseModel):
    name = models.CharField(verbose_name=_("Nome"), max_length=constants.MAX_CHAR_FIELD_NAME_LENGTH)
    shift = models.ForeignKey(
        Shift,
        verbose_name=_("Turno"),
        on_delete=models.PROTECT,
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