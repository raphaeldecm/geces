from datetime import date

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Enrollment, Serie, StudentGroup


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["code", "name", "shift", "teacher"]
        labels = {
            "name": _("Nome"),
            "shift": _("Turno"),
            "teacher": _("Professor"),
        }


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["student", "student_group"]
        labels = {
            "student": _("Aluno"),
        }


class StudentGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_year = date.today().year
        choices = [(current_year, current_year), (current_year + 1, current_year + 1)]
        self.fields["reference_year"] = forms.ChoiceField(
            choices=choices,
            label=_("Ano referência"),
        )

    class Meta:
        model = StudentGroup
        fields = ["serie", "offers", "reference_year"]
        labels = {
            "serie": _("Série"),
            "offers": _("Vagas"),
        }
