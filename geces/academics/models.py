from django.db import models
from django.utils.translation import gettext_lazy as _

from geces.core.constants import MAX_CHAR_FIELD_NAME_LENGTH
from geces.core.models import BaseModel


# Create your models here.
class Shift(BaseModel):
    name = models.CharField(
        verbose_name=_("Nome"), max_length=MAX_CHAR_FIELD_NAME_LENGTH, unique=True
    )

    class Meta:
        verbose_name = _("Turno")
        verbose_name_plural = _("Turnos")

    def __str__(self):
        return self.name


class Serie(BaseModel):
    name = models.CharField(
        verbose_name=_("Nome"), max_length=MAX_CHAR_FIELD_NAME_LENGTH, unique=True
    )

    class Meta:
        verbose_name = _("Série")
        verbose_name_plural = _("Séries")

    def __str__(self):
        return self.name
