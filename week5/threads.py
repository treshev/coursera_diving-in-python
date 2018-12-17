from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time


def f(a):
    while a > 0:
        a -= 1


def run(*args):

    if 1 in args:
        start = time.time()

        f(10_000_000)
        f(10_000_000)
        f(10_000_000)
        # f(10_000_000)
        print("1. No parallel time:  {}".format(time.time() - start))

    if 2 in args:
        start = time.time()
        t1 = Thread(target=f, args={10_000_000})
        t2 = Thread(target=f, args={10_000_000})
        t3 = Thread(target=f, args={10_000_000})
        # t4 = Thread(target=f, args={10_000_000})

        t1.start(), t2.start(), t3.start()
        t1.join(), t2.join(), t3.join()
        print("2. Threads time:      {}".format(time.time() - start))

    if 3 in args:
        start = time.time()
        with ThreadPoolExecutor(max_workers=4) as pool:
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
        print("3. Thread pool time:  {}".format(time.time() - start))

    if 4 in args:
        start = time.time()
        p1 = Process(target=f, args={10_000_000})
        p2 = Process(target=f, args={10_000_000})
        p3 = Process(target=f, args={10_000_000})
        # p4 = Process(target=f, args={10_000_000})

        p1.start(), p2.start(), p3.start()
        p1.join(), p2.join(), p3.join()
        print("4. Process time:      {}".format(time.time() - start))

    if 5 in args:
        start = time.time()
        with ProcessPoolExecutor(max_workers=4) as pool:
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
            pool.submit(f(10_000_0000))
        print("5. Process pool time: {}".format(time.time() - start))


if __name__ == "__main__":
    run(3,5)
