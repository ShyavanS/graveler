#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    clock_t tStart = clock();

    int roll;
    int ones;

    int rolls = 1000000000;
    int numRolls = 0;
    int maxOnes = 0;

    srand(time(NULL));

    for (int i = 0; i < rolls; i++)
    {
        ones = 0;
        numRolls++;

        for (int j = 0; j < 231; j++)
        {
            roll = rand() % 4;

            if (roll == 0)
            {
                ones++;
            }
        }

        if (ones > maxOnes)
        {
            maxOnes = ones;
        }

        if (maxOnes >= 177)
        {
            break;
        }
    }

    clock_t tEnd = clock();

    double tElapsed = (tEnd - tStart) / 1000.0;

    printf("Highest Ones Roll: %d\n", maxOnes);
    printf("Number of Roll Sessions: %d\n", numRolls);
    printf("Runtime: %.6f s\n", tElapsed);
}
