from threading import RLock
import threading
from threading import Thread
import time

a = RLock()
b = RLock()


def foo():
    print("f1: a = {} b = {}".format(a, b))
    a.acquire()
    time.sleep(1)
    b.acquire()
    a.release()
    b.release()


def foo2():
    print("f2: a = {} b = {}".format(a, b))
    b.acquire()
    time.sleep(1)
    a.acquire()
    b.release()
    a.release()


for _ in range(2):
    Thread(target=foo).start()
    Thread(target=foo2).start()