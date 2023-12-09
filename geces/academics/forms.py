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
        fields = ["status", "student", "student_group"]


class StudentGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["code"].required = False
        current_year = date.today().year
        choices = [(current_year, current_year), (current_year + 1, current_year + 1)]
        self.fields["reference_year"] = forms.ChoiceField(
            choices=choices,
            label=_("Ano referência"),
        )

    def clean(self):
        cleaned_data = super().clean()
        reference_year = cleaned_data.get("reference_year")
        serie = cleaned_data.get("serie")

        if reference_year and serie:
            if StudentGroup.objects.filter(serie=serie, reference_year=reference_year).exists():
                raise forms.ValidationError(_("Já existe uma turma para esta série e ano referência"))
            else:
                cleaned_data["code"] = f"{serie.shift.code}{serie.code}{reference_year}"
        return cleaned_data

    class Meta:
        model = StudentGroup
        fields = ["code", "serie", "offers", "reference_year"]
        labels = {
            "serie": _("Série"),
            "offers": _("Vagas"),
        }
