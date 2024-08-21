import java.util.Random;

public class Graveler {
    public static void main(String args[]) {
        long tStart = System.currentTimeMillis();

        int roll;
        int ones;

        Random random = new Random();
        int rolls = 1000000000;
        int numRolls = 0;
        int maxOnes = 0;

        for (int i = 0; i < rolls; i++) {
            ones = 0;
            numRolls++;

            for (int j = 0; j < 231; j++) {
                roll = random.nextInt(4);

                if (roll == 0) {
                    ones++;
                }
            }

            if (ones > maxOnes) {
                maxOnes = ones;
            }

            if (maxOnes >= 177) {
                break;
            }
        }

        long tEnd = System.currentTimeMillis();

        double tElapsed = (tEnd - tStart) / 1000.0;

        System.out.printf("Highest Ones Roll: %d\n", maxOnes);
        System.out.printf("Number of Roll Sessions: %d\n", numRolls);
        System.out.printf("Runtime: %.6f s\n", tElapsed);
    }
}
