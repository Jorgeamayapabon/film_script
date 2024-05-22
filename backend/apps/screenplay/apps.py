from django.apps import AppConfig


class ScreenplayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.screenplay'

    def ready(self):
        import backend.apps.screenplay.signals
