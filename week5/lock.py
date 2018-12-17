from threading import RLock
import threading
from threading import Thread
import time

a = RLock()
b = RLock()


def foo():
    try:
        a.acquire()
        print("Lock a by ", threading.current_thread().name)
        b.acquire()
        print("Lock b by ", threading.current_thread().name)
    finally:
        a.release()
        print("Release a by ", threading.current_thread().name)
        time.sleep(5)
        b.release()
        print("Release b by ", threading.current_thread().name)


for _ in range(2):
    t = Thread(target=foo)
    t.start()