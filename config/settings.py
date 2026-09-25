"""
Django settings for Rupesh Portfolio project.

Generated for Rupesh Pathak — Computer Science Student & Aspiring Software / AI Engineer.
Configured for development with SQLite by default, ready for PostgreSQL in production.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

# Load environment variables from .env if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / '.env')
except ImportError:
    pass


# ============================================================
# SECURITY
# ============================================================

# SECRET_KEY must be provided through an environment variable.
# Do NOT put your real production secret key directly in this file.
SECRET_KEY = os.getenv('SECRET_KEY')

# DEBUG:
# Local development  -> DEBUG=True
# Production          -> DEBUG=False
DEBUG = os.getenv(
    'DEBUG',
    'True'
).strip().lower() in ('true', '1', 'yes')


# Allowed hosts
ALLOWED_HOSTS_STR = os.getenv(
    'ALLOWED_HOSTS',
    '127.0.0.1,localhost'
)

ALLOWED_HOSTS = [
    host.strip()
    for host in ALLOWED_HOSTS_STR.split(',')
    if host.strip()
]

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost'
    ]


# HTTPS / Cookie security
#
# These are controlled through environment variables so that
# local HTTP development continues to work normally.
#
# Production values will be enabled on the hosting server.

SECURE_SSL_REDIRECT = os.getenv(
    'SECURE_SSL_REDIRECT',
    'False'
).strip().lower() in ('true', '1', 'yes')

SESSION_COOKIE_SECURE = os.getenv(
    'SESSION_COOKIE_SECURE',
    'False'
).strip().lower() in ('true', '1', 'yes')

CSRF_COOKIE_SECURE = os.getenv(
    'CSRF_COOKIE_SECURE',
    'False'
).strip().lower() in ('true', '1', 'yes')


# ============================================================
# APPLICATION DEFINITION
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Portfolio Application
    'portfolio',
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ============================================================
# URL / WSGI CONFIGURATION
# ============================================================

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.context_processors.portfolio_globals',
            ],
        },
    },
]

# ============================================================
# DATABASE
# ============================================================

# Supports:
#
# Local development:
#     SQLite
#
# Production:
#     PostgreSQL using DATABASE_URL
#

DATABASE_URL = os.getenv('DATABASE_URL', '')

if DATABASE_URL:

    try:
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.config(
                default=DATABASE_URL,
                conn_max_age=600,
                conn_health_checks=True,
            )
        }

    except ImportError:

        # Fallback to SQLite if dj-database-url
        # is not installed.
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator',
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ============================================================
# MEDIA FILES
# ============================================================

# User uploads:
# - project screenshots
# - resume
# - profile photo

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# DJANGO MESSAGES FRAMEWORK
# ============================================================

# Map Django message tags to Bootstrap 5 alert classes.

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}