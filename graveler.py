import random
from time import time

tStart = time()

rolls = 1000000000
items = [1, 2, 3, 4]


def sample():
    ones = 0

    for i in range(231):
        roll = random.choice(items)

        if roll == 1:
            ones += 1

    return ones


maxOnes = [sample() for i in range(rolls)]

tEnd = time()

tElapsed = tEnd - tStart

print(f"Highest Ones Roll: {max(maxOnes)}")
print(f"Number of Roll Sessions: {rolls}")
print(f"Runtime: {tElapsed:.3f} s")
