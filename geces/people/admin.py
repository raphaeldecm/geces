from django.contrib import admin

from geces.people import models


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    search_fields = ["city", "address", "zip_code"]


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]


class ResponsibleAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "display_series")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("updated_by",)

    def display_series(self, obj):
        return ", ".join([serie.name for serie in obj.series.all()])


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "status", "responsible", "balance")
    readonly_fields = (
        "updated_by",
        "balance",
    )
    search_fields = ["name", "responsible__name"]


admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Suplier, SupplierAdmin)
admin.site.register(models.Responsible, ResponsibleAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Teacher, TeacherAdmin)
