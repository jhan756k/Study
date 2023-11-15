package ch09;

public class CompareSort {
    public static void main(String[] args) {
        int SIZE = 100;
        int[] arr = new int[SIZE];
        for (int i = 0; i < SIZE; i++) {
            arr[i] = (int) (Math.random()*100);
        }

        AllSorts.Selection(arr);
        AllSorts.print(arr);
    }
}
