import multiprocessing
import os

workers = int(os.getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1))

max_requests = 1000
max_requests_jitter = 50

bind = "0.0.0.0:8000"
reload = True
