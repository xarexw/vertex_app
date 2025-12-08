import os
from celery import Celery

# встановлюємо налаштування Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# налаштування Celery з config/settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# автоматичне виявлення задач у файлах tasks.py в усіх INSTALLED_APPS
app.autodiscover_tasks()

# реєстрація періодичних задач (crontab)
app.conf.beat_schedule = {
    'check-expired-subs-every-day': {
        'task': 'subscriptions.tasks.check_expired_subs',
        'schedule': 86400.0, # 86400 секунд = 1 раз на добу
    },
    'recalculate-client-stats-hourly': {
        'task': 'users.tasks.recalculate_client_stats',
        'schedule': 3600.0, # 1 раз на годину (для демонстрації)
    },
}