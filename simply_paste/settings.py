import os
import sys
import dj_database_url


# Django settings for simply_paste project.

# some helpers to make live easier
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
STATIC_DEBUG = DEBUG
REQUIRE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {'default': dj_database_url.config()}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
        '.pasterly.com',
        'localhost',
        'simply-paste-testing.herokuapp.com',
        'simply-paste.herokuapp.com',
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Boise'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
if STATIC_DEBUG:
    STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# STATICFILES_STORAGE = 'require.storage.OptimizedCachedStaticFilesStorage'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '5&rngu$j5yc=che82*w%$=l4n!3o1p2q7-+3tpv!o0%35p!kb7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simply_paste.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'simply_paste.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    # style apps
    'assets',
    'django_admin_bootstrapped',
    'vendor',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    # 3rd party
    'gunicorn',
    'rest_framework',
    'sekizai',
    'south',
    'require',
    'storages',

    # local
    'snippets',
)

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
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# django-require settings, an app that implements require.js on a django server

# The baseUrl to pass to the r.js optimizer.
REQUIRE_BASE_URL = "js"

# The name of a build profile to use for your project, relative to REQUIRE_BASE_URL.
# A sensible value would be 'app.build.js'. Leave blank to use the built-in default build profile.
REQUIRE_BUILD_PROFILE = 'simply-paste.build.js'

# The name of the require.js script used by your project, relative to REQUIRE_BASE_URL.
REQUIRE_JS = "require-jquery.js"

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {}


# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: auto, node or rhino.
# auto will autodetect the environment and make use of node if available and rhino if not.
# It can also be a path to a custom class that subclasses require.environments.Environment and defines some "args" function that returns a list with the command arguments to execute.
REQUIRE_ENVIRONMENT = "node"

AWS_STORAGE_BUCKET_NAME = "pasterly"
AWS_SECRET_ACCESS_KEY   = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_ACCESS_KEY_ID       = os.environ['AWS_ACCESS_KEY_ID']
AWS_URL                 = 'https://'+AWS_STORAGE_BUCKET_NAME+'.s3.amazonaws.com/'
AWS_S3_CUSTOM_DOMAIN    = 'd3uh7ya8h9x9la.cloudfront.net'
# AWS_URL                 = 'https://d3uh7ya8h9x9la.cloudfront.net/'

# django-storage settings
STORAGE_S3          = 'S3'
STORAGE_REQUIRE     = 'REQUIRE'
STORAGE_S3_REQUIRE  = 'S3_REQUIRE'
STORAGE_DEBUG       = 'DEBUG'

# STORAGE_METHOD = STORAGE_S3
# STORAGE_METHOD = STORAGE_S3_REQUIRE
if DEBUG:
    STORAGE_METHOD = STORAGE_DEBUG
else:
    STORAGE_METHOD = STORAGE_S3_REQUIRE

# TODO: join url strings properly to be slash agnostic
# S3
if STORAGE_METHOD == STORAGE_S3:
    DEFAULT_FILE_STORAGE    = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE     = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL              = AWS_URL + 'static/'
    MEDIA_URL               = AWS_URL + 'media/'
    ADMIN_MEDIA_PREFIX      = AWS_URL + 'static/admin/'
# django-require
if STORAGE_METHOD == STORAGE_REQUIRE:
    DEFAULT_FILE_STORAGE    = 'require.storage.OptimizedStaticFilesStorage'
    STATICFILES_STORAGE     = 'require.storage.OptimizedStaticFilesStorage'
    STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
# django-require + S3
if STORAGE_METHOD == STORAGE_S3_REQUIRE:
    DEFAULT_FILE_STORAGE    = 'snippets.storage.OptimizedS3BotoStorage'
    STATICFILES_STORAGE     = 'snippets.storage.OptimizedS3BotoStorage'
    STATIC_URL              = AWS_URL + 'static/'
    MEDIA_URL               = AWS_URL + 'media/'
    ADMIN_MEDIA_PREFIX      = AWS_URL + 'static/admin/'


