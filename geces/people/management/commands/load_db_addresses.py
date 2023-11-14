from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from geces.people.models import State

User = get_user_model()

ADDRESS_JSON = str(settings.APPS_DIR / "adresses" / "bin" / "address_sample.json")


class Command(BaseCommand):
    help = "Load addresses database"

    def handle(self, *args, **options):
        admin = User.objects.filter(is_superuser=True).first()

        state_data = self.get_state_data()
        for state_abbreviation, state_name in state_data:
            state, _ = State.objects.get_or_create(
                abbreviation=state_abbreviation,
                defaults={
                    "name": state_name,
                    "created_by": admin,
                    "updated_by": admin,
                },
            )

    def get_state_data(self):
        return [
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AM", "Amazonas"),
            ("AP", "Amapá"),
            ("BA", "Bahia"),
            ("CE", "Ceará"),
            ("DF", "Brasília"),
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MG", "Minas Gerais"),
            ("MS", "Mato Grosso do Sul"),
            ("MT", "Mato Grosso"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("PR", "Paraná"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("RS", "Rio Grande do Sul"),
            ("SC", "Santa Catarina"),
            ("SE", "Sergipe"),
            ("SP", "São Paulo"),
            ("TO", "Tocantins"),
            ("EX", "Exterior"),
        ]
