import os
from celery import Celery
import multiprocessing

# Fix Windows multiprocessing
multiprocessing.set_start_method('spawn', force=True)

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_project.settings')  # ✅ Your project name here

app = Celery('csv_project')

# Load custom settings from Django settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks from all installed apps automatically
app.autodiscover_tasks()