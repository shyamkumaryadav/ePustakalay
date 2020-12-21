from django.apps import AppConfig
from django.db.models.signals import post_migrate


class EmanagementConfig(AppConfig):
    name = 'e_library'

    def ready(self):
        from e_library import signals
        post_migrate.connect(
            signals.create_info,
            sender=self
        )
