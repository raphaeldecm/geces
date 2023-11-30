from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render  # noqa
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from geces.core.mixins import TitleBaseViewMixin

from . import forms, models

# Create your views here.


class AcademicsHome(generic.TemplateView):
    template_name = "academics/academics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series_count"] = models.Serie.objects.count()
        context["student_groups"] = models.StudentGroup.objects.count()
        return context


class SerieListView(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Serie
    template_name = "series/series_list.html"
    paginate_by = 10
    title = _("Lista de Séries")


class EnrollmentListView(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Enrollment
    template_name = "enrollments/enrollment_list.html"
    paginate_by = 10
    title = _("Lista de Matrículas")


class SerieCreateView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.CreateView):
    model = models.Serie
    template_name = "series/serie_form.html"
    form_class = forms.SerieForm
    success_url = reverse_lazy("academics:serie_list")
    success_message = _("A série foi cadastrada com sucesso")


class SerieUpdateView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.UpdateView):
    model = models.Serie
    template_name = "series/serie_form.html"
    form_class = forms.SerieForm
    success_url = reverse_lazy("academics:serie_list")
    success_message = _("A série foi atualizada com sucesso")


class SerieDetailView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.DetailView):
    model = models.Serie
    template_name = "series/serie_detail.html"


class SerieDeleteView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.DeleteView):
    model = models.Serie
    success_url = reverse_lazy("academics:serie_list")
    success_message = _("A série foi excluída com sucesso")
