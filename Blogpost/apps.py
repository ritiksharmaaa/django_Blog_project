from django.apps import AppConfig


class BlogpostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blogpost'
    def ready(self):
        import Blogpost.signals