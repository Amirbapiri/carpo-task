import os
from celery import Celery
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.local')
django.setup()

celery = Celery('config')
celery.config_from_object('django.conf:django', namespace='CELERY')
celery.autodiscover_tasks()

celery.conf.beat_schedule = {
    'your-periodic-task': {
        'task': 'monitoring.sensors.tasks.generate_sensor_data',
        'schedule': 5.0,  # Run every 1 second
    },
}