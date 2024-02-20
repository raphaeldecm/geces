from django.contrib.auth.mixins import UserPassesTestMixin


class DirectorPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Diretor")


class SellerPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Vendedor")


class SecretaryPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Secretário")
