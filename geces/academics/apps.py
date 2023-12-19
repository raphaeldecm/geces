from django.apps import AppConfig


class AcademicsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "geces.academics"

    def ready(self):
        import geces.academics.signals  # noqa F401 # pylint: disable=unused-import
