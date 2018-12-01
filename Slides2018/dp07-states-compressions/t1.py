# single_threaded.py
import time
import threading
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        #print('current thread {}, n={}'.format(threading.current_thread().getName(), n))
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)
