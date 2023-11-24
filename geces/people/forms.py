from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Address, Responsible, Student, Teacher


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["city", "address", "zip_code", "phone"]
        widgets = {
            "address": forms.TextInput(attrs={"placeholder": _("Rua, número, bairro")}),
            "zip_code": forms.TextInput(attrs={"placeholder": _("59.000-000")}),
            "phone": forms.TextInput(attrs={"placeholder": _("(99) 99999-9999")}),
        }


class ResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ["id", "name", "email", "gender", "birth"]
        widgets = {
            "birth": forms.DateInput(
                attrs={"placeholder": _("dd/mm/aaaa"), "data-input": "data-input", "type": "date"}
            )
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["id", "name", "email", "gender", "birth"]
        widgets = {
            "birth": forms.DateInput(
                attrs={"placeholder": _("dd/mm/aaaa"), "data-input": "data-input", "type": "date"}
            )
        }


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["id", "name", "email", "gender", "birth", "responsible"]
        widgets = {
            "birth": forms.DateInput(
                attrs={"placeholder": _("dd/mm/aaaa"), "data-input": "data-input", "type": "date"}
            ),
            "responsible": forms.TextInput(attrs={"placeholder": _("Nome do responsável")}),
        }
