"""
ASGI config for generador_de_palabras_aleatorias project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generador_de_palabras_aleatorias.settings')

application = get_asgi_application()
