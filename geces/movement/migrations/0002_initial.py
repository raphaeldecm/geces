# Generated by Django 4.2.6 on 2023-10-11 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geces.core.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("movement", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sell",
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
            model_name="sell",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                related_name="vendas",
                through="movement.ProductSell",
                to="movement.product",
                verbose_name="Produtos",
            ),
        ),
        migrations.AddField(
            model_name="sell",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vendas",
                to="people.student",
                verbose_name="Estudante",
            ),
        ),
        migrations.AddField(
            model_name="sell",
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
            model_name="purchase",
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
            model_name="purchase",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                related_name="compras",
                through="movement.ProductPurchase",
                to="movement.product",
                verbose_name="Produtos",
            ),
        ),
        migrations.AddField(
            model_name="purchase",
            name="supplier",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="compras",
                to="people.suplier",
                verbose_name="Fornecedor",
            ),
        ),
        migrations.AddField(
            model_name="purchase",
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
            model_name="productsell",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_sell",
                to="movement.product",
                verbose_name="Produto",
            ),
        ),
        migrations.AddField(
            model_name="productsell",
            name="sell",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_sell",
                to="movement.sell",
                verbose_name="Venda",
            ),
        ),
        migrations.AddField(
            model_name="productpurchase",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_purchase",
                to="movement.product",
                verbose_name="Produto",
            ),
        ),
        migrations.AddField(
            model_name="productpurchase",
            name="purchase",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_purchase",
                to="movement.purchase",
                verbose_name="Compra",
            ),
        ),
        migrations.AddField(
            model_name="product",
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
            model_name="product",
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
