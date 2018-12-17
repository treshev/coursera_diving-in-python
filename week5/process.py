import os
import time
from multiprocessing import Process

def f(name, wait):
    time.sleep(int(wait))
    print("Pid {} = {}".format(name, os.getpid()))



if __name__ == '__main__':
    p = Process(target=f, args={"Child", 2})
    p.start()
    p.join()
    f("Parent", 0)
    exit()




