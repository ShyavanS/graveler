/*
Single-threaded Graveler code in Java (My Version).

Rolls 4-sided die 231 times for 1 billion runs, quits early if 177 "ones" rolls
are performed in any given run.
*/

// Imports
import java.util.Random;

public class Graveler {
    /*
    Main function. Runs 1 billion samples of 231 rolls to count the total number of
    "ones" rolled in each sample and find the maximum number of "ones" rolled across
    all samples. Calculates runtime for code. Outputs statistics.

    Args:
        void

    Returns:
        void
    */
    public static void main(String args[]) {
        long tStart = System.currentTimeMillis(); // Start time to measure time elapsed

        // Variable Declarations
        int roll;
        int ones;

        Random random = new Random(); // Initialize pseudorandom number generator
        int rolls = 1000000000;
        int numRolls = 0;
        int maxOnes = 0;

        // Main Loop: Runs 231 dice rolls 1 billion times
        for (int i = 0; i < rolls; i++) {
            ones = 0; // Reset ones count
            numRolls++; // Increment rolls counter

            // Loop for 231 rolls
            for (int j = 0; j < 231; j++) {
                roll = random.nextInt(4); // Roll 4-sided die

                // Increment ones counter if a "one" was rolled
                if (roll == 0) {
                    ones++;
                }
            }

            // Update maximum ones count
            if (ones > maxOnes) {
                maxOnes = ones;
            }

            if (maxOnes >= 177) {
                break; // Quit early if 177 "ones" have been rolled
            }
        }

        long tEnd = System.currentTimeMillis(); // End time to measure time elapsed

        double tElapsed = (tEnd - tStart) / 1000.0; // Time elapsed

        // Output
        System.out.printf("Highest Ones Roll: %d\n", maxOnes);
        System.out.printf("Number of Roll Sessions: %d\n", numRolls);
        System.out.printf("Runtime: %.6f s\n", tElapsed);
    }
}
