import django_filters
from django import forms

from geces.academics.models import StudentGroup


class StudentGroupFilterSet(django_filters.FilterSet):
    code = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Código",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    serie = django_filters.ModelMultipleChoiceFilter(
        queryset=StudentGroup.objects.all(),
        label="Série",
        field_name="serie",
        required=False,
        help_text="Selecione uma ou mais séries.",
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )
    offers = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Vagas",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        years = StudentGroup.objects.values_list("reference_year", flat=True).distinct()
        year_choices = [(year, year) for year in years]
        self.filters["reference_year"] = django_filters.ChoiceFilter(
            field_name="reference_year",
            label="Filtrar por ano letivo",
            choices=year_choices,
            widget=forms.Select(attrs={"class": "form-select"}),
        )

    class Meta:
        model = StudentGroup
        fields = ("code", "serie", "offers", "reference_year")
