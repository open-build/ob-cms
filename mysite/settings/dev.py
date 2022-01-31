from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4w$$of)udb)qv8=vs^5vy#8%9+kk73x0u$de0dxg2xl+@s^v1g'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']

INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar",]

INTERNAL_IPS = [
    "localhost",
    "127.0.0.1",
]

try:
    from .local import *
except ImportError:
    pass
