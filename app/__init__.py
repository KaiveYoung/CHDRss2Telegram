from celery import Celery
from celery.signals import worker_process_init
from celery.schedules import schedule
from instance.config import CELERY_BROKER
celery = Celery(
    'chd_rss',
    broker=CELERY_BROKER,
    include=[
        'app.tasks',
    ]
)
celery.conf.timezone = 'UTC'


celery.conf.beat_schedule = {
    'task_clean_sch': {
        'task': 'chdrss',
        'schedule': schedule(run_every=60),
        'args': (),
    },
}



@worker_process_init.connect()
def worker_process_init(*args, **kwargs):
    from app.ext import redis,telegram
    redis.init_app()
    telegram.init_app()