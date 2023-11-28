package ch09;

public class UseSort {
  public static void main(String[] args) {
    int[] arr = { 1, 3, 5, 7, 9, 2, 4, 6, 8, 10 };
    QuickSort.Quick(arr, 'a');
    print(arr);
  }

  public static void print(int[] arr) {
    System.out.print("[");
    for (int i = 0; i < arr.length; i++) {
        System.out.print(arr[i]);
        if (i != arr.length - 1) System.out.print(", ");
    }
    System.out.print("]");
    System.out.println();
  }
}
