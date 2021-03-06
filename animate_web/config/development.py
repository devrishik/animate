# -*- coding: utf-8 -*-
''' Development Configurations

Adds sensible defaults for developement of project
- Enables DEBUG
- Outputs outgoing emails to console
- Enables Django Debug Toolbar
- Uses local caches
'''
from __future__ import unicode_literals, absolute_import
from configurations import values
from .common import Common


class Development(Common):

    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    # DATABASES = values.DatabaseURLValue('postgres://animate_web@localhost/animate_web')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            #'NAME': normpath(join(DJANGO_ROOT,'hotelnow')), # for sqllite
            'NAME': 'animate',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
    # END DATABASE CONFIGURATION

    # Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel', ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # end django-debug-toolbar

    # CACHES
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }
    # END OF CACHES

    # Your local stuff: Below this line define 3rd party libary settings
