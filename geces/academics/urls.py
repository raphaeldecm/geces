from django.urls import path

from . import views

app_name = "academics"
urlpatterns = [
    path("", views.AcademicsView.as_view(), name="academics_home"),
]
