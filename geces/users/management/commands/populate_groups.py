from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Load resources database"

    def handle(self, *args, **options):
        groups = ["Diretor", "Secretário", "Vendedor"]
        [Group.objects.get_or_create(name=group) for group in groups]
