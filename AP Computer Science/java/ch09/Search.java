package ch09;

public class Search {
  public static void main(String[] args) {
    int arr[] = { 1, 3, 5, 7, 9, 13, 2, 31, 6 };
    int key = 31;
    int index = binary(arr, key);
    if (index == -1) {
      System.out.println("찾는 값이 없습니다.");
    } else {
      System.out.println("찾는 값의 인덱스는 " + index + "입니다.");
    }
  }

  private static int binary(int arr[], int key) {
    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {
      int mid = (left + right) / 2;
      if (arr[mid] == key) {
        return mid;
      } else if (arr[mid] < key) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return -1; 
  }
}
