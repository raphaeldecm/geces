from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect


class TitleBaseViewMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class ProtectedMessageMixin:

    protected_message = None

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.warning(self.request, self.protected_message)
            return redirect(self.request.META.get("HTTP_REFERER"))
