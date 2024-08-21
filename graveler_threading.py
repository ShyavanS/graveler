import numpy as np
from threading import Thread, Lock
from time import time
from os import _exit

tStart = time()
lock = Lock()

threads = []
maxOnes = []
rolls = 1000000000
sampleSize = 1000000
numThreads = 10


class TargetReached(Exception):
    def __init__(self):
        global tStart
        global rolls
        global sampleSize
        global maxOnes

        tEnd = time()

        tElapsed = tEnd - tStart

        print(f"Highest Ones Roll: {max(maxOnes)}")
        print(f"Number of Roll Sessions: {sample.counter * sampleSize}")
        print(f"Runtime: {tElapsed:.6f} s")


def sample():
    global maxOnes
    global lock

    roll = np.random.randint(1, 5, size=(sampleSize, 231))
    ones = (roll == 1).sum(axis=1)
    sampleMaxOnes = max(ones)

    with lock:
        sample.counter += 1
        maxOnes.append(sampleMaxOnes)

        if sampleMaxOnes >= 177:
            try:
                raise TargetReached
            except TargetReached:
                _exit(0)


sample.counter = 0

for i in range(rolls // sampleSize // numThreads):
    for j in range(numThreads):
        t = Thread(target=sample)
        threads.append(t)
        t.start()

    while threads:
        threads = [t for t in threads if t.is_alive()]

try:
    raise TargetReached
except TargetReached:
    _exit(0)
