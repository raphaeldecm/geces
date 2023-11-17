from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from geces.people import forms, models
from geces.people.mixins import PeopleCreateViewMixin


# Create your views here.
class PeopleHome(LoginRequiredMixin, generic.TemplateView):
    template_name = "people/people.html"


class StudentList(LoginRequiredMixin, generic.ListView):
    model = models.Student
    template_name = "student/student_list.html"
    paginate_by = 10
    ordering = ["name"]


class ResponsbileList(LoginRequiredMixin, generic.ListView):
    model = models.Responsible
    template_name = "responsible/responsible_list.html"
    paginate_by = 10
    ordering = ["name"]


class ResponsibleForm(
    LoginRequiredMixin, messages.views.SuccessMessageMixin, PeopleCreateViewMixin, generic.CreateView
):
    model = models.Responsible
    template_name = "responsible/responsible_form.html"
    form_class = forms.ResponsibleForm
    success_message = _("O responsável foi cadastrado com sucesso")
    success_url = reverse_lazy("people:responsible_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        if address_form.is_valid():
            responsible = form.save(commit=False)
            address = address_form.save()
            responsible.address = address
            responsible.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class ResponsibleUpdate(
    LoginRequiredMixin, messages.views.SuccessMessageMixin, PeopleCreateViewMixin, generic.UpdateView
):
    model = models.Responsible
    template_name = "responsible/responsible_form.html"
    form_class = forms.ResponsibleForm
    success_message = _("O responsável foi cadastrado com sucesso")
    success_url = reverse_lazy("people:responsible_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        if address_form.is_valid():
            responsible = form.save(commit=False)
            address = address_form.save()
            responsible.address = address
            responsible.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
