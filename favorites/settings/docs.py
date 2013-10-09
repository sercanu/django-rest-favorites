__author__ = 'user'

from base import *


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
