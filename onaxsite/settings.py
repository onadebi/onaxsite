"""
Django settings for onaxsite project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path;
from decouple import config;
import os;
import re;

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print(f"===========BASE_DIR: {BASE_DIR}=========")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

# CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'https://onaxsys.com','onaxsys.com','.onaxsys.com','www.onaxsys.com','https://www.onaxsys.com','*']
CORS_ALLOWED_ORIGINS = ['http://localhost', 'http://127.0.0.1', 'https://onaxsys.com','https://onaxsys.com','https://www.onaxsys.com']
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.onaxsys\.com$",  # Allows all subdomains of example.com
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Application definition

INSTALLED_APPS = [
    "poll.apps.PollConfig", # This is the app we created
    # "onaxmain", # This is the app we created
    'common',
    'corsheaders',
    'blog.apps.BlogConfig',
    'onaxmain.apps.OnaxmainConfig', # This is the app we created
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_BASEPATH = BASE_DIR / "staticfiles"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "exportpdf",
    }
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onaxsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'onaxmain/templates/onaxmain'),
                 os.path.join(BASE_DIR, 'common/templates/blog'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onaxsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
     # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    # 'default':{
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': config('DJANGO_DB_NAME'), # database name
    #     'USER': config('DJANGO_DB_USER'),
    #     'PASSWORD': config('DJANGO_DB_PASSWORD'),
    #     'HOST': config('DJANGO_DB_HOST'),
    #     'PORT': config('DJANGO_DB_PORT'), 
    # }
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DJANGO_DB_NAME'), # database name
        'USER': config('DJANGO_DB_USER'),
        'HOST': config('DJANGO_DB_HOST'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),# config('DJANGO_DB_PASSWORD'),
        'PORT': config('DJANGO_DB_PORT'), 
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    # BASE_DIR / "static",
    BASE_DIR / "blog/static",
    # "/var/www/static/",
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
