from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from geces.people import forms


class PeopleCreateViewMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'address_form' not in context:
            context['address_form'] = forms.AddressForm()
        return context

    def form_invalid(self, form):
        messages.error(self.request, _("Erro ao salvar o formulário. Verifique os campos."))
        return self.render_to_response(self.get_context_data(form=form))
