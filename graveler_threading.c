/*
Multithreaded Graveler code in C (My Version).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run. Using my rudimentary knowledge of C & online
resources I translated the same logic of my Java multithreaded code (which I
have more practice with and a better understanding of) to a rough equivalent in
C. There is almost certainly room for improvement as a result to optimize the
code and improve runtime. Code was compiled using O3 optimizations.
*/

// Imports
#include <stdio.h>
#include <stdlib.h>
#include <stdatomic.h>
#include <pthread.h>
#include <time.h>

// Constant Definitions
#define ROLLS 1000000000
#define SAMPLE_SIZE 1000000
#define NUM_THREADS 10

// Variable Declarations
int sampleMaxOnes;
pthread_mutex_t lock; // Mutex to lock variable while using multiple threads

// Atomic integers to prevent overwritting values when using multiple threads
atomic_int maxOnes = 0;
atomic_int counter = 0;

/*
Runs several samples of 231 rolls to count the total number of "ones" rolled.
This function is called by each thread via a pointer and uses SAMPLE_SIZE to
determine how many samples to run.

Args:
    void

Returns:
    void
*/
void *sample(void *arg)
{
    // Initialize variables
    int roll;
    int ones;

    sampleMaxOnes = 0;

    // Loop accross the sample size limit for each thread
    for (int i = 0; i < SAMPLE_SIZE; i++)
    {
        ones = 0; // Reset ones count

        for (int j = 0; j < 231; j++) // Loop for 231 rolls
        {
            roll = rand() % 4; // Roll 4-sided die

            // Increment local ones counter if a "one" was rolled
            if (roll == 0)
            {
                ones++;
            }
        }

        // Update local maximum ones count from this set of samples
        if (ones > sampleMaxOnes)
        {
            sampleMaxOnes = ones;
        }
    }

    atomic_fetch_add(&counter, 1); // Increment rolls counter atomically

    pthread_mutex_lock(&lock); // Lock global variable to make edits thread-safe

    // Update global maximum ones count
    if (sampleMaxOnes > maxOnes)
    {
        maxOnes = sampleMaxOnes;
    }

    pthread_mutex_unlock(&lock); // Unlock global variable for other threads
}

/*
Main function. Initiates 10 threads at a time and calculates maximum number of
"ones" rolled across all samples. Calculates runtime for code. Outputs statistics.

Args:
    void

Returns:
    void
*/
int main()
{
    clock_t tStart = clock(); // Start time to measure time elapsed

    // Initialize pseudorandom number generator seed
    srand(time(NULL));

    // Initialize threads and mutex
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&lock, NULL);

    // Main Loop: Creates 10 threads at a time and runs them until all rolls
    // are complete.
    for (int i = 0; i < ROLLS / SAMPLE_SIZE / NUM_THREADS; i++)
    {
        for (int j = 0; j < NUM_THREADS; j++)
        {
            pthread_create(&threads[j], NULL, sample, NULL); // Create threads
        }

        for (int j = 0; j < NUM_THREADS; j++)
        {
            if (maxOnes >= 177)
            {
                goto output; // Quit early if 177 "ones" have been rolled
            }

            pthread_join(threads[j], NULL); // Wait until threads finish
        }
    }

output:
    pthread_mutex_destroy(&lock); // Destroy mutex

    clock_t tEnd = clock(); // End time to measure time elapsed

    double tElapsed = (tEnd - tStart) / 1000.0; // Time elapsed

    // Output
    printf("Highest Ones Roll: %d\n", maxOnes);
    printf("Number of Roll Sessions: %d\n", atomic_load(&counter) * SAMPLE_SIZE);
    printf("Runtime: %.6f s\n", tElapsed);
}
