from django.shortcuts import render  # noqa
from django.views import generic

from . import models

# Create your views here.


class AcademicsHome(generic.TemplateView):
    template_name = "academics/academics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = models.Series.objects.all()
        context["student_groups"] = models.StudentGroup.objects.all()
        return context
    
