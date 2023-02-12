from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings
from logging.config import dictConfig
from celery.signals import setup_logging

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treasury.settings")
app = Celery("treasury")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@setup_logging.connect
def config_loggers(*args, **kwags):
    dictConfig(settings.LOGGING)
