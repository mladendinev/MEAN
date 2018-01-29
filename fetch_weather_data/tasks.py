from celery import Celery
from celery.utils.log import get_task_logger
from weather_stream import fetchData

app = Celery('tasks')

logger = get_task_logger(__name__)
app.config_from_object('celeryconfig')


@app.task
def collect_data_15_mins():
    print fetchData()