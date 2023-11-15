# Generated by Django 4.2.6 on 2023-11-15 00:15

from django.conf import settings
from django.db import migrations, models
import geces.core.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("academics", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="shift",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET(geces.core.models.get_sentinel_user),
                related_name="created_%(app_label)s_%(class)s_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="shift",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET(geces.core.models.get_sentinel_user),
                related_name="updated_%(app_label)s_%(class)s_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updated by",
            ),
        ),
        migrations.AddField(
            model_name="serie",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET(geces.core.models.get_sentinel_user),
                related_name="created_%(app_label)s_%(class)s_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Created by",
            ),
        ),
        migrations.AddField(
            model_name="serie",
            name="updated_by",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET(geces.core.models.get_sentinel_user),
                related_name="updated_%(app_label)s_%(class)s_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Updated by",
            ),
        ),
    ]
