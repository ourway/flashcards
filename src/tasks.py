# celery tasks module with redis as broker

import time

from celery import Celery

app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    broker_connection_retry_on_startup=True,
)


@app.task
def add(x, y):
    time.sleep(10)
    return x + y
