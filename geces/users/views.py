from django.contrib.auth import get_user_model, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.views.generic import DetailView, RedirectView, UpdateView

from .forms import UserAdminCreationForm

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


class UsersListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5
    ordering = ["name"]


class UserBaseMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_groups"] = models.Group.objects.all()
        return context


class UserCreateView(UserBaseMixin, views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserAdminCreationForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário cadastrado com sucesso!")
    template_name = "users/signup.html"


class ThirdUserUpdateView(UserBaseMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = User
    form_class = UserAdminCreationForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário atualizado com sucesso!")
    template_name = "users/signup.html"
