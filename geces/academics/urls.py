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
    path("enrollment_create/", views.EnrollmentCreateView.as_view(), name="enrollment_create"),
    path("enrollment_update/<int:pk>/", views.EnrollmentUpdateView.as_view(), name="enrollment_update"),
    path("enrollment_detail/<int:pk>/", views.EnrollmentDetailView.as_view(), name="enrollment_detail"),
    path("enrollment_delete/<int:pk>/", views.EnrollmentDeleteView.as_view(), name="enrollment_delete"),
    # Group URLs
    path("student_groups/", views.StudentGroupListView.as_view(), name="student_group_list"),
    path("student_group_create/", views.StudentGroupCreateView.as_view(), name="student_group_create"),
    # path("student_group_update/<int:pk>/", views.GroupUpdateView.as_view(), name="student_group_update"),
    # path("student_group_detail/<int:pk>/", views.GroupDetailView.as_view(), name="student_group_detail"),
    # path("student_group_delete/<int:pk>/", views.GroupDeleteView.as_view(), name="student_group_delete"),

]
