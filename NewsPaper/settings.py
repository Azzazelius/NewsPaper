"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+we5kk%w^4t0po-iobq9%(1dkn$#l6_f0b-ewk7#4)i!ix&1$y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'NewsPaper', # Проект
    'news', # Приложение
    'accounts',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'templates'],
        # 'DIRS': [],
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



WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
LOGIN_REDIRECT_URL = "/posts"
LOGOUT_REDIRECT_URL= "/posts"




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = '/registration/base/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'news.models.BasicSignupForm'}

DEFAULT_FROM_EMAIL = 'Pupapekainos@yandex.com'

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'Pupapekainos'  # ваше имя пользователя, например, если ваша почта user@yandex.ru,
                                  # то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'pxkzxpmkusgaognw'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках,
                        # но включать его здесь обязательно

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CELERY_BROKER_URL = 'redis://default:LUmQ0FOlqLbSGkRVL9DfHfXhMiyqdvf2@redis-17703.c293.eu-central-1-1.ec2.cloud.redislabs.com:17703'  # — указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://default:LUmQ0FOlqLbSGkRVL9DfHfXhMiyqdvf2@redis-17703.c293.eu-central-1-1.ec2.cloud.redislabs.com:17703'  # — указывает на хранилище результатов выполнения задач.
CELERY_ACCEPT_CONTENT = ['application/json']  # — допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json'  # — метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json'  # — метод сериализации результатов.


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    # ======================================================
    # =======================  formatters
    # ======================================================
    'formatters': {
        'form_console_debug': {
            'format': '%(asctime)s %(levelname)s %(message)s '
        },
        'form_console_warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'form_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'form_general_info': {
            'format': '%(levelname)s %(modul)s %(message)s'
        },
        'form_security': {
            'format': '%(asctime)s %(levelname)s %(modul)s %(message)s'
        },
        'form_mail': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
    },
    # ======================================================
    # =======================  filters
    # ======================================================
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # ======================================================
    # =======================  handlers
    # ======================================================
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler', #выводит лог в консоль
            'formatter': 'form_console_debug'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_console_warning'
        },
        'console_critical': {
            'level': 'CRITICAL',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_critical'
        },
        'general_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'form_general_info'
        },
        'file_critical': {
            'level': 'CRITICAL',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'form_critical'
        },
        'file_security': {
            'level': 'NOTSET',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'form_security'
        },
        'log_mail': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'form_mail'
        },
    },
    # ======================================================
    # =======================  loggers
    # ======================================================
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_critical', 'general_info']
        },
        'django.request': {
            'handlers': ['file_critical', 'log_mail'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_critical', 'log_mail'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_critical'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_critical'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'NOTSET',
            'propagate': False,
        }
    }
}

