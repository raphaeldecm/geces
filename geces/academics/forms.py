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


class EnrollmentForm(forms.ModelForm):
    reference_year = forms.ChoiceField(
        choices=[],
        label="Ano referência"
    )
    student_group = forms.ModelChoiceField(
        queryset=StudentGroup.objects.all(),
        label="Turma",
        required=False,
        empty_label=_("Selecione um ano de referência"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_year = date.today().year
        choices = [
            ("", "---------"),
            (current_year, current_year),
            (current_year + 1, current_year + 1)
        ]
        self.fields["reference_year"] = forms.ChoiceField(
            choices=choices,
            label=_("Ano referência"),
        )
        self.fields["student_group"].widget.attrs["disabled"] = True

    def clean_student_group(self):
        student_group = self.cleaned_data.get("student_group")

        if student_group:
            if student_group.enrollments.count() >= student_group.offers:
                raise forms.ValidationError(_("Esta turma já atingiu o limite de discentes"))
            try:
                student_group = StudentGroup.objects.get(pk=student_group.pk)
                return student_group
            except StudentGroup.DoesNotExist:
                raise forms.ValidationError("Turma não encontrada.")

        return student_group

    def clean(self):
        cleaned_data = super().clean()
        reference_year = cleaned_data.get("reference_year")
        student = cleaned_data.get("student")

        if reference_year and student:
            if Enrollment.objects.filter(student=student, student_group__reference_year=reference_year).exists():
                raise forms.ValidationError(_("Já existe uma matrícula para este aluno e ano referência selecionados!"))
        return cleaned_data

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
