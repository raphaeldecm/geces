# Generated by Django 4.2.6 on 2023-12-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("academics", "0003_enrollment_serie_alter_enrollment_student_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment",
            name="serie",
        ),
        migrations.AddField(
            model_name="studentgroup",
            name="offers",
            field=models.PositiveSmallIntegerField(default=1, verbose_name="Limite de Discentes"),
            preserve_default=False,
        ),
    ]