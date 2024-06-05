#import multiprocessing

#cpu_cores = multiprocessing.cpu_count()

workers = 2

#workers = cpu_cores * 2 + 1
max_requests = 1000
max_requests_jitter = 50
bind = '127.0.0.1:8000'
reload = True