import csv
from datetime import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

STUDENTS_CSV = str(settings.APPS_DIR / "people" / "bin" / "students_responsibles.csv")


class Command(BaseCommand):
    help = "Load people database"

    def handle(self, *args, **options):
        admin = User.objects.filter(is_superuser=True).first()

        with open(STUDENTS_CSV, encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Acessando os dados de cada coluna do CSV
                name = row["Nome"]
                serie = row["Curso"]
                birth_date = datetime.strptime(row["Nascimento"], "%d/%m/%Y").date()
                Nacionalidade = row["Nacionalidade"]
                Naturalidade = row["Naturalidade"]
                gender = row["Sexo"]
                fone = row["Telefones"]
                Endereco = f"row['Endereco'], row['Bairro']"
                cidade = row['Cidade']
                cep = row['CEP']

                print("### ", name, serie, birth_date, Nacionalidade, Naturalidade, gender, fone, Endereco, cidade, cep)


                # Crie um objeto Address
                # address = Address.objects.create(
                #     country_state=state,
                #     city=row['Cidade'],
                #     address=row['Endereco'],
                #     zip_code=row['Cep'],
                #     phone=row['Telefone']
                # )

                # Crie um objeto Person
                # person = Person.objects.create(
                #     name=name,
                #     gender=gender,
                #     birth_date=birth_date,
                #     cpf=cpf,
                #     # ... Outros campos do modelo Person
                # )

                # Crie um objeto Student relacionado ao objeto Person criado acima
                # student = Student.objects.create(
                #     person=person,
                #     status=row['Situacao'],
                #     # ... Outros campos do modelo Student
                # )
                # Adicione os campos restantes conforme necessário'
