from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render  # noqa: F401
from django.views.generic import CreateView, ListView, TemplateView

from geces.people import forms, models


# Create your views here.
class PeopleHome(LoginRequiredMixin, TemplateView):
    template_name = "people/people.html"


class StudentList(LoginRequiredMixin, ListView):
    model = models.Student
    template_name = "student/student_list.html"
    paginate_by = 10
    ordering = ["person__name"]


class ResponsbileList(LoginRequiredMixin, ListView):
    model = models.Responsible
    template_name = "responsible/responsible_list.html"
    paginate_by = 10
    ordering = ["person__name"]


class ResponsibleForm(LoginRequiredMixin, CreateView):
    model = models.Responsible
    template_name = "responsible/responsible_form.html"
    form_class = forms.ResponsibleForm
