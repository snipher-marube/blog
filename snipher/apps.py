from django.apps import AppConfig



class SnipherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'snipher'

    def ready(self):
        import snipher.signals
