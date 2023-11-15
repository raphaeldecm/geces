from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, TemplateView

from geces.people import forms, models


# Create your views here.
class PeopleHome(LoginRequiredMixin, TemplateView):
    template_name = "people/people.html"


class StudentList(LoginRequiredMixin, ListView):
    model = models.Student
    template_name = "student/student_list.html"
    paginate_by = 10
    ordering = ["name"]


class ResponsbileList(LoginRequiredMixin, ListView):
    model = models.Responsible
    template_name = "responsible/responsible_list.html"
    paginate_by = 10
    ordering = ["name"]


class ResponsibleForm(LoginRequiredMixin, messages.views.SuccessMessageMixin, CreateView):
    model = models.Responsible
    template_name = "responsible/responsible_form.html"
    form_class = forms.ResponsibleForm
    success_message = _("O responsável foi cadastrado com sucesso")
    success_url = reverse_lazy("people:responsible_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'address_form' not in context:
            context['address_form'] = forms.AddressForm()  # Adiciona o formulário de endereço ao contexto
        return context

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)  # Cria o formulário de Address
        if address_form.is_valid():
            responsible = form.save(commit=False)
            address = address_form.save()
            responsible.address = address
            responsible.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Erro ao salvar o formulário. Verifique os campos."))
        return self.render_to_response(self.get_context_data(form=form))
