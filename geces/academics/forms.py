from datetime import date

from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms

from geces.academics.models import Enrollment, Serie, StudentGroup
from geces.people import models


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["code", "name", "shift", "teachers"]
        labels = {
            "name": _("Nome"),
            "shift": _("Turno"),
            "teachers": _("Docentes"),
        }

# TODO: Refactor this form ti use select2 on student field and filter student_group by year


class EnrollmentForm(forms.ModelForm):
    reference_year = forms.ChoiceField(
        choices=[],
        label="Ano referência"
    )
    student_group = forms.ModelChoiceField(
        queryset=StudentGroup.objects.none(),
        label="Turma",
        required=False,
        empty_label="Selecione o Ano de Referência"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_year = date.today().year
        choices = [(current_year, current_year), (current_year + 1, current_year + 1)]
        self.fields["reference_year"] = forms.ChoiceField(
            choices=choices,
            label=_("Ano referência"),
        )

    class Meta:
        model = Enrollment
        fields = ["status", "student", "student_group"]
        widgets = {
            "student": s2forms.ModelSelect2Widget(
                model=models.Student,
                search_fields=["name__icontains"],
            ),
        }


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
