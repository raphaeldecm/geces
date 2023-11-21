from django.contrib import admin

from geces.academics import models


# Register your models here.
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("updated_by",)


class SerieAdmin(admin.ModelAdmin):
    list_display = ("name", "shift", "teacher")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("updated_by",)


class StudentGroupAdmin(admin.ModelAdmin):
    search_fields = ["reference_year", "shift__name", "serie__name"]
    ordering = ["reference_year"]
    readonly_fields = ["updated_by"]


admin.site.register(models.Shift, ShiftAdmin)
admin.site.register(models.Serie, SerieAdmin)
admin.site.register(models.StudentGroup, StudentGroupAdmin)
