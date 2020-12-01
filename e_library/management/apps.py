from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ManagementConfig(AppConfig):
    name = 'management'

    def ready(self):
        from management import signals
        post_migrate.connect(
            signals.create_genre,
            sender=self
        )
