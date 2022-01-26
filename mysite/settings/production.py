from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms',
        'PASSWORD': '9IIaOVhIoBgQNyNG',
        'USER': 'cms_user',
        'HOST': 'db-mysql-nyc3-97229-do-user-2508039-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['ob-cms-dwtkh.ondigitalocean.app', '*.open.build', '127.0.0.1', '[::1]']

try:
    from .local import *
except ImportError:
    pass
