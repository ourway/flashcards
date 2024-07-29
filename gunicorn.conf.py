# gunicorn config file

import multiprocessing


def on_starting(server):
    server.log.info("Starting gunicorn...")


bind = ":8000"
workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
timeout = 30
keepalive = 2
max_requests = 4096
max_requests_jitter = 512
reload = True
accesslog = "-"
errorlog = "-"
loglevel = "info"
