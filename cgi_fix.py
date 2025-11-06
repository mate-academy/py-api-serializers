"""
Patch para compatibilidade com Python 3.13
"""
import sys
import types

# Criar um módulo cgi fake para compatibilidade
if 'cgi' not in sys.modules:
    cgi_module = types.ModuleType('cgi')
    cgi_module.parse_header = lambda x: (x, {})
    sys.modules['cgi'] = cgi_module

# Agora importe o Django
import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'rest_framework',
            'cinema',
            'user',
        ],
        REST_FRAMEWORK={
            'DEFAULT_RENDERER_CLASSES': [
                'rest_framework.renderers.JSONRenderer',
            ],
        },
        USE_TZ=True,
    )

django.setup()
