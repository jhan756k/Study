package ch09;

public class AllSorts {

    public static void Selection(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int min_ind = i;
            for (int j = i; j < arr.length; j++) {
                if (arr[j] < arr[min_ind]) {
                    min_ind = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_ind];
            arr[min_ind] = temp;
        }
    }

    public static void Insertion(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            for (int j = i-1; j > -1; j--) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
                else break;
            }
        }
    }

    public static void Bubble(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for(int j = 0 ; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j+1]; 
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    public static void Merge(int[] arr, int start, int end) {
        int[] temp = new int[end - start + 1]; 
        if (start == end) return; // 배열 길이 1이면 그냥 리턴
    
        int mid = (start + end) / 2;
        Merge(arr, start, mid);
        Merge(arr, mid + 1, end);
    
        int i = start, j = mid + 1, k = 0;

        while (i <= mid || j <= end) {
            if (i > mid) { 
                temp[k++] = arr[j++];
            } else if (j > end) {
                temp[k++] = arr[i++];
            } else if (arr[i] < arr[j]) { 
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }
    
        for (int x = start; x <= end; x++) {
            arr[x] = temp[x - start];
        }
    }
    
    public static void MergeSort(int[] arr) {
        Merge(arr, 0, arr.length - 1);
    }

    public static void Quick(int[] arr, int low, int high) {
        if (low < high) {
            int mid = divide(arr, low, high);
            Quick(arr, low, mid - 1);
            Quick(arr, mid + 1, high);
        }
    }

    private static int divide(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = (low + 1);
        for (int j = i; j <= high; j++) {
            if (arr[j] <= pivot) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
            }
        }
        arr[low] = arr[i - 1];
        arr[i - 1] = pivot;
        return i - 1;
    }

    public static void QuickSort(int[] arr) {
        Quick(arr, 0, arr.length - 1);
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

    public static void main(String[] args) {
        int arr[] = { 5, 2, 7, 3, 9, 1, 4, 8, 6 };
        QuickSort(arr);
        print(arr);

        /*
        DB - File의 집합
        File - record의 집합
        Record - field의 집합
        Field - character의 집합
        Character

        single/double/더 큰 precision floating point
        */
    }
}