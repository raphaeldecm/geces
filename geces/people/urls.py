from django.urls import path

from . import views

app_name = "people"
urlpatterns = [
    path('student_list/', views.StudentList.as_view(), name="student_list"),
]
