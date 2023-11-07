from django.shortcuts import render  # noqa: F401
from django.views.generic import TemplateView

from geces.users.models import User


# Create your views here.
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
