from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from geces.core.mixins import TitleBaseViewMixin
from geces.people import forms, models
from geces.people.mixins import PeopleCreateViewMixin


# Create your views here.
class PeopleHome(LoginRequiredMixin, TitleBaseViewMixin, generic.TemplateView):
    template_name = "people/people.html"
    title = _("Pessoas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher_count"] = models.Teacher.objects.count()
        context["student_count"] = models.Student.objects.count()
        context["responsible_count"] = models.Responsible.objects.count()
        return context


class StudentList(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Student
    title = _("Lista de Discentes")
    template_name = "student/student_list.html"
    paginate_by = 10
    ordering = ["name"]


class StudentForm(
    LoginRequiredMixin,
    TitleBaseViewMixin,
    messages.views.SuccessMessageMixin,
    PeopleCreateViewMixin,
    generic.CreateView,
):
    model = models.Student
    title = _("Cadastro de Discente")
    template_name = "student/student_form.html"
    form_class = forms.StudentForm
    success_message = _("O discente foi cadastrado com sucesso")
    success_url = reverse_lazy("people:student_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        address_form.created_by = self.request.user
        form.instance.created_by = self.request.user
        if address_form.is_valid():
            responsible_name = form.cleaned_data["responsible"]
            responsible = models.Responsible.objects.filter(name=responsible_name).first()
            student = form.save(commit=False)
            student.responsible = responsible
            address = address_form.save()
            student.address = address
            student.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class StudentDetail(LoginRequiredMixin, TitleBaseViewMixin, generic.DetailView):
    model = models.Student
    title = _("Detalhes do Discente")
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "student/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_group"] = self.get_object().student_groups.all()
        return context


class StudentUpdate(
    LoginRequiredMixin,
    TitleBaseViewMixin,
    messages.views.SuccessMessageMixin,
    PeopleCreateViewMixin,
    generic.UpdateView,
):
    model = models.Student
    title = _("Atualização de Discente")
    template_name = "student/student_form.html"
    form_class = forms.StudentForm
    success_message = _("O discente foi atualizado com sucesso")
    success_url = reverse_lazy("people:student_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        address_form.updated_by = self.request.user
        form.instance.updated_by = self.request.user
        if address_form.is_valid():
            student = form.save(commit=False)
            address = address_form.save()
            student.address = address
            student.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class StudentDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Student
    success_url = reverse_lazy("people:student_list")
    success_message = _("Discente excluído com sucesso!")


class ResponsbileList(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Responsible
    template_name = "responsible/responsible_list.html"
    paginate_by = 10
    ordering = ["name"]
    title = _("Lista de Responsáveis")


class ResponsbileDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Responsible
    success_url = reverse_lazy("people:responsible_list")
    success_message = _("Responsável excluído com sucesso!")


class ResponsbileDetail(LoginRequiredMixin, TitleBaseViewMixin, generic.DetailView):
    model = models.Responsible
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "responsible/responsible_detail.html"
    title = _("Detalhes do Responsável")


class ResponsibleForm(
    LoginRequiredMixin,
    messages.views.SuccessMessageMixin,
    TitleBaseViewMixin,
    PeopleCreateViewMixin,
    generic.CreateView,
):
    model = models.Responsible
    title = _("Cadastro de Responsável")
    template_name = "responsible/responsible_form.html"
    form_class = forms.ResponsibleForm
    success_message = _("O responsável foi cadastrado com sucesso")
    success_url = reverse_lazy("people:responsible_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        address_form.created_by = self.request.user
        form.instance.created_by = self.request.user
        if address_form.is_valid():
            responsible = form.save(commit=False)
            address = address_form.save()
            responsible.address = address
            responsible.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class ResponsibleUpdate(
    LoginRequiredMixin,
    TitleBaseViewMixin,
    messages.views.SuccessMessageMixin,
    PeopleCreateViewMixin,
    generic.UpdateView,
):
    model = models.Responsible
    title = _("Atualização de Responsável")
    template_name = "responsible/responsible_form.html"
    form_class = forms.ResponsibleForm
    success_message = _("O responsável foi atualizado com sucesso")
    success_url = reverse_lazy("people:responsible_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        address_form.updated_by = self.request.user
        form.instance.updated_by = self.request.user
        if address_form.is_valid():
            responsible = form.save(commit=False)
            address = address_form.save()
            responsible.address = address
            responsible.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class TeacherList(LoginRequiredMixin, TitleBaseViewMixin, generic.ListView):
    model = models.Teacher
    title = _("Lista de Professores")
    template_name = "teacher/teacher_list.html"
    paginate_by = 10
    ordering = ["name"]


class TeacherForm(
    LoginRequiredMixin,
    TitleBaseViewMixin,
    messages.views.SuccessMessageMixin,
    PeopleCreateViewMixin,
    generic.CreateView,
):
    model = models.Teacher
    title = _("Cadastro de Professor")
    template_name = "teacher/teacher_form.html"
    form_class = forms.TeacherForm
    success_message = _("O professor foi cadastrado com sucesso")
    success_url = reverse_lazy("people:teacher_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        address_form.created_by = self.request.user
        form.instance.created_by = self.request.user
        if address_form.is_valid():
            teacher = form.save(commit=False)
            address = address_form.save()
            teacher.address = address
            teacher.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class TeacherDetail(LoginRequiredMixin, TitleBaseViewMixin, generic.DetailView):
    model = models.Teacher
    title = _("Detalhes do Professor")
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "teacher/teacher_detail.html"


class TeacherUpdate(
    LoginRequiredMixin,
    TitleBaseViewMixin,
    messages.views.SuccessMessageMixin,
    PeopleCreateViewMixin,
    generic.UpdateView,
):
    model = models.Teacher
    title = _("Atualização de Professor")
    template_name = "teacher/teacher_form.html"
    form_class = forms.TeacherForm
    success_message = _("O professor foi atualizado com sucesso.")
    success_url = reverse_lazy("people:teacher_list")

    @transaction.atomic
    def form_valid(self, form):
        address_form = forms.AddressForm(self.request.POST)
        address_form.updated_by = self.request.user
        form.instance.updated_by = self.request.user
        if address_form.is_valid():
            teacher = form.save(commit=False)
            address = address_form.save()
            teacher.address = address
            teacher.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class TeacherDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Teacher
    success_url = reverse_lazy("people:teacher_list")
    success_message = _("Professor excluído com sucesso!")
