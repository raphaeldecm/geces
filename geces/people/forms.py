from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms

from .models import Address, Responsible, Student, Teacher


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["city", "address", "zip_code", "phone"]
        widgets = {
            "address": forms.TextInput(attrs={"placeholder": _("Rua, número, bairro")}),
            "zip_code": forms.TextInput(attrs={
                "placeholder": _("59.000-000"),
                "onkeydown": "mask(this, maskZipCode)",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": _("(99) 99999-9999"),
                "onkeydown": "mask(this, maskPhone)",
            }),
        }


class ResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ["id", "name", "email", "cpf", "gender", "birth"]
        widgets = {
            "birth": forms.DateInput(
                attrs={"placeholder": _("dd/mm/aaaa"), "data-input": "data-input", "type": "date"}
            ),
            "cpf": forms.TextInput(attrs={
                "placeholder": _("999.999.999-99"),
                "onkeydown": "mask(this, maskCPF)",
            }),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["id", "name", "email", "cpf", "gender", "birth"]
        widgets = {
            "birth": forms.DateInput(
                attrs={"placeholder": _("dd/mm/aaaa"), "data-input": "data-input", "type": "date"}
            ),
            "cpf": forms.TextInput(attrs={
                "placeholder": _("999.999.999-99"),
                "onkeydown": "mask(this, maskCPF)",
            }),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["id", "name", "email", "gender", "birth", "responsible"]
        widgets = {
            "birth": forms.DateInput(
                attrs={"placeholder": _("dd/mm/aaaa"), "data-input": "data-input", "type": "date"}
            ),
            "responsible": s2forms.ModelSelect2Widget(
                model=Responsible,
                search_fields=["name__icontains"],
            ),
        }
