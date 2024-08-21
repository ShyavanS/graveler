"""
Single-threaded Graveler code in Python (My Version).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run. Uses numpy to generate an array of random
integers and sum them to improve speed over loops & list comprehension. This
method is quite different from the Java and C versions due to the optimizations
necessary to get Python on the same level in terms of speed.
"""

# Imports
import numpy as np
from time import time
from sys import exit

tStart = time()  # Start time to measure time elapsed

# Variable Declarations
rolls = 1000000000
sampleSize = 1000000


"""
TargetReached class, extending Exception class.

Custom exception to tell the program to exit under specific conditions and
output the statistics from the run.
"""
class TargetReached(Exception):
    """
    Class init function, calculates time elapsed and outputs statistics
    from run.

    Args:
        self

    Returns:
        void
    """
    def __init__(self, maxOnesList):
        # Use global variables
        global tStart
        global rolls
        global sampleSize

        tEnd = time()  # End time to measure time elapsed

        tElapsed = tEnd - tStart  # Time elapsed

        # Output
        print(f"Highest Ones Roll: {max(maxOnesList)}")
        print(f"Number of Roll Sessions: {sample.counter * sampleSize}")
        print(f"Runtime: {tElapsed:.6f} s")


"""
Runs several samples of 231 rolls to count the total number of "ones" rolled.
This function is called in sequence by a list comprehension task.

Args:
    void

Returns:
    void
"""
def sample():
    # Roll 4-sided die 231 times for number of samples
    roll = np.random.randint(1, 5, size=(sampleSize, 231))
    ones = (roll == 1).sum(axis=1)  # Sum number of ones rolls
    
    # Update maximum ones count from this set of samples
    sampleMaxOnes = max(ones)

    sample.counter += 1  # Increment rolls counter

    # Quit early if 177 "ones" have been rolled
    if sampleMaxOnes >= 177:
        try:
            raise TargetReached(maxOnesList=[sampleMaxOnes])
        except TargetReached:
            exit()

    return sampleMaxOnes  # Return maximum ones count


# Reset rolls counter
sample.counter = 0

# Create list of maximum number of "ones" rolled from call of each sample set
maxOnes = [sample() for i in range(rolls // sampleSize)]

# Raise exception to quit program normally
try:
    raise TargetReached(maxOnesList=maxOnes)
except TargetReached:
    exit()
