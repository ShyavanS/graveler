"""
Multithreaded Graveler code in Python (My Version).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run. Takes advantage of the threading module to
compute the problem quicker by using multiple threads. Also uses numpy to
generate an array of random integers and sum them to improve speed over
loops & list comprehension. This method is quite different from the Java and C
versions due to the optimizations necessary to get Python on the same level in
terms of speed.
"""

# Imports
import numpy as np
from threading import Thread, Lock
from time import time
from os import _exit

tStart = time()  # Start time to measure time elapsed
lock = Lock()  # Lock for global variables while using multiple threads

# Variable Declarations
threads = []
maxOnes = []
rolls = 1000000000
sampleSize = 1000000
numThreads = 10


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
    def __init__(self):
        # Use global variables
        global tStart
        global sampleSize
        global maxOnes

        tEnd = time()  # End time to measure time elapsed

        tElapsed = tEnd - tStart  # Time elapsed

        # Output
        print(f"Highest Ones Roll: {max(maxOnes)}")
        print(f"Number of Roll Sessions: {sample.counter * sampleSize}")
        print(f"Runtime: {tElapsed:.6f} s")


"""
Runs several samples of 231 rolls to count the total number of "ones" rolled.
This function is called by each thread and uses sampleSize to determine how
many samples to run.

Args:
    void

Returns:
    void
"""
def sample():
    # Use global variables
    global maxOnes
    global lock
    global sampleSize

    # Roll 4-sided die 231 times for number of samples
    roll = np.random.randint(1, 5, size=(sampleSize, 231))
    ones = (roll == 1).sum(axis=1)  # Sum number of ones rolls

    # Update local maximum ones count from this set of samples
    sampleMaxOnes = max(ones)

    with lock:
        sample.counter += 1  # Increment rolls counter with lock
        maxOnes.append(sampleMaxOnes)  # Update global maximum ones count with lock

        # Quit early if 177 "ones" have been rolled with lock
        if sampleMaxOnes >= 177:
            try:
                raise TargetReached
            except TargetReached:
                _exit(0)


# Reset rolls counter
sample.counter = 0

# Main Loop: Creates 10 threads at a time and runs them until all rolls are complete.
for i in range(rolls // sampleSize // numThreads):
    # Create threads
    for j in range(numThreads):
        t = Thread(target=sample)
        threads.append(t)
        t.start()

    # Wait until threads finish
    while threads:
        threads = [t for t in threads if t.is_alive()]

# Raise exception to quit program normally
try:
    raise TargetReached
except TargetReached:
    _exit(0)
