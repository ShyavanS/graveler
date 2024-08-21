import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.ArrayList;

public class GravelerThreading extends Thread {
    public static final int rolls = 1000000000;
    public static final int sampleSize = 1000000;
    public static final int numThreads = 10;
    
    public static int sampleMaxOnes;

    public static ArrayList<GravelerThreading> threads = new ArrayList<GravelerThreading>();
    public static AtomicInteger maxOnes = new AtomicInteger(0);
    public static AtomicInteger counter = new AtomicInteger(0);

    public Random random = new Random();

    public void run() {
        int roll;
        int ones;

        sampleMaxOnes = 0;

        for (int i = 0; i < sampleSize; i++) {
            ones = 0;

            for (int j = 0; j < 231; j++) {
                roll = random.nextInt(4);

                if (roll == 0) {
                    ones++;
                }
            }

            if (ones > sampleMaxOnes) {
                sampleMaxOnes = ones;
            }
        }

        counter.incrementAndGet();
        maxOnes.updateAndGet(value -> value < sampleMaxOnes ? sampleMaxOnes : value);
    }

    public static void main(String args[]) {
        long tStart = System.currentTimeMillis();

        mainloop: for (int i = 0; i < rolls / sampleSize / numThreads; i++) {
            for (int j = 0; j < numThreads; j++) {
                GravelerThreading thread = new GravelerThreading();
                threads.add(thread);
                thread.start();
            }

            while (!threads.isEmpty()) {
                for (int j = 0; j < threads.size(); j++) {
                    if (!threads.get(j).isAlive()) {
                        threads.remove(j);
                    }

                    if (maxOnes.get() >= 177) {
                        break mainloop;
                    }
                }
            }
        }

        long tEnd = System.currentTimeMillis();

        double tElapsed = (tEnd - tStart) / 1000.0;

        System.out.printf("Highest Ones Roll: %d\n", maxOnes.get());
        System.out.printf("Number of Roll Sessions: %d\n", counter.get() * sampleSize);
        System.out.printf("Runtime: %.6f s\n", tElapsed);
    }
}
