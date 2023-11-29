package ch09;

public class HeapSort {
  public static void main(String[] args) {
    int[]test = {4,3,5,1,2};
    int[]ans = Heap(test);
    for (int i = 1; i < ans.length; i++) {
      System.out.print(ans[i] + " ");
    }
  }
  public static int[] Heap(int[] a) {
    int[] heap = new int[a.length + 1];
    heap[0] = 1; 
    for (int i = 1; i <= a.length; i++) { // init heap
      insert(heap, a[i - 1]);
    }
    return heap;
  }

  private static void insert(int[] heap, int x) {
    heap[heap[0]] = x; // heap[0]은 마지막 원소 index 값
    upHeap(heap, heap[0]);
    heap[0]++;
  }

  private static void upHeap(int[] heap, int k) {
    while (k > 1 && heap[k / 2] > heap[k]) {
      int temp = heap[k / 2];
      heap[k / 2] = heap[k];
      heap[k] = temp;
      k = k / 2;
    }
  }

  private static void remove(int[] a) {

  }

  private static void downHeap(int[] heap, int k, int n) {

  }
}
