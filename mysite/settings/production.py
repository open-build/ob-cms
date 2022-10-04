from .base import *
import os
from os.path import join, normpath

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buildly-cms',
        'PASSWORD': os.environ.get("PASSWORD"),
        'USER': 'buildly-cms',
        'HOST': 'db-mysql-nyc3-97229-do-user-2508039-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['coral-app-sbh2h.ondigitalocean.app', 'buildly.io', '127.0.0.1', '[::1]','www.buildly.io',]

try:
    from .local import *
except ImportError:
    pass

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new
DEFAULT_FROM_EMAIL = "help@buildly.io"
EMAIL_HOST = "smtp.sendgrid.net"  # new
EMAIL_HOST_USER = "apikey"  # new
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD")  # new
EMAIL_PORT = 587  # new
EMAIL_USE_TLS = True  # new
