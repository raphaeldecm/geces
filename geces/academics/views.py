from django.shortcuts import render  # noqa
from django.views import generic

# Create your views here.


class AcademicsView(generic.TemplateView):
    template_name = "academics/academics.html"
