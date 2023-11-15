from django.contrib import admin

from geces.people import models


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    search_fields = ["city", "address", "zip_code"]


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]


class ResponsibleAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]


class StudentAdmin(admin.ModelAdmin):
    fields = [
        "created_by",
        "status",
        "responsible",
    ]
    readonly_fields = ("updated_by", "balance", )
    search_fields = ["name", "responsible__name"]


class StudentGroupAdmin(admin.ModelAdmin):
    search_fields = ["reference_year", "shift__name", "serie__name"]
    ordering = ["reference_year"]
    readonly_fields = ["updated_by"]


admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.StudentGroup, StudentGroupAdmin)
admin.site.register(models.Suplier, SupplierAdmin)
admin.site.register(models.Responsible, ResponsibleAdmin)
admin.site.register(models.Student, StudentAdmin)
