"""
WSGI config for guess_word_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guess_word_site.settings")

os.environ['DJANGO_SETTINGS_MODULE'] = 'guess_word_site.settings'
os.environ['LC_ALL']="es_ES.UTF-8"

application = get_wsgi_application()
