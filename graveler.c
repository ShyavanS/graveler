/*
Single-threaded Graveler code in C (My Version).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run. Using my rudimentary knowledge of C & online
resources I translated the same logic of my Java single-threaded code (which I
have more practice with and a better understanding of) to a rough equivalent in
C. There is almost certainly room for improvement as a result to optimize the
code and improve runtime. Code was compiled using O3 optimizations.
*/

// Imports
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
Main function. Runs 1 billion samples of 231 rolls to count the total number of
"ones" rolled in each sample and find the maximum number of "ones" rolled across
all samples. Calculates runtime for code. Outputs statistics.

Args:
    void

Returns:
    void
*/
int main()
{
    clock_t tStart = clock(); // Start time to measure time elapsed

    // Initialize variables
    int roll;
    int ones;

    int rolls = 1000000000;
    int numRolls = 0;
    int maxOnes = 0;

    // Initialize pseudorandom number generator seed
    srand(time(NULL));

    // Main Loop: Runs 231 dice rolls 1 billion times
    for (int i = 0; i < rolls; i++)
    {
        ones = 0; // Reset ones count
        numRolls++; // Increment rolls counter

        for (int j = 0; j < 231; j++) // Loop for 231 rolls
        {
            roll = rand() % 4; // Roll 4-sided die

            // Increment ones counter if a "one" was rolled
            if (roll == 0)
            {
                ones++;
            }
        }

        // Update maximum ones count
        if (ones > maxOnes)
        {
            maxOnes = ones;
        }

        if (maxOnes >= 177)
        {
            break; // Quit early if 177 "ones" have been rolled
        }
    }

    clock_t tEnd = clock(); // End time to measure time elapsed

    double tElapsed = (tEnd - tStart) / 1000.0; // Time elapsed

    // Output
    printf("Highest Ones Roll: %d\n", maxOnes);
    printf("Number of Roll Sessions: %d\n", numRolls);
    printf("Runtime: %.6f s\n", tElapsed);
}
