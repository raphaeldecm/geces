# Generated by Django 4.2.6 on 2023-11-15 00:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("city", models.CharField(max_length=255, verbose_name="Cidade")),
                ("address", models.CharField(max_length=255, verbose_name="Endereço")),
                ("zip_code", models.CharField(max_length=8, verbose_name="CEP")),
                ("phone", models.CharField(max_length=11, verbose_name="Telefone")),
            ],
            options={
                "verbose_name": "Endereço",
                "verbose_name_plural": "Endereços",
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                ("email", models.EmailField(max_length=100, verbose_name="E-mail")),
                ("phone", models.CharField(max_length=100, verbose_name="Telefone")),
                (
                    "gender",
                    models.CharField(
                        choices=[("MALE", "Masculino"), ("FEMALE", "Feminino")], max_length=50, verbose_name="Gênero"
                    ),
                ),
            ],
            options={
                "verbose_name": "Pessoa",
                "verbose_name_plural": "Pessoas",
            },
        ),
        migrations.CreateModel(
            name="StudentGroup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("code", models.CharField(max_length=50, unique=True, verbose_name="Código")),
                ("reference_year", models.PositiveSmallIntegerField(verbose_name="Ano referência")),
            ],
            options={
                "verbose_name": "Turma",
                "verbose_name_plural": "Turmas",
            },
        ),
        migrations.CreateModel(
            name="Responsible",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="people.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "Responsável",
                "verbose_name_plural": "Responsáveis",
            },
            bases=("people.person",),
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="people.person",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Pendente"), (2, "Matriculado"), (3, "Cursando")],
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(8),
                        ],
                        verbose_name="Situação",
                    ),
                ),
                ("balance", models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Saldo")),
            ],
            options={
                "verbose_name": "Discente",
                "verbose_name_plural": "Discentes",
            },
            bases=("people.person",),
        ),
        migrations.CreateModel(
            name="Suplier",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="people.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fornecedor",
                "verbose_name_plural": "Fornecedores",
            },
            bases=("people.person",),
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="people.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "Professor",
                "verbose_name_plural": "Professores",
            },
            bases=("people.person",),
        ),
    ]
