from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, ExpressionWrapper, F, IntegerField
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
        context["student_groups_count"] = models.StudentGroup.objects.count()
        context["enrollments_count"] = models.Enrollment.objects.count()
        return context


class SerieListView(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Serie
    template_name = "series/series_list.html"
    paginate_by = 10
    title = _("Lista de Séries")


class SerieCreateView(LoginRequiredMixin, TitleBaseViewMixin, messages.views.SuccessMessageMixin, generic.CreateView):
    model = models.Serie
    title = _("Cadastro de Matrícula")
    template_name = "series/serie_form.html"
    form_class = forms.SerieForm
    success_url = reverse_lazy("academics:serie_list")
    success_message = _("A série foi cadastrada com sucesso")


class SerieUpdateView(LoginRequiredMixin, TitleBaseViewMixin, messages.views.SuccessMessageMixin, generic.UpdateView):
    model = models.Serie
    title = _("Atualização de Série")
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


class EnrollmentListView(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Enrollment
    template_name = "enrollments/enrollment_list.html"
    paginate_by = 10
    title = _("Lista de Matrículas")


class EnrollmentDetailView(LoginRequiredMixin, TitleBaseViewMixin, generic.DetailView):
    model = models.Enrollment
    title = _("Detalhes da Matrícula")
    template_name = "enrollments/enrollment_detail.html"
    title = _("Detalhes da Matrícula")


class EnrollmentCreateView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.CreateView):
    model = models.Enrollment
    title = _("Cadastro de Matrícula")
    template_name = "enrollments/enrollment_form.html"
    form_class = forms.EnrollmentForm
    success_url = reverse_lazy("academics:enrollment_list")
    success_message = _("A matrícula foi cadastrada com sucesso")


class EnrollmentUpdateView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.UpdateView):
    model = models.Enrollment
    title = _("Atualização de Matrícula")
    template_name = "enrollments/enrollment_form.html"
    form_class = forms.EnrollmentForm
    success_url = reverse_lazy("academics:enrollment_list")
    success_message = _("A matrícula foi atualizada com sucesso")


class EnrollmentDeleteView(LoginRequiredMixin, messages.views.SuccessMessageMixin, generic.DeleteView):
    model = models.Enrollment
    success_url = reverse_lazy("academics:enrollment_list")
    success_message = _("A matrícula foi excluída com sucesso")


class StudentGroupListView(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.StudentGroup
    template_name = "student_group/student_group_list.html"
    paginate_by = 10
    title = _("Lista de Turmas")
    ordering = ["serie__name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_groups"] = models.StudentGroup.objects.annotate(
            num_students=Count('students'),
            percentage=ExpressionWrapper(
                (F('num_students') * 100.0) / F('offers'),
                output_field=IntegerField()
            )
        )
        return context

# TODO: Select reference year to filter student groups


class StudentGroupCreateView(
    LoginRequiredMixin, TitleBaseViewMixin, messages.views.SuccessMessageMixin, generic.CreateView
):
    model = models.StudentGroup
    title = _("Cadastro de Turma")
    template_name = "student_group/student_group_form.html"
    form_class = forms.StudentGroupForm
    success_url = reverse_lazy("academics:student_group_list")
    success_message = _("A turma foi cadastrada com sucesso")


class StudentGroupUpdateView(
    LoginRequiredMixin, TitleBaseViewMixin, messages.views.SuccessMessageMixin, generic.UpdateView
):
    model = models.StudentGroup
    title = _("Atualização de Turma")
    template_name = "student_group/student_group_form.html"
    form_class = forms.StudentGroupForm
    success_url = reverse_lazy("academics:student_group_list")
    success_message = _("A turma foi atualizada com sucesso")
