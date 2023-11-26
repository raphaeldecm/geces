from django.urls import path

from . import views

app_name = "academics"
urlpatterns = [
    path("", views.AcademicsHome.as_view(), name="academics_home"),
]
