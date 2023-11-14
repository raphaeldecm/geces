from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from geces.academics.models import Serie, Shift

User = get_user_model()


class Command(BaseCommand):
    help = "Load academics database"

    def handle(self, *args, **options):
        admin = User.objects.filter(is_superuser=True).first()

        if Shift.objects.count() == 0:
            Shift.objects.bulk_create(
                [
                    Shift(
                        name="Matutino", created_by=admin
                    ),
                    Shift(
                        name="Vespertino", created_by=admin
                    ),
                    Shift(
                        name="Noturno", created_by=admin
                    ),
                ]
            )

        if Serie.objects.count() == 0:
            Serie.objects.bulk_create(
                [
                    Serie(name="Nível I", created_by=admin),
                    Serie(name="Nível II", created_by=admin),
                    Serie(name="Nível III", created_by=admin),
                    Serie(name="Alfabetização", created_by=admin),
                    Serie(name="1° Ano", created_by=admin),
                    Serie(name="2° Ano", created_by=admin),
                    Serie(name="3° Ano", created_by=admin),
                    Serie(name="4° Ano", created_by=admin),
                ]
            )
