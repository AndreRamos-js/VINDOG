from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings



os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Vindog.settings')

app = Celery('Vindog')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()
