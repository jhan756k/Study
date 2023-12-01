package ch09;

public class HeapSort {
  public static void main(String[] args) {
    int[] test = { 4, 3, 5, 1, 2, 2, 3, 1231, 44, 96, -23, -123 };
    int[] ans = Heap(test);
    System.out.println("Size: " + (ans[0]));

    for (int i = 1; i < ans.length; i++) {
      System.out.print(remove(ans) + ", ");
    }
    System.out.println();
  }

  public static int[] Heap(int[] a) {
    int[] heap = new int[a.length + 1];
    heap[0] = 1;
    for (int i = 1; i <= a.length; i++) { // init heap
      insert(heap, a[i - 1]);
    }
    heap[0]--; // 마지막에 하나 추가되는거 다시 빼기
    return heap;
  }

  private static void insert(int[] heap, int x) {
    heap[heap[0]] = x; // heap[0]은 마지막 원소 index 값
    upHeap(heap, heap[0]);
    heap[0]++;
  }

  private static void upHeap(int[] heap, int k) {
    while (k > 1 && heap[k / 2] > heap[k]) {
      swap(heap, k / 2, k);
      k = k / 2;
    }
  }

  private static int remove(int[] heap) {
    int x = heap[1];
    heap[1] = heap[heap[0]];
    heap[heap[0]] = 0;
    heap[0]--;
    downHeap(heap);
    return x;
  }

  private static void downHeap(int[] heap) {
    int k = 1;
    while (2 * k <= heap[0]) {
      int a = 2 * k;
      int b = 2 * k + 1;
      int smaller;

      if (b > heap[0] || heap[a] < heap[b]) {
        smaller = a;
      } else {
        smaller = b;
      }
      if (heap[k] < heap[smaller]) {
        break;
      }
      swap(heap, k, smaller);
      k = smaller;
    }
  }

  private static void swap(int[] heap, int i, int j) {
    int temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
  }
}
