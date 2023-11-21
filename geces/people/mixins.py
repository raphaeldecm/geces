from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from geces.people import forms


class PeopleCreateViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "address_form" not in context:
            if getattr(self, "object", None):
                context["address_form"] = forms.AddressForm(instance=getattr(self, "object", None).address)
            else:
                context["address_form"] = forms.AddressForm()
        return context

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        messages.error(self.request, _("Erro ao salvar o formulário. Verifique os campos."))
        context["address_form"] = forms.AddressForm(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form, address_form=context["address_form"]))
