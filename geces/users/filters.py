import django_filters
from django.contrib.auth.models import Group

from .models import User


class UserFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Nome')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    is_active = django_filters.BooleanFilter(label='Active')
    group = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), label='Grupo', field_name='groups')

    class Meta:
        model = User
        fields = ('name', 'email', 'is_active', 'group')
