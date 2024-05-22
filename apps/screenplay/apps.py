from django.apps import AppConfig


class ScreenplayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.screenplay'

    def ready(self):
        import apps.screenplay.signals
