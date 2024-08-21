import numpy as np
from time import time
from sys import exit

tStart = time()

rolls = 1000000000
sampleSize = 1000000


class TargetReached(Exception):
    def __init__(self, maxOnesList):
        global tStart
        global rolls
        global sampleSize

        tEnd = time()

        tElapsed = tEnd - tStart

        print(f"Highest Ones Roll: {max(maxOnesList)}")
        print(f"Number of Roll Sessions: {sample.counter * sampleSize}")
        print(f"Runtime: {tElapsed:.6f} s")


def sample():
    roll = np.random.randint(1, 5, size=(sampleSize, 231))
    ones = (roll == 1).sum(axis=1)
    sampleMaxOnes = max(ones)

    sample.counter += 1

    if sampleMaxOnes >= 177:
        try:
            raise TargetReached(maxOnesList=[sampleMaxOnes])
        except TargetReached:
            exit()

    return sampleMaxOnes


sample.counter = 0

maxOnes = [sample() for i in range(rolls // sampleSize)]

try:
    raise TargetReached(maxOnesList=maxOnes)
except TargetReached:
    exit()
