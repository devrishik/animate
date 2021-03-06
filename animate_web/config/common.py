# -*- coding: utf-8 -*-
'''Django settings for Animate project.

see: https://docs.djangoproject.com/en/dev/ref/settings/
'''

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname

from configurations import Configuration, values

BASE_DIR = dirname(dirname(__file__))


# Common Configurations
# ==============================================================================
class Common(Configuration):
    '''Common Configuration, overide them in it's sub-classes.'''

    # APP CONFIGURATION
    # -----------------
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'south',  # Database migration helpers
        'django_extensions',  # http://django-extensions.readthedocs.org/
        'rest_framework',
    )

    LOCAL_APPS = (
        # Your stuff: custom apps go here
        'pages',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    # MIDDLEWARE CONFIGURATION
    # Note: Order in which they are added are important
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    # END MIDDLEWARE CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    # Defaults to false, which is safe, enable them only in development.
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG

    # SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    #       In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = "CHANGEME_TO_SOME_S3CRET_VALUE!!!"
    # END SECRET CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )

    # MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('Animate admin', 'noreply@example.com'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    # END MANAGER CONFIGURATION

    # EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # END EMAIL CONFIGURATION

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

    SITE_ID = 1

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'UTC'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # TEMPLATE CONFIGURATION
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION

    # URL Configuration
    ROOT_URLCONF = 'urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'
    # End URL Configuration

    # AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
    )

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    # END LOGGING CONFIGURATION

    REST_FRAMEWORK = { 'PAGINATE_BY': 20}

    ########## CELERY CONFIGURATION
    import datetime
    BROKER_URL = 'redis://localhost:6379/0'
    # BROKER_TRANSPORT_OPTIONS = {'polling_interval': 0.3}
    CELERY_TIMEZONE = TIME_ZONE
    CELERY_TASK_SERIALIZER = 'pickle'
    CELERY_ACCEPT_CONTENT=['pickle']
    #========Periodic Tasks
    # CELERYBEAT_SCHEDULE = {
    # 'get-feeds-every-10-secs': {
    # 'task': 'core.tasks.update_latest_feed',
    # 'schedule': datetime.timedelta(seconds=10),
    # },
    # 'check-alert-thresholds': {
    # 'task': 'core.tasks.check_alert_thresholds',
    # 'schedule': datetime.timedelta(minutes=1),
    # },
    # }
    #========End Periodic Tasks
    ########## END CELERY CONFIGURATION
