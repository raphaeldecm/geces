from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    ADMIN_NAME = "Geces Admin"
    ADMIN_EMAIL = "admin@geces.com"
    help = "Adding superuser..."

    def handle(self, *args, **options):
        exists = User.objects.filter(is_superuser=True).exists()

        if exists:
            self.stdout.write("The superuser already exists")
        else:
            User.objects.create(
                name=self.ADMIN_NAME,
                email=self.ADMIN_EMAIL,
                password="argon2$argon2id$v=19$m=102400,t=2,p=8$eG8zRVpIMlNnRnJsd2s1eVNSZ3gxdA$riNO8kaJ8ouNqHGYZNQ504yc7AAyIQQQB4JIhzabyok",  # noqa: E501
                is_superuser=True,
                is_staff=True,
            )
