from django.contrib import admin

from geces.people import models

# Register your models here.


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ["person__name", "email"]


class ResponsibleAdmin(admin.ModelAdmin):
    search_fields = ["person__name", "email"]


class StudentAdmin(admin.ModelAdmin):
    fields = [
        "created_by",
        "person",
        "status",
        "responsible",
    ]
    readonly_fields = ("updated_by", "balance", )
    search_fields = ["person__name", "responsible__name"]


class StudentGroupAdmin(admin.ModelAdmin):
    search_fields = ["reference_year", "shift__name", "serie__name"]
    ordering = ["reference_year"]
    readonly_fields = ["updated_by"]


admin.site.register(models.StudentGroup, StudentGroupAdmin)
admin.site.register(models.Suplier, SupplierAdmin)
admin.site.register(models.Responsible, ResponsibleAdmin)
admin.site.register(models.Student, StudentAdmin)
