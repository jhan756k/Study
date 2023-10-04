import java.util.Random;

public class RandomFlat {
    public static void main(String[] args) {

        // Flat 한지 확인
        Random r = new Random();
        int times = 1000000;
        float arr[] = new float[times];
        int start = 0;
        int end = 10;
        int sd = 0;

        for (int i = 0; i < times; i++) {
            arr[i] = start + (end - start) * r.nextFloat();
            sd += arr[i];
        }
        sd /= arr.length;
        float s = 0;
        int[] count = new int[end - start + 1];
        for (int i = 0; i < times; i++) {
            count[(int) arr[i] - start]++;
            s += Math.pow(arr[i] - sd, 2);
        }
        for (int i = 0; i < end - start + 1; i++) {
            System.out.println(count[i]);
        }
        System.out.println(s/arr.length);
    }
}