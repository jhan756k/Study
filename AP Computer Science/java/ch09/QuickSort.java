package ch09;

public class QuickSort {
  public static void Quick(int[] arr, int order) {
    if (order == 'a') {
      Quick(arr, 0, arr.length - 1);
    } else if (order == 'd') {
      for (int i = 0; i < arr.length; i++) {
        arr[i] = -arr[i];
      }
      Quick(arr, 0, arr.length - 1);
      for (int i = 0; i < arr.length; i++) {
        arr[i] = -arr[i];
      }
    }
  }

  private static void Quick(int[] arr, int low, int high) {
    if (low < high) {
      int mid = divide(arr, low, high);
      Quick(arr, low, mid - 1);
      Quick(arr, mid + 1, high);
    }
  }

  private static int divide(int[] arr, int low, int high) {
    int pivot = arr[low];
    int i = (low + 1);
    for (int j = high; j >= i; j--) {
      if (arr[j] <= pivot) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j++;
      }
    }
    arr[low] = arr[i - 1];
    arr[i - 1] = pivot;
    return i - 1;
  }
}
