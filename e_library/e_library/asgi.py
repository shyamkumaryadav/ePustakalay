"""
ASGI config for e_library project.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_library.settings')

application = get_asgi_application()
