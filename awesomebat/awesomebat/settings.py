import string
import os

import dj_database_url
from decouple import Csv, config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config('SECRET_KEY', default=string.ascii_letters)

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'allauth', 
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'sorl.thumbnail',
]


LOCAL_APPS = [
    'apps.core.apps.CoreConfig',
    'apps.users.apps.UsersConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

SITE_ID = 1

INTERNAL_IPS = ['127.0.0.1']

if config("USE_DOCKER", default=False, cast=bool):
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

ROOT_URLCONF = 'awesomebat.urls'

WSGI_APPLICATION = 'awesomebat.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_USER_MODEL = 'users.CustomUser'

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

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


LOGIN_REDIRECT_URL = 'home'

LOGIN_URL = 'account_login'

ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

# ACCOUNT_EMAIL_VERIFICATION = "none"

# SOCIALACCOUNT_EMAIL_VERIFICATION = "none"


# ==============================================================================
# INTERNATIONALIZATION AND LOCALIZATION SETTINGS
# ==============================================================================

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('vi', _('Vietnamese')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_SUBJECT_PREFIX = config('DEFAULT_FROM_EMAIL', default='[Django Bat]')

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='hocdjango@gmail.com')

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

EMAIL_HOST = config('EMAIL_HOST', default='localhost')

EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)

EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='root')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)


# ==============================================================================
# STATIC & MEDIA FILES SETTINGS
# ==============================================================================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/public')

PRIVATE_MEDIA_ROOT = os.path.join(BASE_DIR, 'media/private')


# ==============================================================================
# CACHE SETTINGS
# ==============================================================================


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

CRISPY_TEMPLATE_PACK = 'bootstrap4'
