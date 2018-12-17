from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

n = 500_000_000


def count(d):
    while d > 0:
        d -= 1


def run(*args):
    if 1 in args:
        start = time.time()
        count(n)
        count(n)
        print('1. No parallel:    {}'.format(time.time() - start))

    if 2 in args:
        start = time.time()
        t1 = Thread(target=count, args={n})
        t2 = Thread(target=count, args={n})

        t1.start(), t2.start()
        t1.join(), t2.join()
        print('2. Threads:        {}'.format(time.time() - start))

    if 3 in args:
        start = time.time()
        with ThreadPoolExecutor(max_workers=4) as pool:
            pool.submit(count(n))
            pool.submit(count(n))
        print('3. ThreadPool:     {}'.format(time.time() - start))

    if 4 in args:
        start = time.time()
        p1 = Process(target=count, args={n})
        p2 = Process(target=count, args={n})

        p1.start(), p2.start()
        p1.join(), p2.join()
        print('4. ProcessPool:    {}'.format(time.time() - start))

    if 5 in args:
        start = time.time()
        with ProcessPoolExecutor(max_workers=4) as pool:
            pool.submit(count(n))
            pool.submit(count(n))
        print('5. Process:        {}'.format(time.time() - start))


if __name__ == "__main__":
    run(1, 2, 3, 4, 5)
