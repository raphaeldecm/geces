from django.urls import path

from . import views

app_name = "people"
urlpatterns = [
    path("", views.PeopleHome.as_view(), name="people_home"),
    # Responsible URLs
    path("responsible_list/", views.ResponsbileList.as_view(), name="responsible_list"),
    path("responsible_form/", views.ResponsibleForm.as_view(), name="responsible_form"),
    path("responsible_edit/<int:pk>/", views.ResponsibleUpdate.as_view(), name="responsible_edit"),
    path("responsible_detail/<int:pk>/", views.ResponsbileDetail.as_view(), name="responsible_detail"),
    path("responsible_delete/<int:pk>/", views.ResponsbileDelete.as_view(), name="responsible_delete"),
    # Teacher URLs
    path("teacher_list/", views.TeacherList.as_view(), name="teacher_list"),
    path("teacher_form/", views.TeacherForm.as_view(), name="teacher_form"),
    path("teacher_detail/<int:pk>/", views.TeacherDetail.as_view(), name="teacher_detail"),
    path("teacher_edit/<int:pk>/", views.TeacherUpdate.as_view(), name="teacher_edit"),
    path("teacher_delete/<int:pk>/", views.TeacherDelete.as_view(), name="teacher_delete"),
    # Student URLs
    path("student_list/", views.StudentList.as_view(), name="student_list"),
    path("student_form/", views.StudentForm.as_view(), name="student_form"),
    path("student_detail/<int:pk>/", views.StudentDetail.as_view(), name="student_detail"),
    path("student_edit/<int:pk>/", views.StudentUpdate.as_view(), name="student_edit"),
    path("student_delete/<int:pk>/", views.StudentDelete.as_view(), name="student_delete"),
]
