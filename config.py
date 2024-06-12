import multiprocessing
import os

workers = int(os.getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1))
threads = workers # it may vary depending on the application, if it is CPU-bound or I/O-bound

max_requests = 1000
max_requests_jitter = 50

bind = "0.0.0.0:8000"
reload = True
