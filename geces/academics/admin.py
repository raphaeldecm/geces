from django.contrib import admin

from geces.academics.models import Serie, Shift


# Register your models here.
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("updated_by", )


class SerieAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("updated_by", )


admin.site.register(Shift, ShiftAdmin)
admin.site.register(Serie, SerieAdmin)
