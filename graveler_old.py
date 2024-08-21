"""
Original Graveler code by ShoddyCast (Austin).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run. Added lines to time how long the code takes to
run and to print the time elapsed. Added comments to better document the code
and describe where runtime can be improved. Formatted code using Black formatter.
"""

# Imports
import random
import math  # Unused import
from time import time
from itertools import repeat

tStart = time() # Start time to measure time elapsed

# Variable Declarations
items = [1, 2, 3, 4]
numbers = [0, 0, 0, 0]
rolls = 0
maxOnes = 0

# Main Loop: Rolls 4-sided die 231 times for 1 billion runs,
# quits early if 177 "ones" rolls are performed in any given run.
while numbers[0] < 177 and rolls < 1000000000:
    # Keeping track of all types of rolls is inneficient, we can just keep track
    # of "ones".
    numbers = [0, 0, 0, 0]

    for i in repeat(None, 231):
        roll = random.choice(items) # Rolls 4-sided die

        # Inefficient due to extra calculation involved in "roll - 1",
        # could use list comprehension.
        numbers[roll - 1] = (numbers[roll - 1] + 1)

    rolls = rolls + 1 # Increment roll counter

    # Update maximum number of "ones" rolled
    if numbers[0] > maxOnes:
        maxOnes = numbers[0]

tEnd = time() # End time to measure time elapsed

tElapsed = tEnd - tStart # Time elapsed

# Output
print(f"Highest Ones Roll: {maxOnes}")
print(f"Number of Roll Sessions: {rolls}")
print(f"Runtime: {tElapsed:.6f} s")
