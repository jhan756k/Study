package ch09;

public class MergeSort {
  private static void Merge(int[] arr, int start, int end) {
    int[] temp = new int[end - start + 1];
    if (start == end)
      return;

    int mid = (start + end) / 2;
    Merge(arr, start, mid);
    Merge(arr, mid + 1, end);

    int i = start, j = mid + 1, k = 0;

    while (i <= mid || j <= end) {
      if (i > mid) {
        temp[k] = arr[j];
        k++;
        j++;
      } else if (j > end) {
        temp[k] = arr[i];
        k++;
        i++;
      } else if (arr[i] < arr[j]) {
        temp[k] = arr[i];
        k++;
        i++;
      } else {
        temp[k] = arr[j];
        k++;
        j++;
      }
    }

    for (int x = start; x <= end; x++) {
      arr[x] = temp[x - start];
    }
  }

  public static void Merge(int[] arr, char order) {
    if (order == 'a') {
      Merge(arr, 0, arr.length - 1);
    } else if (order == 'd') {
      for (int i = 0; i < arr.length; i++) {
        arr[i] = -arr[i];
      }
      Merge(arr, 0, arr.length - 1);
      for (int i = 0; i < arr.length; i++) {
        arr[i] = -arr[i];
      }
    }
  }

}