from django.contrib import admin

from geces.people import models

# Register your models here.


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]


class ResponsibleAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]


class StudentAdmin(admin.ModelAdmin):
    search_fields = ["name", "serie", "responsible__name"]


admin.site.register(models.Suplier, SupplierAdmin)
admin.site.register(models.Responsible, ResponsibleAdmin)
admin.site.register(models.Student, StudentAdmin)
