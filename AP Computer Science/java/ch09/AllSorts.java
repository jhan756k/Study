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
        int temp[] = new int[end-start+1];
        if (start == end) return;
        int mid = (start + end) / 2;
        Merge(arr, start, mid);
        Merge(arr, mid+1, end);
        int i = start;
        int j = mid+1;
        int k = 0;
        while (i <= mid && j <= end) {
            if (arr[i] < arr[j]) {
                temp[k] = arr[i];
                i++;
                k++;
            }
            else {
                temp[k] = arr[j];
                k++;
                j++;
            }
        }
        while (i <= mid) {
            temp[k] = arr[i];
            k++;
            i++;
        }
        while (j <= end) {
            temp[k] = arr[j];
            k++;
            j++;
        }
        print(temp);
        for (int l = start; l <= end; l++) { // 값 arr에 대입
            arr[l] = temp[l-start];
        }
    }

    public static void MergeSort(int[] arr) {
        Merge(arr, 0, arr.length - 1);
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
        Insertion(arr);
        print(arr);

        /*
        DB - File의 집합
        File - record의 집합
        Record - field의 집합
        Field - character의 집합
        Character
        */
    }
}