from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render  # noqa: F401
from django.views.generic import ListView

from . import models


# Create your views here.
class StudentList(LoginRequiredMixin, ListView):
    model = models.Student
    template_name = "student/student_list.html"
    paginate_by = 10
    ordering = ["person__name"]
