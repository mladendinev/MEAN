from datetime import timedelta

BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULE = {
    'fetchWeatherData': {
        'task': 'tasks.collect_data_15_mins',
        'schedule': timedelta(minutes=30),
        'args': ()
    },

}
