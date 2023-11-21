# Generated by Django 4.2.6 on 2023-11-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0002_remove_student_responsible_student_and_more"),
        ("academics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentgroup",
            name="students",
            field=models.ManyToManyField(related_name="student_groups", to="people.student", verbose_name="Discentes"),
        ),
    ]
