from django.contrib.auth import get_user_model, models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, RedirectView, UpdateView
from django_filters.views import FilterView

from geces.core.mixins import TitleBaseViewMixin

from .filters import UserFilterSet
from .forms import UserAdminCreationForm

User = get_user_model()


class UserUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
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


class UsersListView(LoginRequiredMixin, TitleBaseViewMixin, FilterView):
    model = User
    title = _("Lista de Usuários")
    paginate_by = 5
    ordering = ["name"]
    filterset_class = UserFilterSet
    template_name = "users/user_list.html"
    queryset = User.objects.filter(is_superuser=False).exclude(email="deleted")


class UserBaseMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_groups"] = models.Group.objects.all()
        return context


class UserCreateView(UserBaseMixin, TitleBaseViewMixin, LoginRequiredMixin, views.SuccessMessageMixin, CreateView):
    model = User
    title = _("Cadastro de Usuário")
    form_class = UserAdminCreationForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário cadastrado com sucesso!")
    template_name = "users/signup.html"


class ThirdUserUpdateView(
    UserBaseMixin, TitleBaseViewMixin, LoginRequiredMixin, views.SuccessMessageMixin, UpdateView
):
    model = User
    title = _("Atualização de Usuário")
    form_class = UserAdminCreationForm
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário atualizado com sucesso!")
    template_name = "users/signup.html"


class UserDeleteView(LoginRequiredMixin, views.SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users:list")
    success_message = _("Usuário excluído com sucesso!")


class UserDetailView(UserBaseMixin, TitleBaseViewMixin, LoginRequiredMixin, DetailView):
    model = User
    title = _("Detalhes do Usuário")
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "users/user_detail.html"
