# multi_threaded.py
import time
import threading
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        #print('current thread {}, n={}'.format(threading.current_thread().getName(), n))
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
