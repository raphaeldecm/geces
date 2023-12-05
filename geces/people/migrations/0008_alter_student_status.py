# Generated by Django 4.2.6 on 2023-12-05 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0007_alter_responsible_cpf_alter_student_cpf_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Pendente"), (2, "Matriculado"), (3, "Cursando")],
                default=1,
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)],
                verbose_name="Situação",
            ),
        ),
    ]