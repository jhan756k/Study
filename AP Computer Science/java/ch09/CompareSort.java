package ch09;

import java.util.Random;

public class CompareSort {
    public static void main(String[] args) {
        int size = 100000;
        int[] arr = new int[size];
        Random rand = new Random(1);

        double sum = 0;
        for (int i = 0; i < 10; i++) {
            // for (int a = 0; a < size; a++) {
            //     arr[a] = rand.nextInt(2000000001) - 1000000000;
            // }
            // for (int a = 0; a < size; a++) {
            //     arr[a] = a;
            // }
            for (int a = 0; a < size; a++) {
                arr[a] = size - a;
            }

            long startTime = System.currentTimeMillis();

            // AllSorts.Selection(arr);
            // AllSorts.Insertion(arr);
            QuickSort.Quick(arr, 'a');
            // MergeSort.Merge(arr, 'a');
            // int [] heap = HeapSort.Heap(arr);

            long endTime = System.currentTimeMillis();
            
            long elapsedTime = endTime - startTime;
            sum += elapsedTime;
            System.out.println(i + 1 + "번째: " + elapsedTime + " 밀리초");
        }
        System.out.println();
        System.out.println("평균: " + sum / 10 + " 밀리초");
    }
}
