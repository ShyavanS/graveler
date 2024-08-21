/*
Multithreaded Graveler code in Java (My Version).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run. Extends Java Thread class to compute the problem
quicker by using multiple threads.
*/

// Imports
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.ArrayList;

public class GravelerThreading extends Thread {
    // Constant Definitions
    public static final int rolls = 1000000000;
    public static final int sampleSize = 1000000;
    public static final int numThreads = 10;
    
    // Variable Declarations
    public static int sampleMaxOnes;

    public static ArrayList<GravelerThreading> threads = new ArrayList<GravelerThreading>();

    // Atomic integers to prevent overwritting values when using multiple threads
    public static AtomicInteger maxOnes = new AtomicInteger(0);
    public static AtomicInteger counter = new AtomicInteger(0);

    // Initialize pseudorandom number generator
    public Random random = new Random();

    /*
    Runs several samples of 231 rolls to count the total number of "ones" rolled.
    This function is called by each thread and uses sampleSize to determine how
    many samples to run.

    Args:
        void

    Returns:
        void
    */
    public void run() {
        // Initialize variables
        int roll;
        int ones;

        sampleMaxOnes = 0;

        // Loop accross the sample size limit for each thread
        for (int i = 0; i < sampleSize; i++) {
            ones = 0; // Reset ones count

            // Loop for 231 rolls
            for (int j = 0; j < 231; j++) {
                roll = random.nextInt(4); // Roll 4-sided die

                // Increment local ones counter if a "one" was rolled
                if (roll == 0) {
                    ones++;
                }
            }

            // Update local maximum ones count from this set of samples
            if (ones > sampleMaxOnes) {
                sampleMaxOnes = ones;
            }
        }

        counter.incrementAndGet(); // Increment rolls counter atomically

        // Update global maximum ones count atomically
        maxOnes.updateAndGet(value -> value < sampleMaxOnes ? sampleMaxOnes : value);
    }

    /*
    Main function. Initiates 10 threads at a time and calculates maximum number of
    "ones" rolled across all samples. Calculates runtime for code. Outputs statistics.

    Args:
        void

    Returns:
        void
    */
    public static void main(String args[]) {
        // Start time to measure time elapsed
        long tStart = System.currentTimeMillis();

        // Main Loop: Creates 10 threads at a time and runs them until all rolls
        // are complete.
        mainloop: for (int i = 0; i < rolls / sampleSize / numThreads; i++) {
            // Create threads
            for (int j = 0; j < numThreads; j++) {
                GravelerThreading thread = new GravelerThreading();
                threads.add(thread);
                thread.start();
            }

            // Wait until threads finish
            while (!threads.isEmpty()) {
                for (int j = 0; j < threads.size(); j++) {
                    if (!threads.get(j).isAlive()) {
                        threads.remove(j);
                    }

                    // Quit early if 177 "ones" have been rolled
                    if (maxOnes.get() >= 177) {
                        break mainloop;
                    }
                }
            }
        }

        long tEnd = System.currentTimeMillis(); // End time to measure time elapsed

        double tElapsed = (tEnd - tStart) / 1000.0; // Time elapsed

        // Output
        System.out.printf("Highest Ones Roll: %d\n", maxOnes.get());
        System.out.printf("Number of Roll Sessions: %d\n", counter.get() * sampleSize);
        System.out.printf("Runtime: %.6f s\n", tElapsed);
    }
}
