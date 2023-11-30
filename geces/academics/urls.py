from django.urls import path

from . import views

app_name = "academics"
urlpatterns = [
    path("", views.AcademicsHome.as_view(), name="academics_home"),
    # Serie URLs
    path("series/", views.SerieListView.as_view(), name="serie_list"),
    path("serie_create/", views.SerieCreateView.as_view(), name="serie_create"),
    path("serie_update/<int:pk>/", views.SerieUpdateView.as_view(), name="serie_update"),
    path("serie_detail/<int:pk>/", views.SerieDetailView.as_view(), name="serie_detail"),
    path("serie_delete/<int:pk>/", views.SerieDeleteView.as_view(), name="serie_delete"),
    # Enrollment URLs
    path("enrollments/", views.EnrollmentListView.as_view(), name="enrollment_list"),
]
