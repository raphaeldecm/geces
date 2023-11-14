from django.urls import path

from . import views

app_name = "people"
urlpatterns = [
    path('home/', views.PeopleHome.as_view(), name="people_home"),
    path('student_list/', views.StudentList.as_view(), name="student_list"),
    path('responsible_list/', views.ResponsbileList.as_view(), name="responsible_list"),
    path('responsible_form/', views.ResponsibleForm.as_view(), name="responsible_form"),
]
