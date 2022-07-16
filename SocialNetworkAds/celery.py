import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialNetworkAds.settings')

app = Celery('SocialNetworkAds')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
