import django_filters
from django import forms
from django.contrib.auth.models import Group

from .models import User


class UserFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    email = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    is_active = django_filters.BooleanFilter(
        label="Ativo",
        widget=django_filters.widgets.BooleanWidget(
            attrs={
                "class": "form-select",
            }
        ),
    )
    group = django_filters.ModelMultipleChoiceFilter(
        queryset=Group.objects.all(),
        label="Grupos",
        field_name="groups",
        required=False,
        help_text="Selecione um ou mais grupos.",
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("name", "email", "is_active", "group")
