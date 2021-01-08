from django.apps import AppConfig
from django.db.models.signals import post_migrate


class EmanagementConfig(AppConfig):
    name = 'emanagement'

    def ready(self):
        from emanagement import signals
        post_migrate.connect(
            signals.create_genre,
            sender=self
        )
