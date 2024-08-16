import random
from threading import Thread
from time import time

tStart = time()
threads = []

maxOnes = []
rolls = 1000000000
items = [1, 2, 3, 4]


def sample():
    global maxOnes
    ones = 0

    for i in range(231):
        roll = random.choice(items)

        if roll == 1:
            ones += 1

    maxOnes.append(ones)


for i in range(rolls):
    t = Thread(target=sample)
    threads.append(t)
    t.start()

while threads:
    threads = [t for t in threads if t.is_alive()]

tEnd = time()

tElapsed = tEnd - tStart

print(f"Highest Ones Roll: {max(maxOnes)}")
print(f"Number of Roll Sessions: {rolls}")
print(f"Runtime: {tElapsed:.3f} s")
