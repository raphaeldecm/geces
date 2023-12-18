from django.contrib import admin

from geces.canteen import models


class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name", "price"]
    readonly_fields = ["updated_by"]


class PurchaseAdmin(admin.ModelAdmin):
    search_fields = ["supplier", "products"]
    readonly_fields = ["updated_by"]


class SellAdmin(admin.ModelAdmin):
    search_fields = ["student", "products"]
    readonly_fields = ["updated_by"]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.Sell, SellAdmin)
