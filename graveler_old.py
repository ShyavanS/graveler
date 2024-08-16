import random
import math
from time import time
from itertools import repeat

tStart = time()

items = [1, 2, 3, 4]
numbers = [0, 0, 0, 0]
rolls = 0
maxOnes = 0

while numbers[0] < 177 and rolls < 1000000000:
    numbers = [0, 0, 0, 0]
    
    for i in repeat(None, 231):
        roll = random.choice(items)
        numbers[roll - 1] = numbers[roll - 1] + 1
    
    rolls = rolls + 1
    
    if numbers[0] > maxOnes:
        maxOnes = numbers[0]

tEnd = time()

tElapsed = tEnd - tStart

print(f"Highest Ones Roll: {maxOnes}")
print(f"Number of Roll Sessions: {rolls}")
print(f"Runtime: {tElapsed:.3f} s")
