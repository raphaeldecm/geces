from django.urls import path

from geces.users.views import (
    ThirdUserUpdateView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UsersListView,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="self-update"),
    path("detail/<int:pk>/", view=UserDetailView.as_view(), name="detail"),
    path("list/", view=UsersListView.as_view(), name="list"),
    path("signup/", view=UserCreateView.as_view(), name="signup"),
    path("edit/<int:pk>/", view=ThirdUserUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", view=UserDeleteView.as_view(), name="delete"),
]
