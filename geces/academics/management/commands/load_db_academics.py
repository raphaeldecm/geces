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
                    Shift(name="Matutino", created_by=admin),
                    Shift(name="Vespertino", created_by=admin),
                    Shift(name="Noturno", created_by=admin),
                ]
            )
        mat = Shift.objects.get(name="Matutino")
        ves = Shift.objects.get(name="Vespertino")
        if Serie.objects.count() == 0:
            Serie.objects.bulk_create(
                [
                    Serie(name="Maternal", shift=mat, created_by=admin),
                    Serie(name="Maternal", shift=ves, created_by=admin),
                    Serie(name="Nível I", shift=mat, created_by=admin),
                    Serie(name="Nível I", shift=ves, created_by=admin),
                    Serie(name="Nível II", shift=mat, created_by=admin),
                    Serie(name="Nível II", shift=ves, created_by=admin),
                    Serie(name="Nível III", shift=mat, created_by=admin),
                    Serie(name="Nível III", shift=ves, created_by=admin),
                    Serie(name="1° Ano", shift=mat, created_by=admin),
                    Serie(name="1° Ano", shift=ves, created_by=admin),
                    Serie(name="2° Ano", shift=mat, created_by=admin),
                    Serie(name="2° Ano", shift=ves, created_by=admin),
                    Serie(name="3° Ano", shift=mat, created_by=admin),
                    Serie(name="3° Ano", shift=ves, created_by=admin),
                    Serie(name="4° Ano", shift=mat, created_by=admin),
                    Serie(name="4° Ano", shift=ves, created_by=admin),
                    Serie(name="5° Ano", shift=mat, created_by=admin),
                    Serie(name="5° Ano", shift=ves, created_by=admin),
                ]
            )
