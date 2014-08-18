# -*- coding: utf-8 -*-
''' Production Configurations

Adds sensiable default for running app in production.
'''
from __future__ import unicode_literals, absolute_import
from configurations import values
from .common import Common


class Production(Common):

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue('postgres://animate:password@localhost/animate_web')
    # END DATABASE CONFIGURATION

    # SECRET KEY
    SECRET_KEY = values.SecretValue('w)ca-a0xdt1!*m%uf0829_)^&w@(=x&ygzeymy1=1av)z#^*%e')
    # END SECRET KEY

    # django-secure
    INSTALLED_APPS += (
        "djangosecure", 
        "s3_folder_storage", # static and media to S3 seperately
    )

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # end django-secure

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    INSTALLED_APPS += ("gunicorn", )

    # STORAGE CONFIGURATION
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += ('storages', )

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
    try:
        from S3 import CallingFormat
        AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
    except ImportError:
        pass

    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.Value('AKIAIEF4J3Q2TEXCN4PA ')
    AWS_SECRET_ACCESS_KEY = values.Value('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')
    AWS_STORAGE_BUCKET_NAME = values.Value('animate_web')
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False

    # see: https://github.com/antonagestam/collectfast
    AWS_PRELOAD_METADATA = True
    INSTALLED_APPS += ("collectfast", )

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIREY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
            AWS_EXPIREY, AWS_EXPIREY)
    }

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
    # END STORAGE CONFIGURATION

    try:
        # see: https://github.com/rdegges/django-heroku-memcacheify#install
        # Avoids installing of pylibmc on development enviroment
        from memcacheify import memcacheify
        CACHES = memcacheify()
    except ImportError:
        CACHES = values.CacheURLValue(default="memcached://127.0.0.1:11211")

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
    # END TEMPLATE CONFIGURATION

    # Your production stuff: Below this line define 3rd party libary settings
