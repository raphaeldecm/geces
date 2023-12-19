from django.contrib import admin

from geces.finance import models


# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "status", "type", "value", "due_date")
    search_fields = ("enrollment__student__name",)
    ordering = ("due_date",)
    readonly_fields = ("updated_by",)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_type", "invoice", "value", "discount", "observations")
    search_fields = ("invoice__enrollment__student__name",)
    ordering = ("created_at",)
    readonly_fields = ("updated_by",)


admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Payment, PaymentAdmin)
