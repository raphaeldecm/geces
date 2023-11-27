from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Serie


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["code", "name", "shift", "teacher"]
        labels = {
            "name": _("Nome"),
            "shift": _("Turno"),
            "teacher": _("Professor"),
        }