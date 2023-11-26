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
                    Shift(code="01", name="Matutino", created_by=admin),
                    Shift(code="02", name="Vespertino", created_by=admin),
                    Shift(code="03", name="Noturno", created_by=admin),
                ]
            )
        mat = Shift.objects.get(name="Matutino")
        ves = Shift.objects.get(name="Vespertino")
        if Serie.objects.count() == 0:
            Serie.objects.bulk_create(
                [
                    Serie(code=f"01{mat.code}", name="Maternal", shift=mat, created_by=admin),
                    Serie(code=f"01{ves.code}", name="Maternal", shift=ves, created_by=admin),
                    Serie(code=f"02{mat.code}", name="Nível I", shift=mat, created_by=admin),
                    Serie(code=f"02{ves.code}", name="Nível I", shift=ves, created_by=admin),
                    Serie(code=f"03{mat.code}", name="Nível II", shift=mat, created_by=admin),
                    Serie(code=f"03{ves.code}", name="Nível II", shift=ves, created_by=admin),
                    Serie(code=f"04{mat.code}", name="Nível III", shift=mat, created_by=admin),
                    Serie(code=f"04{ves.code}", name="Nível III", shift=ves, created_by=admin),
                    Serie(code=f"05{mat.code}", name="1° Ano", shift=mat, created_by=admin),
                    Serie(code=f"05{ves.code}", name="1° Ano", shift=ves, created_by=admin),
                    Serie(code=f"06{mat.code}", name="2° Ano", shift=mat, created_by=admin),
                    Serie(code=f"06{ves.code}", name="2° Ano", shift=ves, created_by=admin),
                    Serie(code=f"07{mat.code}", name="3° Ano", shift=mat, created_by=admin),
                    Serie(code=f"07{ves.code}", name="3° Ano", shift=ves, created_by=admin),
                    Serie(code=f"08{mat.code}", name="4° Ano", shift=mat, created_by=admin),
                    Serie(code=f"08{ves.code}", name="4° Ano", shift=ves, created_by=admin),
                    Serie(code=f"09{mat.code}", name="5° Ano", shift=mat, created_by=admin),
                    Serie(code=f"09{ves.code}", name="5° Ano", shift=ves, created_by=admin),
                ]
            )
