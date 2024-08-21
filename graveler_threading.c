#include <stdio.h>
#include <stdlib.h>
#include <stdatomic.h>
#include <pthread.h>
#include <time.h>

#define ROLLS 1000000000
#define SAMPLE_SIZE 1000000
#define NUM_THREADS 10

int sampleMaxOnes;
pthread_mutex_t lock;

atomic_int maxOnes = 0;
atomic_int counter = 0;

void *sample(void *arg)
{
    int roll;
    int ones;

    sampleMaxOnes = 0;

    for (int i = 0; i < SAMPLE_SIZE; i++)
    {
        ones = 0;

        for (int j = 0; j < 231; j++)
        {
            roll = rand() % 4;

            if (roll == 0)
            {
                ones++;
            }
        }

        if (ones > sampleMaxOnes)
        {
            sampleMaxOnes = ones;
        }
    }

    atomic_fetch_add(&counter, 1);

    pthread_mutex_lock(&lock);

    if (sampleMaxOnes > maxOnes)
    {
        maxOnes = sampleMaxOnes;
    }

    pthread_mutex_unlock(&lock);
}

int main()
{
    clock_t tStart = clock();

    srand(time(NULL));
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&lock, NULL);

    for (int i = 0; i < ROLLS / SAMPLE_SIZE / NUM_THREADS; i++)
    {
        for (int j = 0; j < NUM_THREADS; j++)
        {
            pthread_create(&threads[j], NULL, sample, NULL);
        }

        for (int j = 0; j < NUM_THREADS; j++)
        {
            if (maxOnes >= 177)
            {
                goto output;
            }

            pthread_join(threads[j], NULL);
        }
    }

output:
    pthread_mutex_destroy(&lock);
    
    clock_t tEnd = clock();

    double tElapsed = (tEnd - tStart) / 1000.0;

    printf("Highest Ones Roll: %d\n", maxOnes);
    printf("Number of Roll Sessions: %d\n", atomic_load(&counter) * SAMPLE_SIZE);
    printf("Runtime: %.6f s\n", tElapsed);
}
