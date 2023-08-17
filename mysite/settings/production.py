from .base import *
import os
from os.path import join, normpath

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms',
        'PASSWORD': os.environ.get("PASSWORD"),
        'USER': 'cms_user',
        'HOST': 'db-mysql-nyc3-97229-do-user-2508039-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['ob-cms-dwtkh.ondigitalocean.app', 'open.build', '127.0.0.1', '[::1]','www.open.build','ukraine.open.build','colombia.open.build']

try:
    from .local import *
except ImportError:
    pass

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://6975369468324c3baa02b389ee8dcbeb@o1380602.ingest.sentry.io/6693855",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new
DEFAULT_FROM_EMAIL = "help@open.build"
EMAIL_HOST = "smtp.sendgrid.net"  # new
EMAIL_HOST_USER = "apikey"  # new
EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD")  # new
EMAIL_PORT = 587  # new
EMAIL_USE_TLS = True  # new

AWS_STORAGE_BUCKET_NAME = 'open-build'
AWS_ACCESS_KEY_ID = 'DO00MW9V6QPPJKVCGHYA'
AWS_SECRET_ACCESS_KEY = os.environ.get("SPACES_SECRET")
AWS_S3_CUSTOM_DOMAIN = 'cms-static.nyc3.digitaloceanspaces.com' + "/" + AWS_STORAGE_BUCKET_NAME
AWS_S3_ENDPOINT_URL  = 'https://cms-static.nyc3.digitaloceanspaces.com'


MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + "/" + AWS_STORAGE_BUCKET_NAME + "/"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

AWS_DEFAULT_ACL = 'public-read'

SENDGRID_API_KEY = os.environ.get("SENDGRID")