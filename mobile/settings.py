import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
ADMIN_MEDIA_PREFIX = '/admin_media/'
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'mobile.dev'             # Or path to database file if using sqlite3.
DEBUG = True
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    
    #external - see requirements.txt
    'flatcontent',
)
LANGUAGE_CODE = 'en-us'
MANAGERS = ADMINS
MEDIA_ROOT = os.path.join(PROJECT_PATH, os.pardir, 'media')
MEDIA_URL = '/media/'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'))
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)
TIME_ZONE = 'America/Chicago'
ROOT_URLCONF = 'mobile.urls'
SITE_ID = 1
USE_I18N = True