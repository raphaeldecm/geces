from django.urls import resolve, reverse

from geces.users.models import User


def test_detail(user: User):
    assert reverse("users:detail", kwargs={"pk": user.pk}) == f"/users/detail/{user.pk}/"
    assert resolve(f"/users/detail/{user.pk}/").view_name == "users:detail"


def test_update():
    assert reverse("users:self-update") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:self-update"


def test_redirect():
    assert reverse("users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:redirect"
